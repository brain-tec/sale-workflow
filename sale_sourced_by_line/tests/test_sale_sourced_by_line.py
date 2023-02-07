# Copyright 2013-2014 Camptocamp SA - Guewen Baconnier
# © 2016 Eficent Business and IT Consulting Services S.L.
# © 2016 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestSaleSourcedByLine(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super(TestSaleSourcedByLine, cls).setUpClass()
        cls.env(context=dict(cls.env.context, tracking_disable=True))
        cls.company = cls.env.ref("base.main_company")
        cls.company_shop = cls.env.ref("stock.res_company_1")

        cls.user = cls.env["res.users"].create(
            {
                "login": "Salesman Chicago Sourced By Line",
                "email": "test@test.com",
                "name": "Salesman Chicago Sourced By Line",
                "groups_id": [(4, cls.env.ref("sales_team.group_sale_salesman").id)],
                "company_ids": [(6, 0, (cls.company | cls.company_shop).ids)],
                "company_id": cls.company_shop.id,
            }
        )
        cls.sale_order_model = cls.env["sale.order"].with_user(cls.user)
        cls.sale_order_line_model = cls.env["sale.order.line"].with_user(cls.user)
        cls.stock_move_model = cls.env["stock.move"]
        cls.stock_warehouse_model = cls.env["stock.warehouse"]

        # Refs
        cls.customer = cls.env.ref("base.res_partner_2")
        cls.product_1 = cls.env.ref("product.product_product_27")
        cls.product_2 = cls.env.ref("product.product_product_24")
        cls.warehouse_shop0 = cls.env.ref("stock.stock_warehouse_shop0")
        cls.warehouse0 = cls.env.ref("stock.warehouse0")
        cls.warehouse1 = cls.stock_warehouse_model.create(
            {"name": "Test Warehouse", "code": "TWH"}
        )

        # # TODO: Two tests failed because of a product not having a route set.
        # #       But with it the last test fails because the stock.move
        # #       doesn't have a warehouse associated.
        # route_1 = self.env["stock.location.route"].create({
        #     "name": "SO -> Customer",
        #     "product_selectable": True,
        #     "sale_selectable": True,
        #     "rule_ids": [
        #         (0, 0, {
        #             'name': 'SO -> Customer',
        #             'action': 'pull_push',
        #             'picking_type_id': self.env.ref('stock.picking_type_out').id,
        #             'location_src_id': self.warehouse0.lot_stock_id.id,
        #             'location_id': self.env.ref('stock.stock_location_customers').id,
        #         }),
        #     ],
        # })
        # self.product_1.route_ids = [(6, 0, route_1.ids)]

    def test_sales_order_multi_source(self):
        so = self.sale_order_model.create(
            {
                "partner_id": self.customer.id,
            }
        )
        self.sale_order_line_model.create(
            {
                "product_id": self.product_1.id,
                "product_uom_qty": 8,
                "warehouse_id": self.warehouse1.id,
                "order_id": so.id,
            }
        )
        self.sale_order_line_model.create(
            {
                "product_id": self.product_2.id,
                "product_uom_qty": 8,
                "warehouse_id": self.warehouse0.id,
                "order_id": so.id,
            }
        )
        # confirm quotation
        so.action_confirm()
        self.assertEqual(
            len(so.picking_ids),
            2,
            "2 delivery orders expected. Got %s instead" % len(so.picking_ids),
        )
        for line in so.order_line:
            self.assertEqual(
                line.procurement_group_id.name,
                line.order_id.name + "/" + line.warehouse_id.name,
                "The name of the procurement group is not " "correct.",
            )
            moves = self.stock_move_model.search(
                [("group_id", "=", line.procurement_group_id.id)]
            )
            for move in moves:
                self.assertEqual(
                    move.group_id,
                    line.procurement_group_id,
                    "The group in the stock move does not "
                    "match with the procurement group in "
                    "the sales order line.",
                )
                self.assertEqual(
                    move.picking_id.group_id,
                    line.procurement_group_id,
                    "The group in the stock picking does "
                    "not match with the procurement group "
                    "in the sales order line.",
                )

    def test_sales_order_no_source(self):
        so = self.sale_order_model.create(
            {
                "partner_id": self.customer.id,
                "warehouse_id": self.warehouse1.id,
            }
        )
        self.sale_order_line_model.create(
            {"product_id": self.product_1.id, "product_uom_qty": 8, "order_id": so.id}
        )
        self.sale_order_line_model.create(
            {"product_id": self.product_2.id, "product_uom_qty": 8, "order_id": so.id}
        )
        # confirm quotation
        so.action_confirm()
        self.assertEqual(
            len(so.picking_ids),
            1,
            "1 delivery order expected. Got %s instead" % len(so.picking_ids),
        )

    def test_sale_order_source(self):
        so = self.sale_order_model.create(
            {
                "partner_id": self.customer.id,
            }
        )
        self.sale_order_line_model.create(
            {
                "product_id": self.product_1.id,
                "product_uom_qty": 8,
                "warehouse_id": self.warehouse1.id,
                "order_id": so.id,
            }
        )
        self.sale_order_line_model.create(
            {
                "product_id": self.product_2.id,
                "product_uom_qty": 8,
                "warehouse_id": self.warehouse0.id,
                "order_id": so.id,
            }
        )
        # confirm quotation
        so.action_confirm()
        for line in so.order_line:
            moves = self.stock_move_model.search(
                [("group_id", "=", line.procurement_group_id.id)]
            )
            for move in moves:
                self.assertEqual(
                    move.warehouse_id,
                    line.warehouse_id,
                    "The warehouse in the stock move does not "
                    "match with the Sales order line.",
                )
