from odoo import fields, models


class EmployeeEmergencyContact(models.Model):
    _name = 'recruitment_extension.emergency_contact'

    employee_id = fields.Many2one('hr.employee')
    applicant_id = fields.Many2one('hr.applicant')
    name = fields.Char(string="Name")
    phone = fields.Char(string="Phone")
    street = fields.Char(string="Street")
    street2 = fields.Char(string="Street2")
    zip = fields.Char(string='Zip')
    country_id = fields.Many2one('res.country')
    state_id = fields.Many2one('res.country.state', domain="[('country_id', '=', country_id)]")
