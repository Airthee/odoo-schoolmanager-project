# -*- coding: utf-8 -*-
{
    'name': "schoolmanager",

    'summary': """
        Allow school managing""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Raphaël Tison",
    'website': "http://github.com/Raphael_T",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/helico/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/tdsimodel_security.xml',
        'datas/datas.xml',
        'views/schoolmanager_course_views.xml',
        'schoolmanager_menu.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
