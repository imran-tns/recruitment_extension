from odoo import models, fields, _
from odoo.exceptions import UserError


class Applicant(models.Model):
    _inherit = "hr.applicant"

    emergency_contact_ids = fields.One2many('recruitment_extension.emergency_contact', 'applicant_id')
    education_info_ids = fields.One2many('recruitment_extension.education_info', 'applicant_id')

    def create_employee_from_applicant(self):
        """ Extended Create Employee Function """
        self.validate_required_information()
        dict_act_window = super().create_employee_from_applicant()
        employee_data = dict_act_window['context']
        employee_data['default_education_info_ids'] = self.education_info_ids.ids
        employee_data['default_emergency_contact_ids'] = self.emergency_contact_ids.ids
        employee_data['default_parent_id'] = self.department_id.manager_id.id
        return dict_act_window

    def validate_required_information(self):
        if not self.education_info_ids:
            raise UserError(_("Please add at least on education information."))

        if not self.emergency_contact_ids:
            raise UserError(_("Please add at least on emergency contact information."))
