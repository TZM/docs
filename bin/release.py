#!/usr/bin/env python

# Copyright (C) 2009 David Versmisse <david.versmisse@itaapy.com>
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

# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
from sys import stderr, exit, argv
from datetime import datetime


def get_date():
    try:
        # Date
        date = Popen(['git', 'log', '--pretty=format:%at', '-n1'],
                     stderr=PIPE, stdout=PIPE)
        if date.wait() != 0:
            raise ValueError
        date = datetime.fromtimestamp(int(date.stdout.read()))
    except:
        print>>stderr, '%s: error: unable to read info' % argv[0].split(
                                                                '/')[-1]
        exit(-1)
    # Output
    return date


def get_branch():
    try:
        # Branch
        branches = Popen(['git', 'branch'], stderr=PIPE, stdout=PIPE)
        if branches.wait() != 0:
            raise ValueError
        for line in branches.stdout:
            if line.startswith('*'):
                branch = line[2:].rstrip()
                break
        else:
            raise ValueError
    except:
        print>>stderr, '%s: error: unable to read info' % argv[0].split(
                                                                '/')[-1]
        exit(-1)
    # Output
    return branch


if __name__ == '__main__':

    date = get_date()
    date = date.strftime('%Y%m%d-%H%M')
    version = '%s-%s' % (get_branch(), date)

    print version

