"""
Tebrama - Tempo no Brasil para Mastodon
Copyright (C) 2021-2022  Vitor Guia

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
"""

import unittest
from sepbit.tebrama.cptec_inpe import capital, previsao


class CptecInpeTest(unittest.TestCase):
    """
    Test cptec_inpe.py module
    """

    def test_capital(self):
        """
        Test capital function
        """
        result = capital('SBBH')

        self.assertTrue(result, '#BeloHorizonte - #MG')


    def test_previsao(self):
        """
        Test capital function
        """
        result = previsao('SBBH')

        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
