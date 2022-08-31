from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.MyFloatConverter, 'my_float')
register_converter(converters.MyDateConverter, 'my_date')

urlpatterns = [
    path('', views.index, name='horoscope-index'),
    path('type', views.index_type_list, name='horoscope-type'),
    # dynamic URLs: <converter:parameter>
    path('<my_date:date>', views.get_my_date_converters),  # date parameter input example: 05-08-2022
    path('<yyyy:four_digits>', views.get_yyyy_converters),
    path('<int:number>', views.get_info_about_sign_zodiac_by_number),
    path('<int:day>/<int:month>', views.get_info_by_date), # two numeric parameters!: /horoscope/day/month
    path('<my_float:real_number>', views.get_my_float_converters),
    path('<str:sign_zodiac>', views.get_info_about_sign_zodiac, name='horoscope-name'),
    path('type/<str:sign_type>', views.index_type, name='type-name'),
]
