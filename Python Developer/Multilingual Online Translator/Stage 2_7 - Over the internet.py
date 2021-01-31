import requests
from bs4 import BeautifulSoup


def get_tran_info():
    lanto = input('Type "en" if you want to translate from French into English,'
                  ' or "fr" if you want to translate from English into French:')
    if lanto == 'en':
        lanfrom = 'fr'
    else:
        lanfrom = 'en'

    user_translate = input('Type the word you want to translate: ')

    print(f'You chose {lanto} as the language to translate {user_translate} to')

    return user_translate, lanfrom, lanto


def generate_url(user_translate, lanfrom, lanto):
    languages = {'fr': 'french', 'en': 'english'}
    url = 'https://context.reverso.net/translation/'
    url = f'{url}{languages[lanfrom]}-{languages[lanto]}/{user_translate}'
    return url


def request(url):
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh)'}
    r = requests.get(url, headers=headers)
    if r:
        print(str(r.status_code) + ' OK')
    else:
        print(str(r.status_code) + ' fail')
    return r


def get_trans(r):
    soup = BeautifulSoup(r.content, 'html.parser')
    translations = soup.find_all(['div', 'a'], {'class': 'dict'})
    examples = soup.find_all('div', {'class': ['src', 'trg']})

    return translations, examples


if __name__ == '__main__':
    user_translate, lanfrom, lanto = get_tran_info()
    url = generate_url(user_translate, lanfrom, lanto)
    r = request(url)
    translations, examples = get_trans(r)

    print('Translations')
    print([t.text.strip('\n ') for t in translations])
    print([e.text.strip('\n ') for e in examples if e.text.strip()])
