# encoding=utf-8
import urllib2, json, codecs, locale, sys

# Wrap sys.stdout into a StreamWriter to allow writing unicode.
sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)


url = "https://api.open-budget.org/v1/expenses.json?year=2014&area_id=0"
json_string = urllib2.urlopen(url)

expenses = json.load(json_string)

print u"Year,Код,Найменування1,Найменування2,Найменування3,Найменування4,Всього"

def escape(a):
  return a.replace('"', '""')

for expense in expenses:
#  print "%s,%s,%s,%s" % (expense["year"], expense["code"], expense["code_name"], expense["total"])
#  print  int(expense["code"]) % 100 
  if int(expense["code"]) % 100 > 0:
    print "%s,%s,\"%s\",\"%s\",\"%s\",\"%s\",%s" % (expense["year"], expense["code"],
          escape(code_name), escape(code_name2), escape(expense["code_name"]), escape(expense["code_name"]), expense["total"])
  elif int(expense["code"]) % 10000 > 0:
    code_name2 =  expense["code_name"]
  else:
    code_name =  expense["code_name"]

