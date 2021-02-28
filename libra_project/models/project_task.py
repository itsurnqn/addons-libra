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

    service_ids = fields.One2many(comodel_name="project.task.service",
                                inverse_name="task_id",
                                string="Servicios")

    # product_ids = fields.One2many(comodel_name="project.task.product",
    #                             inverse_name="task_id",
    #                             string="Productos")

    @api.model
    def create(self,values):
        res = super(ProjectTask,self).create(values)
        # import pdb; pdb.set_trace()
        if 'task_estandar_id' in values:
            
            #1# creo las tareas para ese standar
            subtarea = self.env["project.task.subtask2"]
            # import pdb; pdb.set_trace()
            for tarea_estandar in self.task_estandar_id.estandar_task_ids:
                val = {
                    'task_id': res.id,
                    'task_estandar_id': tarea_estandar.id
                }
                subtarea.create(val)

            #2# creo los servicios para el standar.
            # standar->tarea->proyecto(sale_order_id)->sale order->sale order line-> servicios del standar.
            #  
            servicio_tarea = self.env["project.task.service"]
            servicios = self.project_id.sale_order_id.mapped("order_line").mapped("product_id").filtered(lambda x: x.estandar_id.id == self.task_estandar_id.id)
            # import pdb; pdb.set_trace()
            for rec in servicios:
                # import pdb; pdb.set_trace()
                val_servicio = {
                    'task_id': res.id,
                    'product_template_id': rec.id,
                    'cantidad_pedida': self.project_id.sale_order_id.mapped("order_line").filtered(lambda x: x.product_id == rec.id).product_uom_qty
                }
                servicio_tarea.create(val_servicio)

        return res

    @api.multi
    def write(self,values):
        super(ProjectTask,self).write(values)
        # import pdb; pdb.set_trace()
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

        # if 'project_id' in values:
            # import pdb; pdb.set_trace()            

    # @api.onchange('project_id')
    # def project_id_change(self):
    #     import pdb; pdb.set_trace()
        

