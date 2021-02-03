##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import fields, models, api

class ProjectTaskEstandar(models.Model):
    _name = 'project.task.estandar.task'
    _description = 'Tareas del estandar'
    # _order = 'sequence asc'
    # _order = 'project_id,sequence'

    name = fields.Char(required=True,
                        string="Nombre")

    tipo = fields.Selection(
                            [('tecnico','Técnico'),
                            ('coordinacion','Coordinación'),
                            ],'Tipo')


    # completada = fields.Boolean(string="Completada?",
    #                             default=False)

    # observaciones = fields.Char(required=False,
    #                     string="Observaciones")


    estandar_id = fields.Many2one(comodel_name="project.task.estandar",
                                ondelete="cascade",
                                  string="Estandar",)

class ProjectTaskEstandar(models.Model):
    _name = 'project.task.estandar'
    _description = 'Estandar'
    _rec_name = "codigo"
    # _order = 'sequence asc'
    # _order = 'project_id,sequence'

    codigo = fields.Char(required=True,
                        string="Código")

    name = fields.Char(required=True,
                        string="Nombre")

    estandar_task_ids = fields.One2many(comodel_name="project.task.estandar.task",
                                        inverse_name="estandar_id",
                                        string="Tareas del estandar")

    def action_estandar_task_tree(self):
        action = self.env.ref('libra_project.action_estandar_task_tree').read()[0]
        action['context'] = {
            'default_estandar_id': self.id,
        }
        return action