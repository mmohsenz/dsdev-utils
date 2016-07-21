# --------------------------------------------------------------------------
# The MIT License (MIT)
#
# Copyright (c) 2014-2016 Digital Sapphire
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
# --------------------------------------------------------------------------
from __future__ import unicode_literals
import io

from dsdev_utils.crypto import get_package_hashes


def test_package_hash():
    with io.open('hash-test.txt', 'w', encoding='utf-8') as f:
        f.write('I should find some lorem text' * 123)

    digest = ('cb44ec613a594f3b20e46b768c5ee780e0a9b66ac'
              '6d5ac1468ca4d3635c4aa9b')
    assert digest == get_package_hashes('hash-test.txt')
