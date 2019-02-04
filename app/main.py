

from model.client import Client
from model.unico import Unico
from model.summary import Summary

from mapper.mapperObject import MapperObject

from util.fileUtils import FileUtils
from util.appHelpers import AppHelpers

from datetime import datetime
import csv

summary =Summary()
fileUtils = FileUtils()
appHelpers = AppHelpers()

file_output = 'data/temp/cleaning-csv{sufix_file}.csv'.format(sufix_file = appHelpers.generate_sufix_file())

def _cleannig_duplicates(items):
    items_cleaned = {}

    count_item = 0
    for item in items:
        count_item += 1
        items_cleaned[item['fattura']] = item

    summary.rows_worked = count_item

    return items_cleaned


def _convert_to_unico(items, file_csv):
    mapperObject = MapperObject()

    count_item = 0
    total_amount = 0

    exist_file = not fileUtils.existFile(file_output)

    with open(file_output, mode='a', newline='') as csv_file_writer:
        writer = csv.DictWriter(csv_file_writer, fieldnames=Unico.header_names(), delimiter=";")

        if exist_file:
            writer.writeheader()

        for key, val in items:
            count_item += 1
            unico = mapperObject.client_to_unico(count_item, val, file_csv)
            total_amount += float(unico.importo.replace('.','').replace(',','.'))
            writer.writerow(unico.__dict__)

    summary.number_invoices = count_item
    summary.total_amount = total_amount

    fileUtils.move_file(file_output, str(file_output).replace('temp', 'processed'))


def _process_cleannig_csv(directory):

    numFiles = fileUtils.countFiles(directory)

    if numFiles > 0:
        files = fileUtils.getFiles(directory, 'csv')
        for file_csv in files:
            summary.name_file = file_csv

            path_file_origin = 'data/input/{}'.format(file_csv)
            path_file_working = 'data/working/{}'.format(file_csv)

            fileUtils.move_file(path_file_origin, path_file_working)

            items = Client.load_from_csv(path_file_working, header=True)

            _convert_to_unico(_cleannig_duplicates(items).items(), file_csv)


if __name__ == '__main__':

    summary.execute_data = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    _process_cleannig_csv('data/input/')

    print(summary.__dict__)






