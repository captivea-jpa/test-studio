# coding: utf-8
# Part of CAPTIVEA. Odoo 12 EE.

from odoo import fields, models


class ResPartner(models.Model):
  """Manage 'res.partner' model. Overriding model."""
  _inherit = "res.partner"
  
  aaa_my_field = fields.Char(string="Field for testing purposes")
  
