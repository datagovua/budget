#!/usr/bin/python
# encoding: UTF-8
import xlrd
import codecs
import locale
import sys
import json
import yaml
import csv

# Wrap sys.stdout into a StreamWriter to allow writing unicode.
sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout) 


def is_code(a):
  try:
    float(a)
    return True
  except ValueError:
    return False


def format_code(row, desc):
  code = int(float(row[desc["code_column"]]))
  try:
    total = float(row[desc["total_column"]])
  except:
    print row,desc["total_column"]
  return code, total


def get_raw_data(filename, sheet_number):
  rb = xlrd.open_workbook(filename,formatting_info=False)
  data = []
  sheet = rb.sheet_by_index(sheet_number)
  for rownum in range(sheet.nrows):
    row = sheet.row_values(rownum)
    data.append(row)
  return data


def read(filename, sheets):
  all_data = {}
  for sheet_number, desc in enumerate(sheets[:3]):
    data = get_raw_data(filename, sheet_number)
  
    # first column should be the numeric code
    if desc['code_column'] is not None:
      data = filter(lambda row: is_code(row[desc['code_column']]), data)

      # code, total
      data = map(lambda row: format_code(row, desc), data)

      for code, total in data:
        all_data[code] = total
      json_filename = 'data/' + desc["json_filename"]
      write(json_filename, data) 
      
    else:
      print desc['desc']
  return all_data


def write(json_filename, data):
  with open(json_filename, 'w') as f:
    f.write(json.dumps({"columnTitles": ["Код классификации", "Сумма"],
                "columnValues": data
               }))
    print 'written to %s' % json_filename


def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
  csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
  for row in csv_reader:
    yield [unicode(cell, 'utf-8') for cell in row]


def read_classification(filename):
  code_to_name = {}
  with open(filename, 'r') as csvfile:
    readr = unicode_csv_reader(csvfile, delimiter=',', quotechar='"')
    for code, name in readr:
      code_to_name[code] = name
  return code_to_name


if __name__ == '__main__':

  with open("sheets.yml", 'r') as f:
    sheets_info = yaml.load(f)

  data = read('temp/f415607n146.xls', sheets_info['temp/f415607n146.xls'])
  data_add = read('temp/f421359n93.xls', sheets_info['temp/f421359n93.xls'])
  for code, total in data_add.iteritems():
    #if not code in data:
    #  print code
    data[code] = total

  code_to_name = read_classification('data/classification.csv')  
  
  for code, total in sorted(data.iteritems()):
    print code, code_to_name[code], total

