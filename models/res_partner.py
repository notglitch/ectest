# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Partner(models.Model):

    _inherit = 'res.partner'

    def _has_social_network(self):
        for customer in self:
            if customer.facebook and customer.linkedin and customer.twitter:
                customer.has_social_media = True
            else:
                customer.has_social_media = False

    facebook = fields.Char(string="Facebook", store=True)
    linkedin = fields.Char(string="Linkedin", store=True)
    twitter = fields.Char(string="Twitter", store=True)
    has_social_media = fields.Boolean("Is profile completed?",
                                      compute='_has_social_network')


