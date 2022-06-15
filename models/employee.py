# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    _description = "Extended Employee Model from Recruitment Extension Module"

    emergency_contact_ids = fields.One2many('recruitment_extension.emergency_contact', 'employee_id')
    education_info_ids = fields.One2many('recruitment_extension.education_info', 'employee_id')
    leave_ids = fields.One2many('recruitment_extension.leave', 'employee_id')

    @api.model
    def create(self, vals):
        if not vals['leave_day_ids']:
            raise UserError(_("Please select leave days."))
        return super().create(vals)
