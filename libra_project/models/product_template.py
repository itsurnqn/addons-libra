##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    estandar_id = fields.Many2one(comodel_name="project.task.estandar",
                                ondelete="cascade",
                                  string="Estandar",)        