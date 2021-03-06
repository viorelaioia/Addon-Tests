#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.mobile.details import Details


class TestDetails:

    @pytest.mark.nondestructive
    def test_that_contribute_button_is_not_present_on_the_mobile_page(self, mozwebqa):
        details_page = Details(mozwebqa, 'MemChaser')
        Assert.true(details_page.is_the_current_page)
        Assert.false(details_page.is_contribute_button_present)
