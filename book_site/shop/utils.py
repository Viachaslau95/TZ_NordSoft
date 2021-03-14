import csv

from django.http import HttpResponse

from shop.models import Book


def export_to_csv(queryset, fields, titles, file_name):
    response = HttpResponse(content_type='text/csv')
    # force download
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(file_name)
    # the csv writer
    writer = csv.writer(response)

    writer.writerow(titles)

    for book in Book.objects.values_list('name', 'author__name'):
        writer.writerow(book)
    return response
