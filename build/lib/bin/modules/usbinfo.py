#!/usr/bin/env python
#
# Copyright (C) 2014 Joel W. Dafoe
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
from string import ascii_uppercase, ascii_lowercase


class USBdrv:
    def __init__(self):
        self.mounted_drvs = self.find_drives()
       
    def find_drives(self):
        mounts = []
        for mount in self.get_drives():
            if os.path.exists(mount):
                mounts.append(mount)
        return mounts

    @staticmethod
    def get_drives():
        if os.name == "nt":
            for letter in list(ascii_uppercase):
                if letter != 'C':
                    yield letter+':'
        if os.name == "posix":
            for device in list(ascii_lowercase):
                if device != 'a':
                    yield '/dev/sd'+device+'1'


if __name__ == '__main__':
    print(USBdrv().mounted_drvs)
