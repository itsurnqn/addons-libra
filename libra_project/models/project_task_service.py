##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import fields, models

class ProjectTaskService(models.Model):
    _name = 'project.task.service'
    _description = 'Servicios'

    task_id = fields.Many2one(comodel_name="project.task",
                            ondelete="cascade",
                            string="Tarea")

    product_template_id = fields.Many2one(comodel_name="product.template",
                                        ondelete="restrict",
                                        string="servicio")

    default_code = fields.Char(related="product_template_id.default_code")


    cantidad_pedida = fields.Integer(string="Cant. pedida")

    cantidad_ejecutada = fields.Integer(string="Cant. ejecutada",default=0)
