import csv

from django.shortcuts import render

from .settings import INFLATION_CSV


def inflation_view(request):
    template_name = 'inflation.html'

    list_year = []
    with open(INFLATION_CSV, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for row in reader:
            row_dict = dict(row)
            year_dict = {}
            year_dict['year'] = row_dict['Год']
            year_dict['total'] = row_dict['Суммарная']
            values = []
            for key in row_dict:
                if key != 'Год' and key != 'Суммарная':
                    values.append(row_dict[key])
            year_dict['values'] = values
            list_year.append(year_dict)
    context = {'list_year': list_year}
    return render(request, template_name, context)

