#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Tebrama - Tempo no Brasil para Mastodon
Copyright (C) 2021 Vitor Guia

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import sys
import time
from os import environ
from sepbit.tebrama.mastodon import statuses
from sepbit.tebrama.cptec_inpe import previsao

def main():
    '''
    Entry point
    '''
    statuses(
        environ['INSTANCE'],
        environ['TOKEN'],
        data = {
            'status': previsao(sys.argv[1].upper()),
            'language': 'por',
            'visibility': 'public'
        }
    )

if __name__ == '__main__':
    main()
