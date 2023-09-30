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
        'website',
    ],
    'data': [
        'views/res_partner_view.xml',
        'views/crm_social_media_data.xml',
        'views/website_crm_social_media.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
