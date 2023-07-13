from django.urls import path
from .views import home, polling_unit_result, lga_results, add_polling_unit_result, polling_unit_results


urlpatterns = [
    path('', home),
    path('polling_unit/<int:polling_unit_id>/', polling_unit_result, name='polling_unit_result'),
    path('lga/', lga_results, name='lga_results'),
    path('polling_unit_results/', polling_unit_results, name='polling_unit_results'),
    path('add_polling_unit_result/', add_polling_unit_result, name='add_polling_unit_result'),
]

