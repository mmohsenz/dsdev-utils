# ------------------------------------------------------------------------------
# The MIT License (MIT)
#
# Copyright (c) 2014-2019 Digital Sapphire
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
# ------------------------------------------------------------------------------
import logging

from dsdev_utils.exceptions import VersionError
from dsdev_utils.helpers import EasyAccessDict, Version
import pytest

log = logging.getLogger()


class TestVerson(object):
    def test_version_short(self):
        assert Version('1.1') > Version('1.1beta1')
        assert Version('1.2.1beta1') < Version('1.2.1')
        assert Version('1.2.1alpha1') < Version('1.2.1alpha2')

    def test_version_full(self):
        assert Version('1.1') > Version('1.1b1')
        assert Version('1.2.1b1') < Version('1.2.1')
        assert Version('1.2.1a1') < Version('1.2.1a2')

    def test_version(self):
        assert Version('5.0') == Version('5.0')
        assert Version('4.5') != Version('5.1')
        with pytest.raises(VersionError):
            Version('1')
        with pytest.raises(VersionError):
            Version('1.1.1.1')


class TestEasyAccessDict(object):

    def test_easy_access(self):
        key = 'carson*da*park'
        data = {'carson': {'da': {'park': 'mills'}}}
        easy_data = EasyAccessDict(data)
        assert 'mills' == easy_data.get(key)
