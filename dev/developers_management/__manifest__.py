{
    'name': 'developers_management',
    'version': '1.0',
    'author': 'Viktor Kruts',
    'description': 'test task odoo',
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/developer.xml',
        'views/company.xml',
    ],
    'test': [
        'tests/test_developer_model.py',
    ],
}
