# --------------------------------------------------------------------------
# The MIT License (MIT)
#
# Copyright (c) 2014-2015 JMSwag
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
try:
    from pathlib2 import Path
except ImportError:
    from pathlib import Path

import os

from dsdev_utils.paths import ChDir, get_mac_dot_app_dir


def test_get_mac_app_dir():
        main = 'Main'
        path = os.path.join(main, 'Contents', 'MacOS', 'app')
        assert get_mac_dot_app_dir(path) == main


def test_chdir(cleandir):
    new_dir = 'temp'
    og_dir = os.getcwd()
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
    new_dir = os.path.abspath(new_dir)
    with ChDir(new_dir):
        assert os.getcwd() == new_dir
    assert og_dir == os.getcwd()


def test_chdir_pathlib(cleandir):
    new_dir = Path(os.getcwd(), 'temp')
    og_dir = os.getcwd()
    if not os.path.exists(str(new_dir)):
        os.mkdir(str(new_dir))

    with ChDir(new_dir):
        assert os.getcwd() == str(new_dir)
    assert  og_dir == os.getcwd()
