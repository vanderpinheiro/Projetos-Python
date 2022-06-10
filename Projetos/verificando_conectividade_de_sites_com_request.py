import requests
print('Bem-vindo ao verificador de sites 1.0')
while True:
    urls = str(input('Digite uma url, se quiser mais de uma separe-as por vírgula:\n')).replace(' ', '').lower().split(',')
    for url in urls:
        if '.' not in url:
            print(f'URL {url} inválida')
            continue
        if 'http' not in url:
            url=(f'http://{url}')
        try:
            r = requests.get(url)
            if r.status_code == 200:
                print(f'O site {url} está online')
            else:
                print(f'O site {url} está offline')
        except:
            print(f'O  {url} está offline')
    while True:
        resp = input('Precisa verificar mais algum site? (s/n) ').strip().lower()
        if resp not in 'sn':
            print('Opção inválida. Digite somente \"s\" ou \"n\"')
        elif resp == 'n':
            break
        elif resp == 's':
            break
    if resp == 'n':
        break
print('Programa encerrado!')
