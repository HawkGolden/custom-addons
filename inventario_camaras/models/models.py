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
