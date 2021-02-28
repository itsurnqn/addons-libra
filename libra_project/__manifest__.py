# Copyright 2020 ITSur - Juan Pablo Garza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Adaptaciones de project para libra",
    "version": "12.0.1.0.0",
    "author": "ITSur",
    "website": "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list    
    "category": "Uncategorized",
    
    "license": "AGPL-3",
    "development_status": "Production/Stable",
    "maintainers": ["juanpgarza"],
    'depends': [
        'project','sale','sale_timesheet'
    ],
    "data": [
        'report/report.xml',
        'report/templates.xml',        
        'wizards/import_task_product_views.xml',
        'views/product_template_views.xml',
        'views/project_task_views.xml',
        'views/project_task_estandar_views.xml',
        'security/ir.model.access.csv',
        # 'data/libra_project_data.xml',
    ],
    'installable': True,
}