import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency
import csv
import gspread


#pegando o site no IBAN e lendo
site_iban = 'https://www.iban.com/currency-codes'
get_iban = requests.get(site_iban)

#extraindo o HTML do site IBAN
html_iban = get_iban.text

#organizando o HTML
soup = BeautifulSoup(html_iban, 'html.parser')

tabela = soup.find('tbody')
paises = tabela.find_all('tr')


lista =[]
for linha in paises:
    items = linha.find_all('td')
    nome = items[0].text
    moeda = items[2].text
    if moeda == '':
        continue
    else:
        pais = {
            'pais': nome,
            'código': moeda
        }
    lista.append(pais)

for index, name in enumerate(lista):
    print(f'#{index} {name["pais"]}')

while True:
    try:
        cod = int(input('Digite o número do pais de origem da moeda: \n #:'))
        print(f'Você escolheu o pais {lista[cod]["pais"]} de meoda {lista[cod]["código"]}')
    except (ValueError):
        print('O valor que você digitou não é um número.')
    except (IndexError):
        print('Esse número que você digitou não existe na lista')
    else:
        break

while True:
    try:
        cod2 = int(input('Digite o número do pais que quer fazer a conversão: \n #:'))
        print(f'Você escolheu o pais {lista[cod2]["pais"]} de meoda {lista[cod2]["código"]}')
    except (ValueError):
        print('O valor que você digitou não é um número.')
    except (IndexError):
        print('Esse número que você digitou não existe na lista')
    else:
        break

while True:
    try:
        quantia = float(input('Digite a quantia que quer converter: '))
    except (ValueError):
        print('O valor que você digitou não é um número.')
    else:
        break

#transformando os dados no site:
wise_site = f'https://wise.com/gb/currency-converter/{lista[cod]["código"]}-to-{lista[cod2]["código"]}-rate?amount={quantia}'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
#pegando o site:
get_sitewise = requests.get(wise_site, headers=headers)
#extraindo o html do site:
html_wise = get_sitewise.text
#organizando o html do site:
soup2 = BeautifulSoup(html_wise,'html.parser')
#pegar o valor que preciso do site:
result = float(soup2.find('span', class_='text-success').get_text())
convertido = quantia * result
resultado_transfomacao = str(lista[cod2]["código"])
print(format_currency(convertido,f'{resultado_transfomacao}', locale ='br'))
