##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import fields, models

class ProjectTaskSubtask(models.Model):
    _name = 'project.task.subtask2'
    _description = 'subtareas'

    task_id = fields.Many2one(comodel_name="project.task",
                            ondelete="cascade",
                            string="Tarea")

    task_estandar_id = fields.Many2one(comodel_name="project.task.estandar.task",
                                        ondelete="restrict",
                                        string="tarea")

    tipo_tarea = fields.Selection(related="task_estandar_id.tipo")

    completada = fields.Boolean(string="Completada?",
                                default=False)

    observaciones = fields.Char(required=False,
                        string="Observaciones")

    descripcion = fields.Char(related="task_estandar_id.descripcion",string="Descripción")
