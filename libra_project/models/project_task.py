##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import fields, models, api

class ProjectTask(models.Model):
    _inherit = 'project.task'

    task_estandar_id = fields.Many2one(
        comodel_name='project.task.estandar',
        ondelete='restrict',
        string='Estandar',
        copy=True
    )

    subtask_ids2 = fields.One2many(comodel_name="project.task.subtask2",
                                inverse_name="task_id",
                                string="Sub tareas")

    @api.model
    def create(self,values):
        res = super(ProjectTask,self).create(values)
        # import pdb; pdb.set_trace()
        if 'task_estandar_id' in values:
            # creo las tareas para ese standar
            subtarea = self.env["project.task.subtask2"]
            # import pdb; pdb.set_trace()
            for tarea_estandar in self.task_estandar_id.estandar_task_ids:
                val = {
                    'task_id': res.id,
                    'task_estandar_id': tarea_estandar.id
                }
                subtarea.create(val)

        return res

    @api.multi
    def write(self,values):
        super(ProjectTask,self).write(values)

        if 'task_estandar_id' in values and not self.subtask_ids2:
            # creo las tareas para ese standar
            subtarea = self.env["project.task.subtask2"]
            # import pdb; pdb.set_trace()
            for tarea_estandar in self.task_estandar_id.estandar_task_ids:
                val = {
                    'task_id': self.id,
                    'task_estandar_id': tarea_estandar.id
                }
                subtarea.create(val)

        

