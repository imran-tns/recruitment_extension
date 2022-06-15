from odoo import models, fields, _, api
from odoo.exceptions import UserError


class LeaveDays(models.Model):
    _name = "recruitment_extension.leave_days"

    day = fields.Date()
    employee_id = fields.Many2one('hr.employee')

    @api.onchange('day')
    def _onchange_day_check_if_day_in_current_year(self):
        if self.day:
            if self.day.year != fields.Date.today().year:
                raise UserError(_("Select days from current year only"))
