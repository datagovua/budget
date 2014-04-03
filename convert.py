#!/usr/bin/python
# encoding: UTF-8
import xlrd
import codecs
import locale
import sys
import json

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
  total = float(row[desc["total_column"]])
  return code, total


def get_raw_data(filename):
  rb = xlrd.open_workbook(filename,formatting_info=False)
  data = []
  sheet = rb.sheet_by_index(0)
  for rownum in range(sheet.nrows):
    row = sheet.row_values(rownum)
    data.append(row)
  return data


if __name__ == '__main__':
  xls_folder = 'temp/d1/'
  files = [
    ('Додаток № 1 зміни до додатку №1.xls', {'desc': u'Доходи',
                                             'code_column': 0}),
    ('Додаток № 2 зміни до додатку №2.xls', {'desc': u'Фінансування',
                                             'code_column': 0, 'total_column': 2, 'common_fond': 3, 'special_fond': 4, 'json_filename': 'financing.json'}),
    ('Додаток № 3 зміни до додатку №3.xls', {'desc': u'Розподіл видатків',
                                             'code_column': 0}),
    ('Додаток №4 Зміни до додатку №4.xls', {'desc': u'Надання та повернення кредитів', 'code_column': 0}),
    (u'Додаток №5 зміни до додатку №5.xlsx', {'desc': u'Розподіл видатків на централізовані заходи між адміністративно-територіальними одиницями',
                                             'code_column': None}),
    ('Додаток №6 зміни до додатку №6.xlsx', {'desc': u'Міжбюджетні трансферти',
                                             'code_column': 4}),
    ('Додаток №7 зміни до додатку №7.xlsx', {'desc':u'Міжбюджетні трансферти',
                                             'code_column': 0}),
    ('Додаток №8 зміни до додатку №8.xls', {'desc': u'Видатки на здійснення правосуддя',
                                            'code_column': 0}),
    ('Додаток №9 зміни до додатку №9.xlsx', {'desc': u'Перелік кредитів (позик)',
                                             'code_column': 3}),
    ('Додаток №10 зміни до додатку №10.xls', {'desc': u'Субвенції на дороги',
                                              'code_column': 0}),
    ('Додаток №11  Крим.xlsx', {'desc': u'Міжбюджетні трансферти (Крим)',
                                'code_column': 3}),
  ]
  for filename, desc in [files[1]]:
#    print filename
#  if len(sys.argv) != 2:
#    print "Usage: \n%s n\nn - a number from 0 to 10"
#    sys.exit(-1)
#  fileno = int(sys.argv[1])
    filename = xls_folder + filename
  
    data = get_raw_data(filename)
  
    # first column should be the numeric code
    if desc['code_column'] is not None:
      data = filter(lambda row: is_code(row[desc['code_column']]), data)

      # code, total
      data = map(lambda row: format_code(row, desc), data)
 
      json_filename = desc["json_filename"]
      with open(json_filename, 'w') as f:
        f.write(json.dumps({"columnTitles": ["Код классификации", "Сумма"],
                    "columnValues": data
                   }))
        print 'written to %s' % json_filename 
      
      # csv
      #for code, total in data:
      #    print u'"%s",' % cell,
      #  print
    else:
      print desc['desc']
