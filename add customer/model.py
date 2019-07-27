from odoo import models, fields, api



class test(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'


    test = fields.Char('nickname')  # type: Char






