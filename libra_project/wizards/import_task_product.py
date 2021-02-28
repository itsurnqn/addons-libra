from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning
import base64
from io import BytesIO
from xlrd import open_workbook

import logging
_logger = logging.getLogger(__name__)

class ImportTaskProduct(models.TransientModel):
    _name = 'import.task.product.wizard'
    _description = 'Importación de productos'

    project_id = fields.Many2one(comodel_name="project.project",
                                string="Projecto")

    excel_file_for_import = fields.Binary("Archivo")

    @api.model
    def default_get(self, field_names):
        defaults = super(
            ImportTaskProduct, self).default_get(field_names)
        defaults['project_id'] = self.env.context['active_id']
        return defaults
    
    def do_import(self):
        try:
            inputx = BytesIO()
            inputx.write(base64.decodestring(self.excel_file_for_import))
            book = open_workbook(file_contents=inputx.getvalue())
        except TypeError as e:
            raise UserError(u'ERROR: {}'.format(e))

        sheet = book.sheets()[0]

        # producto_tarea = self.env["project.task.product"]
        material_tarea = self.env["project.task.material"]
        for i in list(range(sheet.nrows)):
            # columna 1 = xmlID del estandar
            estandar_id = self.env.ref(sheet.cell(i, 0).value)
            # columna 2 = código de producto
            default_code = int(sheet.cell(i, 1).value)
            # columna 3 = descripcion
            # columna 4 = cantidad
            cantidad = sheet.cell(i, 3).value

            tarea = self.project_id.task_ids.filtered(lambda x: x.task_estandar_id.id == estandar_id.id)

            producto = self.env["product.template"].search([("default_code","=", default_code)])
            # import pdb; pdb.set_trace()

            # val = {
            #     'task_id': tarea.id,
            #     'product_template_id': producto.id,
            #     'cantidad_pedida': cantidad
            # }

            # producto_tarea.create(val)

            val = {
                'task_id': tarea.id,
                'product_id': producto.product_variant_id.id,
                'quantity': cantidad
            }

            material_tarea.create(val)
            # _logger.info("%s" % default_code)