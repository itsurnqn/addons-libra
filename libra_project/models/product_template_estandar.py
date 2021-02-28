##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import fields, models

class ProductTemplateEstandar(models.Model):
    _name = 'product.template.estandar'
    _description = 'productos/servicios del estandar'

    estandar_id = fields.Many2one(comodel_name="project.task.estandar",
                                ondelete="cascade",
                                  string="Estandar",)
