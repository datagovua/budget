#!/usr/bin/python
# encoding: UTF-8
import xlrd
import codecs
import locale
import sys

# Wrap sys.stdout into a StreamWriter to allow writing unicode.
sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout) 


def is_code(a):
  try:
    float(a)
    return True
  except ValueError:
    return False


def format_code(row):
  row[0] = int(float(row[0]))
  return row


if __name__ == '__main__':
  xls_folder = 'temp/d1/'
  files = [
    ('Додаток № 1 зміни до додатку №1.xls', {'desc': 'Доходи',
                                             'code_column': 0}),
    ('Додаток № 2 зміни до додатку №2.xls', {'desc': 'Фінансування',
                                             'code_column': 0}),
    ('Додаток № 3 зміни до додатку №3.xls', {'desc': 'Розподіл видатків',
                                             'code_column': 0}),
    ('Додаток №4 Зміни до додатку №4.xls', {'desc': 'Надання та повернення кредитів', 'code_column': 0}),
    ('Додаток №5 зміни до додатку №5.xlsx', {'desc': 'Розподіл видатків на централізовані заходи між адміністративно-територіальними одиницями',
                                             'code_column': None}),
    ('Додаток №6 зміни до додатку №6.xlsx', {'desc': 'Міжбюджетні трансферти',
                                             'code_column': 4}),
    ('Додаток №7 зміни до додатку №7.xlsx', 'Міжбюджетні трансферти'),
    ('Додаток №8 зміни до додатку №8.xls', 'Видатки на здійснення правосуддя'),
    ('Додаток №9 зміни до додатку №9.xlsx', 'Перелік кредитів (позик)'),
    ('Додаток №10 зміни до додатку №10.xls', 'Субвенції на дороги'),
    ('Додаток №11  Крим.xlsx', 'Міжбюджетні трансферти (Крим)'),
  ]
#  for filename, desc in files:
#    print filename
  if len(sys.argv) != 2:
    print "Usage: \n%s n\nn - a number from 0 to 10"
    sys.exit(-1)
  fileno = int(sys.argv[1])
  filename = xls_folder + files[fileno][0]

  rb = xlrd.open_workbook(filename,formatting_info=False)
  data = []
  sheet = rb.sheet_by_index(0)
  for rownum in range(sheet.nrows):
    row = sheet.row_values(rownum)
    data.append(row)

  # first column should be the numeric code
  data = filter(lambda row: is_code(row[0]), data)
  data = map(lambda row: format_code(row), data)

  for row in data:
    for cell in row:
      print u'"%s",' % cell,
    print
