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
        print(str(r.status_code) + ' OK' + '\n')
    else:
        print(str(r.status_code) + ' fail')
    return r


def get_trans(r):
    soup = BeautifulSoup(r.content, 'html.parser')
    translations = soup.find_all(['div', 'a'], {'class': 'dict'})
    examples = soup.find_all('div', {'class': ['src', 'trg']})

    return translations, examples


def format_translations(translations, no_of_examples):
    translations = [t.text.strip('\n ') for t in translations]
    forbidden = '"[]'
    for index, word in enumerate(translations):
        for char in forbidden:
            if char in word:
                translations[index] = word.replace(char, '')

    for i in range(no_of_examples):
        try:
            print(translations[i])
        except:
            break


def format_examples(examples, no_of_examples):
    examples = [e.text.strip('\n ') for e in examples if e.text.strip()]

    forbidden = '"[]'
    for index, sentence in enumerate(examples):
        for char in forbidden:
            if char in sentence:
                examples[index] = sentence.replace(char, '')

    for i in range(0, no_of_examples * 2, 2):
        try:
            print(examples[i] + ':')
            print(examples[i + 1])
            print()
        except:
            break


if __name__ == '__main__':
    languages = {'fr': 'French', 'en': 'english'}
    user_translate, lanfrom, lanto = get_tran_info()
    url = generate_url(user_translate, lanfrom, lanto)
    r = request(url)
    translations, examples = get_trans(r)
    print('Context examples:' + '\n')

    no_of_examples = 500

    print(f'{languages[lanto]} Translations:')
    format_translations(translations, no_of_examples)
    print()
    print(f'{languages[lanto]} Examples:')
    format_examples(examples, no_of_examples)
