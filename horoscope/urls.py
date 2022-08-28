from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.MyFloatConverter, 'my_float')
register_converter(converters.MyDateConverter, 'my_date')

urlpatterns = [
    # функция главного меню index сработает, если в роуте после /horoscope  ничего не будет:
    path('', views.index, name='horoscope-index'),
    # функция меню групп знаков зодиака index_type_list  сработает при роуте /horoscope/type:
    path('type', views.index_type_list, name='horoscope-type'),
    # dynamic URLs: <converter:parameter>
    path('<my_date:sign_zodiac>', views.get_my_date_converters),
    path('<yyyy:sign_zodiac>', views.get_yyyy_converters),
    path('<int:sign_zodiac>', views.get_info_about_sign_zodiac_by_number),
    path('<int:day>/<int:month>', views.get_info_by_date), # two numeric parameters!: /horoscope/day/month
    path('<my_float:sign_zodiac>', views.get_my_float_converters),
    path('<str:sign_zodiac>', views.get_info_about_sign_zodiac, name='horoscope-name'),
    path('type/<str:sign_zodiac>', views.index_type, name='type-name'),
]
