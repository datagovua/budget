Бюджетні дані
=============

Існують наступні рівні бюджетних даних:

* Державний бюджет
* Обласний бюджет
* Міський бюджет

## Державний бюджет

* Про Державний бюджет України на 2014 рік
  * [Рада](http://zakon4.rada.gov.ua/laws/show/719-18)
  * [Мінфін](http://www.minfin.gov.ua/file/link/397661/file/budg.zip) (zip)
  * [Законопроект від 27.03.2014](http://w1.c1.rada.gov.ua/pls/zweb2/webproc4_1?pf3511=50433) (не опублікований)
* Виконання бюджету
  * [Виконання Державного бюджету України](http://www.treasury.gov.ua/main/uk/doccatalog/list?currDir=146477)
  * [Показники виконання Державного бюджету України](http://195.78.68.18/minfin/control/uk/publish/archive/main?cat_id=77643)

## Обласні бюджети

* Одеська область
  * 2016
    * [бюджет](http://oblrada.odessa.gov.ua/wp-content/uploads/49-VII.pdf) (створено 21 грудня 2015 року)

## Міські бюджети

* Одеса
  * 2016
    * [бюджет (проект)](http://omr.gov.ua/ru/67025/) (змінено 18 листопада 2015 року)
    * виконання
  * 2015
    * [бюджет](http://omr.gov.ua/ru/acts/council/67004/) (змінено 16 грудня 2015 року)
    * [виконання](http://omr.gov.ua/ru/news/79118/) (станом на 6 січня 2016 року)
  * 2014
    * [бюджет](http://omr.gov.ua/ru/acts/council/57231/) (змінено 4 грудня 2014 року)
    * [виконання](http://omr.gov.ua/ru/acts/council/66397/) (звіт затверджено 24 грудня 2014 року)


## Скрипти обробки файлів держбюджету

Prerequisites: Linux, Python, pip

    ./dependencies.sh # install dependencies
    . export_path.sh  # extend $PATH with ~/.local/bin
    ./download.py     # download official data and unpack
    ./convert.py      # TODO convert to csv or json

## Open Budget

Open Budget - ініціатива Sergey Gerasimov @ SoftServe (mail[at]grsmv.com).

Ідея:

* зібрати оригінальні файли бюджетів в одному місці
* обробити в ручному режимі
* надати API
* візуалізувати

Недоліки:

* ручний режим збору файлів
* ручний режим обробки файлів (https://github.com/open-budget/data/issues/55)

Реалізація:

* https://api.open-budget.org/
* https://github.com/open-budget/api

## Конвертація Open Budget у CSV стандарту OpenSpending

    ./import-from-openbudget.py > data/expenses.csv

## Обговорення ідеї

* [IT-країна](http://www.it-krayina.org.ua/openbudget/)
  * [Голосування](http://ideas.it-krayina.org.ua/topic/420190-proekt-vdkritij-byudzhet-42/)
* [Хакатон Social Boost](http://2014.socialboost.com.ua/ideas/view/2)
* [Github issues](https://github.com/Maidan-hackaton/budget/issues)


## Приклади реализації

* [Тексти (Бюджет України-2012)](http://texty.org.ua/mod/datavis/apps/budget2/index.html#/~/-----------)
* [Электронный бюджет (Россия)](http://budget.gov.ru/)
* [ГосЗатраты (Россия)](http://clearspending.ru/)
* [Budget of Canada](http://www.budget.gc.ca/2014/home-accueil-eng.html)
* [Meie Raha (Estonia)](http://meieraha.eu/)
* [Ireland](http://budget.gov.ie/Budgets/2014/2014.aspx)

