def language_direction() -> str:
    # to later be used as language from and to
    while True:
        lan = input('Type \'en\' if you want to translate from French to English'
          '\n or \'fr\' if you want to translate from English to french:')
        languages = ['fr', 'en']
        if lan not in languages:
            continue
        else:
            return lan

def to_translate() -> str:

    # To be used to fullfill any later conditions on user input

    user_translate = input('Type the word you want to translate')

    return user_translate


if __name__ == '__main__':

    lan_to = language_direction()
    translate = to_translate()

    print(f'You chose "{lan_to}" as the language to translate "{translate} to')






