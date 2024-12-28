# -*- coding: utf-8 -*-
# from odoo import http


# class CalcuBasic(http.Controller):
#     @http.route('/calcu_basic/calcu_basic', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/calcu_basic/calcu_basic/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('calcu_basic.listing', {
#             'root': '/calcu_basic/calcu_basic',
#             'objects': http.request.env['calcu_basic.calcu_basic'].search([]),
#         })

#     @http.route('/calcu_basic/calcu_basic/objects/<model("calcu_basic.calcu_basic"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('calcu_basic.object', {
#             'object': obj
#         })

