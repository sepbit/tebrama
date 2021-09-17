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

import xml.etree.ElementTree as ET
from urllib.request import Request, urlopen

def capital(codigo):
    '''
    Capitais das estações
    See http://servicos.cptec.inpe.br/XML/#res-estacoes-meteorologicas
    '''
    if codigo == 'SBBH':
        return '#BeloHorizonte - #MG'

    if codigo == 'SBBE':
        return '#Belem - #PA'

    if codigo == 'SBCT':
        return '#Curitiba - #PR'

    if codigo == 'SBFZ':
        return '#Fortaleza - #CE'

    if codigo == 'SBPA':
        return '#PortoAlegre - #RS'

    if codigo == 'SBRF':
        return '#Recife - #PE'

    if codigo == 'SBRJ':
        return '#RiodeJaneiro - #RJ'

    if codigo == 'SBSP':
        return '#SaoPaulo - #SP'

    if codigo == 'SBSV':
        return '#Salvador - #BA'

    return False

def previsao(codigo):
    '''
    Previsão tempo CPTEC/INPE
    See http://servicos.cptec.inpe.br/XML/#req-estacoes-meteorologicas
    '''
    request = Request(
        'http://servicos.cptec.inpe.br/XML/estacao/' + codigo+ '/condicoesAtuais.xml',
        headers={
            'User-Agent': 'Mozilla/5.0'
        }
    )
    with urlopen(request) as response:
        response = response.read()

    root = ET.fromstring(response.decode())
    message = 'Previsão do tempo ' + capital( codigo )
    message += '\nAtualização: ' + root.find('atualizacao').text
    message += '\nTempo: ' + root.find('tempo_desc').text
    message += '\nTemperatura: ' + root.find('temperatura').text + '°C'
    message += '\nVento: ' + root.find('vento_int').text + 'km/h'
    message += '\nUmidade: ' + root.find('umidade').text + '%'
    message += '\n\n#bot #tempo #Brasil'

    return message
