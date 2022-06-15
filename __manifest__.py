# -*- coding: utf-8 -*-
{
    'name': "recruitment_extension",

    'summary': """
        Recruitment Extension Module """,

    'description': """
        This module extends the hr recruitment module from odoo community """,

    'author': "Imran",
    'website': "http://www.brainstation.com",
    'category': 'Human Resource',
    'version': '0.1',
    'depends': ['hr', 'hr_recruitment', 'hr_holidays'],
    'data': [
        'security/ir.model.access.csv',
        'security/record_rule/rule_for_department_managers.xml',
        'views/hr_applicant.xml',
        'views/hr_employee.xml',
    ],
    'application': True,
    'installable': True,
}
