from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': 'Лев - пятый знак зодиака, Солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, Юпитер (с 20 февраля по 20 марта).'
}

zodiacs = list(zodiac_dict)

sign_types = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces'],
}


def index(request):  # главное меню (все знаки зодиака в виде ссылок)
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


def index_type_list(request):  # меню стихий знаков зодиака в виде ссылок
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


def index_type(request, sign_zodiac: str):  # меню знаков зодиака определённой стихии
    roster = sign_types.get(sign_zodiac)
    context = {
        'roster': roster,
    }
    return render(request, 'horoscope/index.html', context=context)


'''
def index_type(request, sign_zodiac):
    roster = sign_types.get(sign_zodiac)
    if roster:  # если у малого словаря есть такой ключ ─ тригон знаков зодиака, то вернуть его значение
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
    return render(request, 'horoscope/info_zodiac.html', context=data)  # данные context отправятся в html-шаблон


'''
def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    if description:  # если у большого словаря есть такой ключ ─ знак зодиака, то вернуть его значение
        return HttpResponse(f'<h2>{description}</h2>')
    elif sign_zodiac == 'fire' or sign_zodiac == 'earth' or sign_zodiac == 'air' or sign_zodiac == 'water':
        redirect_url = reverse('type-name', args=[sign_zodiac])
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f'{sign_zodiac} ─ неизвестный знак зодиака!')
'''


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'{sign_zodiac} ─ номер несуществующего знака зодиака!')
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)


def get_yyyy_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали число из четырёх цифр {sign_zodiac}')


def get_my_float_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали вещественное число {sign_zodiac}')


def get_my_date_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали дату {sign_zodiac}')


def get_info_by_date(request, day, month):
    sign_from = {(21, 1): 'aquarius', (20, 2): 'pisces', (21, 3): 'aries',
                (21, 4): 'taurus', (22, 5): 'gemini', (22, 6): 'cancer',
                (23, 7): 'leo', (21, 8): 'virgo', (24, 9): 'libra',
                (24, 10): 'scorpio', (23, 11): 'sagittarius', (23, 12): 'capricorn'}
    sign_list = list(sign_from)
    if month not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
        return HttpResponse('Неверно указан МЕСЯЦ !!!')
    if (month in (1, 3, 5, 7, 8, 10, 12) and day > 31) or \
    (month in (4, 6, 9, 11) and day > 30) or (month == 2 and day > 29):
        return HttpResponse('Неверно указан ДЕНЬ месяца !!!')

    for i, elem in enumerate(sign_list):
        if month == elem[1]:
            if day >= elem[0]:
                sign = sign_from.get(elem)
            elif day < elem[0]:
                sign = sign_from.get(sign_list[i-1])
    return HttpResponse(f'<h3>{day}-й день {month}-го месяца приходится на</h3>\n<h2>{zodiac_dict.get(sign)}</h2>')
