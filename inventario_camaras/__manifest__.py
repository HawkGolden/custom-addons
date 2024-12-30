{
    'name': 'Inventario de Cámaras',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Gestión de cámaras de seguridad y su inventario asociado.',
    'author': 'Tu nombre',
    'website': 'http://www.tuwebsite.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'inventario_camaras/static/src/css/custom_styles.css'
        ],
    },
    'icon': '/inventario_camaras/static/description/new_icon.png',  # Ruta al archivo del icono
    'installable': True,
    'application': True,
    'auto_install': False,
}