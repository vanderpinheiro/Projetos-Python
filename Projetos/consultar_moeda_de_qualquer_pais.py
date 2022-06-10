import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency


def conversor_moeda():
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
    print(lista)

    for index, name in enumerate(lista):
        print(f'#{index} {name["pais"]}')

    while True:
        try:
            cod = int(input('Digite um número para saber o código da moeda: \n #:'))
            print(f'Você escolhei o pais {lista[cod]["pais"]}')
            print(f'O código da moeda é {lista[cod]["código"]}')
        except (ValueError):
            print('O valor que você digitou não é um número.')
        except (IndexError):
            print('Esse número que você digitou não existe na lista')
        else:
            break

conversor_moeda()