{
    'name': 'Inventario de Cámaras',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Gestión de cámaras de seguridad y su inventario asociado.',
    'author': 'Tu nombre',
    'website': 'http://www.tuwebsite.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',  # Habilitar el archivo de seguridad
        'views/views.xml',  # Vistas del módulo
        'views/templates.xml',  # Plantillas adicionales (opcional)
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}



