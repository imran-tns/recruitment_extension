from odoo import fields, models


class EmployeeEducationInfo(models.Model):
    _name = 'recruitment_extension.education_info'

    applicant_id = fields.Many2one('hr.applicant')
    employee_id = fields.Many2one('hr.employee')
    institute_id = fields.Many2one('recruitment_extension.educational_institute', string="Institute")
    degree_id = fields.Many2one('hr.recruitment.degree', string="Degree")
    passing_year = fields.Char(string="Passing Year")
