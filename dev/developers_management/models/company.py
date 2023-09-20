from odoo import api, fields, models


class Company(models.Model):
    _name = 'company'

    name = fields.Char(string='name', required=True)
    address = fields.Text(string='address')
    developers = fields.One2many('developer', 'company_id', string='Developers')

