# -*- coding: utf-8 -*-
# from odoo import http


# class InventarioCamaras(http.Controller):
#     @http.route('/inventario_camaras/inventario_camaras', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inventario_camaras/inventario_camaras/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('inventario_camaras.listing', {
#             'root': '/inventario_camaras/inventario_camaras',
#             'objects': http.request.env['inventario_camaras.inventario_camaras'].search([]),
#         })

#     @http.route('/inventario_camaras/inventario_camaras/objects/<model("inventario_camaras.inventario_camaras"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inventario_camaras.object', {
#             'object': obj
#         })

