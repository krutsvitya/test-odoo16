from odoo import api, fields, models


class Developer(models.Model):
    _name = 'developer'

    name = fields.Char(string='name', required=True, unique=True)
    type = fields.Selection([('front-end', 'Front-end'),
                             ('backend', 'Backend'),
                             ('fullstack', 'Fullstack'),
                             ('out-stuff', 'out-stuff')],
                            string='type')
    global_identification = fields.Char(compute='compute_global_identification')
    phone = fields.Char(string='phone')
    email = fields.Char(string='email')
    address = fields.Text(string='address')
    birthday = fields.Date(string='date')

    @api.depends('name', 'type')
    def compute_global_identification(self):
        for developer in self:
            developer.global_identification = f'{developer.name} - {developer.type}'

    @api.depends('type')
    def onchange_type(self):
        for developer in self:
            if developer.type == 'out-staff':
                developer.phone = False
