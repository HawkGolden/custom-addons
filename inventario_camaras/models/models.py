# -*- coding: utf-8 -*-
from odoo import models, fields

class InventarioCamara(models.Model):
    _name = 'inventario.camara'
    _description = 'Inventario de Cámaras'

    name = fields.Char(string="Nombre de la Cámara", required=True)
    serial = fields.Char(string="Número de Serie", required=True)
    referencia = fields.Char(string="Referencia")
    marca = fields.Char(string="Marca")
    descripcion = fields.Text(string="Observaciones")
    archivos = fields.Binary(string="Archivos Adjuntos")
    archivos_nombre = fields.Char(string="Nombre del Archivo")
    dvr_id = fields.Many2one('inventario.dvr', string="DVR Asociado")

class DVR(models.Model):
    _name = 'inventario.dvr'
    _description = 'DVR'

    name = fields.Char(string="Nombre del DVR", required=True)
    ubicacion = fields.Char(string="Ubicación")
    camaras_ids = fields.One2many('inventario.camara', 'dvr_id', string="Cámaras Conectadas")