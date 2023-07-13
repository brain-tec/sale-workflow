import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo13-addons-oca-sale-workflow",
    description="Meta package for oca-sale-workflow Odoo addons",
    version=version,
    install_requires=[
        'odoo13-addon-partner_contact_sale_info_propagation',
        'odoo13-addon-partner_prospect',
        'odoo13-addon-partner_sale_pivot',
        'odoo13-addon-portal_sale_personal_data_only',
        'odoo13-addon-product_form_sale_link',
        'odoo13-addon-product_supplierinfo_for_customer_elaboration',
        'odoo13-addon-product_supplierinfo_for_customer_sale',
        'odoo13-addon-sale_advance_payment',
        'odoo13-addon-sale_attached_product',
        'odoo13-addon-sale_automatic_workflow',
        'odoo13-addon-sale_automatic_workflow_delivery_state',
        'odoo13-addon-sale_automatic_workflow_job',
        'odoo13-addon-sale_automatic_workflow_payment',
        'odoo13-addon-sale_automatic_workflow_payment_mode',
        'odoo13-addon-sale_blanket_order',
        'odoo13-addon-sale_by_packaging',
        'odoo13-addon-sale_cancel_reason',
        'odoo13-addon-sale_commercial_partner',
        'odoo13-addon-sale_contact_type',
        'odoo13-addon-sale_coupon_most_expensive',
        'odoo13-addon-sale_coupon_most_expensive_delivery',
        'odoo13-addon-sale_coupon_multi_currency',
        'odoo13-addon-sale_coupon_multi_use',
        'odoo13-addon-sale_coupon_multi_use_currency',
        'odoo13-addon-sale_coupon_product_management',
        'odoo13-addon-sale_cutoff_time_delivery',
        'odoo13-addon-sale_delivery_state',
        'odoo13-addon-sale_discount_display_amount',
        'odoo13-addon-sale_elaboration',
        'odoo13-addon-sale_exception',
        'odoo13-addon-sale_fixed_discount',
        'odoo13-addon-sale_force_invoiced',
        'odoo13-addon-sale_force_whole_invoiceability',
        'odoo13-addon-sale_global_discount',
        'odoo13-addon-sale_invoice_no_mail',
        'odoo13-addon-sale_invoice_plan',
        'odoo13-addon-sale_invoice_policy',
        'odoo13-addon-sale_isolated_quotation',
        'odoo13-addon-sale_last_price_info',
        'odoo13-addon-sale_manual_delivery',
        'odoo13-addon-sale_order_archive',
        'odoo13-addon-sale_order_carrier_auto_assign',
        'odoo13-addon-sale_order_disable_user_autosubscribe',
        'odoo13-addon-sale_order_general_discount',
        'odoo13-addon-sale_order_incoterm_place',
        'odoo13-addon-sale_order_invoice_amount',
        'odoo13-addon-sale_order_invoicing_finished_task',
        'odoo13-addon-sale_order_line_chained_move',
        'odoo13-addon-sale_order_line_date',
        'odoo13-addon-sale_order_line_delivery_state',
        'odoo13-addon-sale_order_line_description',
        'odoo13-addon-sale_order_line_input',
        'odoo13-addon-sale_order_line_packaging_qty',
        'odoo13-addon-sale_order_line_price_history',
        'odoo13-addon-sale_order_line_sequence',
        'odoo13-addon-sale_order_lot_selection',
        'odoo13-addon-sale_order_partner_no_autofollow',
        'odoo13-addon-sale_order_partner_restrict',
        'odoo13-addon-sale_order_price_recalculation',
        'odoo13-addon-sale_order_pricelist_tracking',
        'odoo13-addon-sale_order_priority',
        'odoo13-addon-sale_order_product_assortment',
        'odoo13-addon-sale_order_product_assortment_availability_inline',
        'odoo13-addon-sale_order_product_availability_inline',
        'odoo13-addon-sale_order_product_recommendation',
        'odoo13-addon-sale_order_product_recommendation_secondary_unit',
        'odoo13-addon-sale_order_qty_change_no_recompute',
        'odoo13-addon-sale_order_revision',
        'odoo13-addon-sale_order_secondary_unit',
        'odoo13-addon-sale_order_tag',
        'odoo13-addon-sale_order_type',
        'odoo13-addon-sale_order_warn_message',
        'odoo13-addon-sale_partner_delivery_window',
        'odoo13-addon-sale_partner_incoterm',
        'odoo13-addon-sale_partner_selectable_option',
        'odoo13-addon-sale_payment_sheet',
        'odoo13-addon-sale_procurement_amendment',
        'odoo13-addon-sale_procurement_group_by_commitment_date',
        'odoo13-addon-sale_procurement_group_by_line',
        'odoo13-addon-sale_product_category_menu',
        'odoo13-addon-sale_product_multi_add',
        'odoo13-addon-sale_product_set',
        'odoo13-addon-sale_product_set_packaging_qty',
        'odoo13-addon-sale_product_set_sale_by_packaging',
        'odoo13-addon-sale_quotation_number',
        'odoo13-addon-sale_resource_booking',
        'odoo13-addon-sale_secondary_salesperson',
        'odoo13-addon-sale_shipping_info_helper',
        'odoo13-addon-sale_sourced_by_line',
        'odoo13-addon-sale_stock_cancel_restriction',
        'odoo13-addon-sale_stock_delivery_address',
        'odoo13-addon-sale_stock_last_date',
        'odoo13-addon-sale_stock_line_sequence',
        'odoo13-addon-sale_stock_picking_blocking',
        'odoo13-addon-sale_stock_picking_note',
        'odoo13-addon-sale_stock_picking_validation_blocking',
        'odoo13-addon-sale_stock_return_request',
        'odoo13-addon-sale_stock_secondary_unit',
        'odoo13-addon-sale_stock_sourcing_address',
        'odoo13-addon-sale_tier_validation',
        'odoo13-addon-sale_validity',
        'odoo13-addon-sale_validity_auto_cancel',
        'odoo13-addon-sale_wishlist',
        'odoo13-addon-sales_team_security',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 13.0',
    ]
)
