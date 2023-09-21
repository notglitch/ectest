# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'CRM SOCIAL MEDIA',
    'category': 'Sales/CRM',
    'sequence': 15,
    'summary': 'Customers Social Media Managment',
    'description': "Technical Test to CE Job Application",
    'depends': [
        'base_setup',
        'base',
        'crm',
    ],
    'data': [
        'views/res_partner_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
