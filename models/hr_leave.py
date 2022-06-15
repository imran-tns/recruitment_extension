from odoo import models, fields, _, api
from odoo.exceptions import UserError


class LeaveDays(models.Model):
    _name = "recruitment_extension.leave"

    number_of_day = fields.Integer()
    leave_year = fields.Selection(selection='leave_year_selection', string="Year",
                                  default=str(fields.Date.today().year))
    leave_type_id = fields.Many2one('hr.leave.type')
    employee_id = fields.Many2one('hr.employee')

    @api.model
    def leave_year_selection(self):
        return [
            (str(fields.Date.today().year), str(fields.Date.today().year))
        ]
