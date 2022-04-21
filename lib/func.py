# TODO: финал
def check_language():
    languages = ('Русский', 'English')

    print("Set language (Copy and Paste):")

    for language in languages:
        print(f'\t- {language}')

    value = input('User: ')

    return 'ru' if value.lower() == 'русский' else 'en'
