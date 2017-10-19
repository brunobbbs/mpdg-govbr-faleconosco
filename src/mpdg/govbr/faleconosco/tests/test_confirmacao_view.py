# -*- coding: utf-8 -*-
from mpdg.govbr.faleconosco.testing import MPDG_GOVBR_FALECONOSCO_INTEGRATION_TESTING

import unittest


class ConfirmacaoViewTest(unittest.TestCase):

    layer = MPDG_GOVBR_FALECONOSCO_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_view_faleconosco_form(self):
        view = self.portal.restrictedTraverse('@@confirmacao')
        self.assertTrue(view)
