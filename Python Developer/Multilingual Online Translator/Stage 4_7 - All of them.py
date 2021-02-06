import requests
from bs4 import BeautifulSoup
from typing import Dict, List

def print_dic(dic: Dict) -> str:
    """Allows you to print a dictionary in a cleaner way"""

    values = list(dic.values())
    keys = list(dic.keys())

    string = ''

    for i in range(len(keys)):

        if i == len(keys) - 1:
            string += f'{keys[i]}. {values[i]}.'
        else:
            string += f'{keys[i]}. {values[i]}\n'

    print(string)

def get_tran_info():
    print('Hello, welcome to the translator. languages supported are as follows:')
    language_dict = {'1': 'Arabic', '2': 'German', '3': 'English', '4': 'Spanish',
                     '5': 'French', '6': 'Hebrew', '7': 'Japanese', '8': 'Dutch',
                     '9': 'Polish', '10': 'Portuguese', '11': 'Romanian', '12': 'Russian',
                     '13': 'Turkish'}

    print_dic(language_dict)

    lanfrom = language_dict[input('Type the number of your language: ')]
    lanto = language_dict[input('Type the number of the language you want to translate to')]

    user_translate = input('Type the word you want to translate: ')

    # print(f'You chose {lanto} as the language to translate {user_translate} to')

    return user_translate, lanfrom, lanto


def generate_url(user_translate, lanfrom, lanto):
    url = 'https://context.reverso.net/translation/'
    url += f'{lanfrom.lower()}-{lanto.lower()}/{user_translate}'
    print(url)
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
    user_translate, lanfrom, lanto = get_tran_info()
    url = generate_url(user_translate, lanfrom, lanto)
    r = request(url)
    translations, examples = get_trans(r)

    no_of_examples = 500

    print(f'{lanto} Translations:')
    format_translations(translations, no_of_examples)
    print()
    print(f'{lanto} Examples:')
    format_examples(examples, no_of_examples)
