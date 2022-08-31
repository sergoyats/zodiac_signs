from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

zodiac_dict = {
    'aries': 'Aries is the first sign of the zodiac, Mars (from March 21 to April 20).',
    'taurus': 'Taurus is the second sign of the zodiac, Venus (from April 21 to May 21).',
    'gemini': 'Gemini is the third sign of the zodiac, Mercury (from May 22 to June 21).',
    'cancer': 'Cancer is the fourth sign of the zodiac, the Moon (from June 22 to July 22).',
    'leo': 'Leo is the fifth sign of the zodiac, the Sun (from July 23 to August 21).',
    'virgo': 'Virgo is the sixth sign of the zodiac, Mercury (from August 22 to September 23).',
    'libra': 'Libra is the seventh sign of the zodiac, Venus (from September 24 to October 23).',
    'scorpio': 'Scorpio is the eighth sign of the zodiac, Mars (from October 24 to November 22).',
    'sagittarius': 'Sagittarius is the ninth sign of the zodiac, Jupiter (from November 23 to December 22).',
    'capricorn': 'Capricorn is the tenth sign of the zodiac, Saturn (from December 23 to January 20).',
    'aquarius': 'Aquarius is the eleventh sign of the zodiac, Uranus and Saturn (from January 21 to February 19).',
    'pisces': 'Pisces is the twelfth sign of the zodiac, Jupiter (from February 20 to March 20).'
}

zodiacs = list(zodiac_dict)

sign_types = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces'],
}


def index(request):  # the main menu (all zodiac signs)
    context = {
        'zodiacs': zodiacs,
        'zodiac_dict': zodiac_dict
    }
    return render(request, 'horoscope/index.html', context=context)


'''
def index(request):
    li_elements = ''
    for sign in zodiacs:
        redirect_path = reverse('horoscope-name', args=[sign])
        li_elements += f'<li> <a href="{redirect_path}"> {sign.title()} </a> </li>'
    response = f'<ol>{li_elements}</ol>'
    # ol ─ ordered list
    return HttpResponse(response)
'''


def index_type_list(request):  # the elements menu
    kinds = list(sign_types)
    context = {
        'kinds': kinds,
    }
    return render(request, 'horoscope/index.html', context=context)


'''
def index_type_list(request):
    kinds = list(sign_types)
    li_components = ''
    for kind in kinds:
        redirect_path = reverse('horoscope-name', args=[kind])
        li_components += f'<li><a href="{redirect_path}"> {kind.title()} </a></li>'
    response = f'<ol>{li_components}</ol>'
    # ul ─ unordered list
    return HttpResponse(response)
'''


def index_type(request, sign_type: str):  # the menu of zodiac signs of a certain element
    roster = sign_types.get(sign_type)
    context = {
        'roster': roster,
    }
    return render(request, 'horoscope/index.html', context=context)


'''
def index_type(request, sign_type):
    roster = sign_types.get(sign_type)
    if roster:
        li_components = ''
        for kind in roster:
            redirect_path = reverse('horoscope-name', args=[kind])
            li_components += f'<li> <a href="{redirect_path}"> {kind.title()} </a> </li>'
        response = f'<ul>{li_components}</ul>'
        return HttpResponse(response)
'''


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    data = {
        'description': description,
        'sign': sign_zodiac,
        'zodiac_dict': zodiac_dict,
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


'''
def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    if description:
        return HttpResponse(f'<h2>{description}</h2>')
    elif sign_zodiac == 'fire' or sign_zodiac == 'earth' or sign_zodiac == 'air' or sign_zodiac == 'water':
        redirect_url = reverse('type-name', args=[sign_zodiac])
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f'{sign_zodiac} is an unknown zodiac sign!')
'''


def get_info_about_sign_zodiac_by_number(request, number: int):
    if number not in range(1, 13):
        return HttpResponseNotFound(f'{number} is the number of a non-existent zodiac sign!')
    name_zodiac = zodiacs[number - 1]
    redirect_url = reverse('horoscope-name', args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)


def get_yyyy_converters(request, four_digits):
    return HttpResponse(f'You have entered a four digit number {four_digits}')


def get_my_float_converters(request, real_number):
    return HttpResponse(f'You have entered a real number {real_number}')


def get_my_date_converters(request, date):
    return HttpResponse(f'You have entered the date {date}')


def get_info_by_date(request, day, month):
    sign_from = {(21, 1): 'aquarius', (20, 2): 'pisces', (21, 3): 'aries',
                 (21, 4): 'taurus', (22, 5): 'gemini', (22, 6): 'cancer',
                 (23, 7): 'leo', (21, 8): 'virgo', (24, 9): 'libra',
                 (24, 10): 'scorpio', (23, 11): 'sagittarius', (23, 12): 'capricorn'}
    sign_list = list(sign_from)
    if month not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
        return HttpResponse('The MONTH is specified incorrectly !!!')
    if (month in (1, 3, 5, 7, 8, 10, 12) and day > 31) or \
            (month in (4, 6, 9, 11) and day > 30) or (month == 2 and day > 29):
        return HttpResponse('The DAY of the month is specified incorrectly !!!')

    for i, elem in enumerate(sign_list):
        if month == elem[1]:
            if day >= elem[0]:
                sign = sign_from.get(elem)
            elif day < elem[0]:
                sign = sign_from.get(sign_list[i - 1])
    return HttpResponse(f'<h3>The {day}th day of the {month}th month falls on</h3>\n<h2>{zodiac_dict.get(sign)}</h2>')
