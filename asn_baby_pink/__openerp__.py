{
    'name': 'ASN Baby Pink Theme',
    'version': '1.0',
    'author': 'ASN',
    'description': '''
        A custom module to change default odoo menu color
    ''',
    'category': 'Themes/ASN',
    'depends': [
        'base',
    ],
    'data': [
        'views/custom_view.xml',
    ],
    'css': ['static/src/css/styles.css'],
    'auto_install': False,
    'installable': True,
}
