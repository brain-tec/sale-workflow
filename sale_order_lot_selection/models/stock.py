from odoo import models


class StockMove(models.Model):
    _inherit = "stock.move"

    def _update_reserved_quantity(
        self,
        need,
        available_quantity,
        location_id,
        lot_id=None,
        package_id=None,
        owner_id=None,
        strict=True,
    ):
        if self._context.get("sol_lot_id"):
            lot_id = self._get_sol_lot_id()
        return super()._update_reserved_quantity(
            need,
            available_quantity,
            location_id,
            lot_id=lot_id,
            package_id=package_id,
            owner_id=owner_id,
            strict=strict,
        )

    def _get_sol_lot_id(self):
        if self.sale_line_id:
            return self.sale_line_id.lot_id
        else:
            for move in self.move_dest_ids:
                lot_id = move._get_sol_lot_id()
                if lot_id:
                    return lot_id

    def _get_assigned_move_ids(self):
        move_ids = self.env["stock.move"]
        if self.state == "assigned":
            move_ids |= self
        for move in self.move_orig_ids:
            move_ids |= move._get_assigned_move_ids()
        return move_ids

    # This method has caused some issues with tickets:
    # bt#11722, bt#12546, bt#12985
    # In some cases it does not work because the lot can not be found in the
    # sales order line, but it could be found
    # in the moves. So we are enhancing this method to do both actions using
    # the method "_get_sol_lot_id"
    def _prepare_move_line_vals(self, quantity=None, reserved_quant=None):
        vals = super()._prepare_move_line_vals(
            quantity=quantity, reserved_quant=reserved_quant
        )
        lot_id = self._get_sol_lot_id()
        if reserved_quant and lot_id:
            vals["lot_id"] = lot_id.id
        return vals
