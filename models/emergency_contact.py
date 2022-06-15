from odoo import fields, models


class EmployeeEmergencyContact(models.Model):
    _name = 'recruitment_extension.emergency_contact'

    employee_id = fields.Many2one('hr.employee')
    applicant_id = fields.Many2one('hr.applicant')
    name = fields.Char(string="Name")
    address = fields.Text(string="Address")
    phone = fields.Char(string="Phone")
