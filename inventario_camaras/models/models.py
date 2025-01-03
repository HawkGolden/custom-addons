# -*- coding: utf-8 -*-
from odoo import models, fields


class InventarioCamara(models.Model):
    _name = 'inventario.camara'
    _description = 'Inventario de Cámaras'

    name = fields.Char(string="Nombre de la Cámara", required=True)
    serial = fields.Char(string="Número de Serie")
    referencia = fields.Char(string="Referencia")
    marca = fields.Char(string="Marca")
    descripcion = fields.Text(string="Observaciones")
    archivos = fields.Binary(string="Archivos Adjuntos")
    archivos_nombre = fields.Char(string="Nombre del Archivo")
    dvr_id = fields.Many2one('inventario.dvr', string="DVR Asociado")

    # Nuevo campo de selección para el estado de la cámara
    estado = fields.Selection([
        ('averiada', 'Averiada'),
        ('activa', 'Activa'),
        ('inactiva', 'Inactiva'),
        ('desactivada', 'Desactivada'),
        ('en_prueba', 'En Prueba')
    ], string="Estado de la Cámara", default='activa')
    # Nuevo campo para la fecha de instalación
    fecha_instalacion = fields.Date(string="Fecha de Instalación")

    # --- Nueva Sección: Tecnología de Cámaras ---
    tipo_tecnologia = fields.Selection([
        ('analogica', 'Analógica'),
        ('ip', 'IP'),
        ('hibrida', 'Híbrida'),
        ('digital', 'Digital'),
        ('otra', 'Otra'),
    ], string="Tipo de Tecnología")

    tipo_lente = fields.Selection([
        ('2mp', '2MP'),
        ('fijo', 'Lente Fijo'),
        ('varifocal', 'Lente Varifocal'),
        ('motores', 'Lente Motorizado'),
    ], string="Tipo de Lente")

    ia_integrada = fields.Boolean(string="Cuenta con IA")

    tecnologia_color = fields.Selection([
        ('estandar', 'Estándar'),
        ('starlight', 'Starlight'),
        ('full_color', 'Full Color'),
    ], string="Tecnología de Color")

    tioc = fields.Boolean(string="TIOC")

    almacenamiento = fields.Selection([
        ('sin_almacenamiento', 'No tiene'),
        ('sd_32', 'MicroSD hasta 32GB'),
        ('sd_64', 'MicroSD hasta 64GB'),
        ('sd_128', 'MicroSD hasta 128GB'),
        ('sd_256', 'MicroSD hasta 256GB'),
    ], string="Almacenamiento Interno")

    resolucion = fields.Selection([
        ('720p', '720p (HD)'),
        ('1080p', '1080p (Full HD)'),
        ('2mp', '2MP'),
        ('4mp', '4MP'),
        ('5mp', '5MP'),
        ('8mp', '8MP (4K)'),
    ], string="Resolución")

    rango_vision_nocturna = fields.Selection([
        ('10m', 'Hasta 10m'),
        ('20m', 'Hasta 20m'),
        ('30m', 'Hasta 30m'),
        ('50m', 'Hasta 50m'),
        ('mas_50m', 'Más de 50m'),
    ], string="Rango de Visión Nocturna")

    observaciones_tecnicas = fields.Text(string="Observaciones Técnicas")

    # Nueva sección de Compras
    fecha_compra = fields.Date(string="Fecha de Compra")
    precio_compra = fields.Monetary(string="Precio de Compra", currency_field='currency_id')
    proveedor_id = fields.Many2one('res.partner', string="Proveedor")  # Asumiendo que "res.partner" es el modelo de proveedores
    factura_compra = fields.Binary(string="Factura de Compra")
    currency_id = fields.Many2one('res.currency', string="Moneda", default=lambda self: self.env.company.currency_id)


class DVR(models.Model):
    _name = 'inventario.dvr'
    _description = 'DVR'

    name = fields.Char(string="Nombre del DVR", required=True)
    ubicacion = fields.Char(string="Ubicación")
    referencia = fields.Char(string="Referencia")  # Campo agregado
    marca = fields.Char(string="Marca")  # Campo agregado
    camaras_ids = fields.One2many('inventario.camara', 'dvr_id', string="Cámaras Conectadas")
