# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http
from odoo.http import request, route


class CRMSocialMedia(http.Controller):
    _references_per_page = 20

    @route('/ectest/', type='http', auth="public", website=True)
    def customer(self):
        customers = request.env['res.partner'].search([])

        values = {'customers': customers}
        return request.render("ectest.crm_social_media_data", values)
