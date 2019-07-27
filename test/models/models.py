from odoo import models, fields, api

#class msalama(models.Model):
 #   _name = 'msalama.msalama'

  #  name = fields.Char('the name')
   # phone = fields.Integer('phone')


#class calories(models.Model):
 #   _name = 'product.template'
  #  _inherit = 'product.template'


   # calories = fields.Integer('calories')
    #service = fields.Float('service')
    #lastupdate = fields.Date('last update')
    #update = fields.Date('update')
    #size = fields.Float('size')
    #dietitem = fields.Boolean('diet item')


class nickname(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    nickname = fields.Char(str='nickname')
