from random import choice, randint


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == 'a':
        return 'https://hips.hearstapps.com/hmg-prod/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg'
    elif 'hello' in lowered:
        return 'Chào con chó!'
    elif 'cảm ơn' in lowered:
        return 'Bố mày xin'
    elif 'bye' in lowered:
        return 'Cút Cút'
    elif 'random' in lowered:
        return f'You rolled: {randint(1, 6)}'
    else:
        return choice(['Nói tiếng việt đi',
                       'Nói gì chả hiểu',
                       'Không hiểu tiếng việt'])
