from odoo import api, fields, models
from odoo.odoo.exceptions import ValidationError


class Developer(models.Model):
    _name = 'developer'

    name = fields.Char(string='name', required=True)
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
    company_id = fields.Many2one('company', string='Company')
    position = fields.Char(string='Position')

    @api.depends('name', 'type')
    def compute_global_identification(self):
        for developer in self:
            developer.global_identification = f'{developer.name} - {developer.type}'

    @api.depends('type')
    def onchange_type(self):
        for developer in self:
            if developer.type == 'out-staff':
                developer.phone = False

    @api.constrains('name')
    def _check_name(self):
        for developer in self:
            if developer.name and not developer.name.istitle():
                raise ValidationError("Each word in the name should start with a capital letter.")

    @api.constrains('phone')
    def _check_phone(self):
        for developer in self:
            if developer.phone and '+' not in developer.phone:
                raise ValidationError("Phone number should contain a '+' symbol.")

    @api.constrains('email')
    def _check_email(self):
        for developer in self:
            if developer.email and '@' not in developer.email:
                raise ValidationError("Email address should contain an '@' symbol.")
