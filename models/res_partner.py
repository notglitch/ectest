# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import base64
from odoo import api, fields, models, modules


class Partner(models.Model):

    _inherit = 'res.partner'

    @api.model
    def _compute_image(self):
        for customer in self:
            if customer.facebook and customer.linkedin and customer.twitter:
                image_path = modules.get_module_resource('ectest', 'static/src/img', 'icon3.png')
                customer.image = base64.b64encode(open(image_path, 'rb').read())
            else:
                customer.image = False

    facebook_followers = fields.Float(string="facebook followers", store=True)
    facebook_followers_sig = fields.Selection(
        [("few", "<k"), ("k", "K"), ("m", "M"), ("mm", "MM")], default="few",
        string="measure", store=True)
    facebook = fields.Char()
    linkedin_followers = fields.Float(string="linkedin followers", store=True)
    linkedin_followers_sig = fields.Selection(
        [("few", "<k"), ("k", "K"), ("m", "M"), ("mm", "MM")], default="few",
        string="measure", store=True)
    linkedin = fields.Char()
    twitter = fields.Char()
    twitter_followers = fields.Float('twitter followers')
    twitter_followers_sig = fields.Selection(
        [("few", "<k"), ("k", "K"), ("m", "M"), ("mm", "MM")], default="few")
    website_brief_info = fields.Text(string="Website Brief info")
    image = fields.Image(string="Profile Completed", compute='_compute_image')


