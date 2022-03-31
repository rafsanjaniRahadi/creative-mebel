# -*- coding: utf-8 -*-
# from odoo import http


# class CreativeMebel(http.Controller):
#     @http.route('/creative_mebel/creative_mebel/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/creative_mebel/creative_mebel/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('creative_mebel.listing', {
#             'root': '/creative_mebel/creative_mebel',
#             'objects': http.request.env['creative_mebel.creative_mebel'].search([]),
#         })

#     @http.route('/creative_mebel/creative_mebel/objects/<model("creative_mebel.creative_mebel"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('creative_mebel.object', {
#             'object': obj
#         })
