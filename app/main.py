

from model.client import Client
from model.unico import Unico
from model.summary import Summary

from mapper.mapperObject import MapperObject

from datetime import datetime
import csv

summary =Summary()

#file_csv = '2018_4_0000004735671002_0000004735671002_DF_20180626_104122.CSV'
#file_csv = '2018_4_0000004736011000_0000004736011000_DF_20180626_102506.csv'
#file_csv = '2018_4_0000004738701004_0000004738701004_DF_20180626_101154.csv'
#file_csv = '2018_4_0000013664791004_0000013664791004_DF_20180626_112004.csv'
file_csv = '2018_4_0000097056460583_0000097056460583_DF_20180626_103505.csv'


def _cleannig_duplicates(items):
    items_cleaned = {}

    count_item = 0
    for item in items:
        count_item += 1
        items_cleaned[item['fattura']] = item

    summary.rows_worked = count_item

    return items_cleaned


def _convert_to_unico(items):
    mapperObject = MapperObject()

    count_item = 0
    total_amount = 0

    with open('data/working/pulizie_quarto_bimestre-2.csv', mode='a', newline='') as csv_file_writer:
        writer = csv.DictWriter(csv_file_writer, fieldnames=Unico.header_names(), delimiter=";")
        writer.writeheader()

        for key, val in items:
            count_item += 1
            unico = mapperObject.client_to_unico(count_item, val, file_csv)
            total_amount += float(unico.importo.replace('.','').replace(',','.'))
            writer.writerow(unico.__dict__)

    summary.number_invoices = count_item
    summary.total_amount = total_amount


if __name__ == '__main__':

    summary.execute_data = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    summary.name_file = file_csv

    items = Client.load_from_csv('data/input/quarto-bimestre/{}'.format(file_csv),header = True)

    _convert_to_unico(_cleannig_duplicates(items).items())

    print(summary.__dict__)





