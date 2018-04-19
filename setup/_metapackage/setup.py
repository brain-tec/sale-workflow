import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo10-addons-oca-sale-workflow",
    description="Meta package for oca-sale-workflow Odoo addons",
    version=version,
    install_requires=[
        'odoo10-addon-product_price_category',
        'odoo10-addon-sale_automatic_workflow',
        'odoo10-addon-sale_automatic_workflow_exception',
        'odoo10-addon-sale_automatic_workflow_payment_mode',
        'odoo10-addon-sale_cancel_reason',
        'odoo10-addon-sale_commercial_partner',
        'odoo10-addon-sale_company_currency',
        'odoo10-addon-sale_exception',
        'odoo10-addon-sale_force_invoiced',
        'odoo10-addon-sale_generator',
        'odoo10-addon-sale_invoice_group_method',
        'odoo10-addon-sale_isolated_quotation',
        'odoo10-addon-sale_layout_hidden',
        'odoo10-addon-sale_merge_draft_invoice',
        'odoo10-addon-sale_order_action_invoice_create_hook',
        'odoo10-addon-sale_order_invoicing_finished_task',
        'odoo10-addon-sale_order_line_date',
        'odoo10-addon-sale_order_line_description',
        'odoo10-addon-sale_order_line_sequence',
        'odoo10-addon-sale_order_lot_generator',
        'odoo10-addon-sale_order_lot_mrp',
        'odoo10-addon-sale_order_lot_selection',
        'odoo10-addon-sale_order_margin_percent',
        'odoo10-addon-sale_order_price_recalculation',
        'odoo10-addon-sale_order_revision',
        'odoo10-addon-sale_order_type',
        'odoo10-addon-sale_owner_stock_sourcing',
        'odoo10-addon-sale_procurement_group_by_line',
        'odoo10-addon-sale_product_set',
        'odoo10-addon-sale_product_set_layout',
        'odoo10-addon-sale_rental',
        'odoo10-addon-sale_revert_done',
        'odoo10-addon-sale_shipping_info_helper',
        'odoo10-addon-sale_sourced_by_line',
        'odoo10-addon-sale_start_end_dates',
        'odoo10-addon-sale_stock_picking_blocking',
        'odoo10-addon-sale_triple_discount',
        'odoo10-addon-sale_validity',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
