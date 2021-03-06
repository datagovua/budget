Бюджетні дані
=============

Цей проект ставить за мету збір бюджетних даних, машинну їх обробку та приведення до стандартного виду.

* [Джерела даних](source-data/README.md)
* [Стандартизація даних](standardization/README.md)

## Скрипти обробки файлів держбюджету

Prerequisites: Linux, Python, pip

    ./dependencies.sh # install dependencies
    . export_path.sh  # extend $PATH with ~/.local/bin
    ./download.py     # download official data and unpack
    ./convert.py      # TODO convert to csv or json

## Обговорення ідеї

Є питання? Пишіть: [Github issues](https://github.com/Maidan-hackaton/budget/issues)

## Приклади реализації

* [Тексти (Бюджет України-2012)](http://texty.org.ua/mod/datavis/apps/budget2/index.html#/~/-----------)
* [Электронный бюджет (Россия)](http://budget.gov.ru/)
* [ГосЗатраты (Россия)](http://clearspending.ru/)
* [Budget of Canada](http://www.budget.gc.ca/2014/home-accueil-eng.html)
* [Meie Raha (Estonia)](http://meieraha.eu/)
* [Ireland](http://budget.gov.ie/Budgets/2014/2014.aspx)

