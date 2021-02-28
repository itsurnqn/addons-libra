##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import fields, models, api

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.multi
    def _timesheet_create_project(self):
        res = super(SaleOrderLine,self)._timesheet_create_project()

        # por acá SOLO en las líneas que crean proyecto.
        # la idea es que solo tenga una por sale.order.
        # lo tendré que controlar?

        # todas las lineas cuyo producto tiene un estandar asociado
        order_line_ids = self.order_id.mapped("order_line").filtered(lambda x: x.product_id.estandar_id)

        servicio_tarea = self.env["project.task.service"]
        for line in order_line_ids:
            # se busca la tarea tiene el mismo estandar que el producto.
            tarea = self.project_id.task_ids.filtered(lambda x: x.task_estandar_id.id == line.product_id.estandar_id.id and x.project_id.id == self.project_id.id)
            
            for t in tarea:
                # se crea el servicio para la tarea
                val = {
                    'task_id': t.id,
                    'product_template_id': line.product_id.product_tmpl_id.id,
                    'cantidad_pedida': line.product_uom_qty
                }
                servicio_tarea.create(val)

    # @api.multi
    # def _timesheet_create_project(self):
    #     """ Generate project for the given so line, and link it.
    #         :param project: record of project.project in which the task should be created
    #         :return task: record of the created task
    #     """
    #     self.ensure_one()
    #     account = self.order_id.analytic_account_id
    #     if not account:
    #         self.order_id._create_analytic_account(prefix=self.product_id.default_code or None)
    #         account = self.order_id.analytic_account_id

    #     # create the project or duplicate one
    #     values = {
    #         'name': '%s - %s' % (self.order_id.client_order_ref, self.order_id.name) if self.order_id.client_order_ref else self.order_id.name,
    #         'allow_timesheets': True,
    #         'analytic_account_id': account.id,
    #         'partner_id': self.order_id.partner_id.id,
    #         'sale_line_id': self.id,
    #         'sale_order_id': self.order_id.id,
    #         'active': True,
    #     }
    #     if self.product_id.project_template_id:
    #         values['name'] = "%s - %s" % (values['name'], self.product_id.project_template_id.name)
    #         project = self.product_id.project_template_id.copy(values)
    #         project.tasks.write({
    #             'sale_line_id': self.id,
    #             'partner_id': self.order_id.partner_id.id,
    #             'email_from': self.order_id.partner_id.email,
    #         })
    #         # duplicating a project doesn't set the SO on sub-tasks
    #         project.tasks.filtered(lambda task: task.parent_id != False).write({
    #             'sale_line_id': self.id,
    #         })
    #     else:
    #         project = self.env['project.project'].create(values)
    #     # link project as generated by current so line
    #     self.write({'project_id': project.id})
    #     return project