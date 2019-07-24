# -*- coding: utf-8 -*-
from odoo import http

# class Msalama(http.Controller):
#     @http.route('/msalama/msalama/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/msalama/msalama/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('msalama.listing', {
#             'root': '/msalama/msalama',
#             'objects': http.request.env['msalama.msalama'].search([]),
#         })

#     @http.route('/msalama/msalama/objects/<model("msalama.msalama"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('msalama.object', {
#             'object': obj
#         })