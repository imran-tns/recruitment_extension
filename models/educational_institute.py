from odoo import fields, models


class EducationalInstitute(models.Model):
    _name = 'recruitment_extension.educational_institute'

    name = fields.Char(required=True)
    address = fields.Char()
