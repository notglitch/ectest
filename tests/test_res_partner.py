import unittest
from odoo.tests.common import TransactionCase


class TestSocialMedia(TransactionCase):
    def TestResPartner(self):
        # I can not find the customer category.
        # It most to be evaluated only for costumer category
        partner = self.env['res.partner']

        test_case_1 = partner.create({'name': 'Oscar Monte',
                                      'facebook': 'www.facebook.com',
                                      'twitter': 'www.twitter.com',
                                      'linkedin': 'www.linkedin.com'
                                      })
        test_case_2 = partner.create({'name': 'Luciana Monte',
                                      'facebook': '',
                                      'twitter': 'www.twitter.com',
                                      'linkedin': 'www.linkedin.com'
                                      })
        test_case_3 = partner.create({'name': 'Rubio Monte',
                                      'facebook': '',
                                      'twitter': '',
                                      'linkedin': 'www.linkedin.com'
                                      })
        test_case_4 = partner.create({'name': 'Martha Monte',
                                      'facebook': '',
                                      'twitter': '',
                                      'linkedin': ''
                                      })
        # This test may proof that can store computed fields in extended model,
        # even when can't be used in a filter view
        self.assertEqual(test_case_1.has_social_media, True, msg='Completed Profile')
        self.assertEqual(test_case_2.has_social_media, False, msg='Incomplete Profile')
        self.assertEqual(test_case_3.has_social_media, False, msg='Incomplete Profile')
        self.assertEqual(test_case_4.has_social_media, False, msg='Empty Profile')
