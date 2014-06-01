Бюджет
======

Державний бюджет України / Государственный бюджет Украины


## Open Budget -> DataHub & OpenSpending

    ./import-from-openbudget.py > data/expenses.csv

## Open Budget: Ініціатива Sergey Gerasimov @ SoftServe (mail[at]grsmv.com)

* https://api.open-budget.org/
* https://github.com/open-budget/api

## Скрипт обробки офіційних даних

Prerequisites: Linux, Python, pip

    ./dependencies.sh # install dependencies
    . export_path.sh  # extend $PATH with ~/.local/bin
    ./download.py     # download official data and unpack
    ./convert.py      # TODO convert to csv or json


## Офіційні дані

* Про Державний бюджет України на 2014 рік
  * [Рада](http://zakon4.rada.gov.ua/laws/show/719-18)
  * [Мінфін](http://www.minfin.gov.ua/file/link/397661/file/budg.zip) (zip)
  * [Законопроект від 27.03.2014](http://w1.c1.rada.gov.ua/pls/zweb2/webproc4_1?pf3511=50433) (не опублікований)
* [Показники виконання Державного бюджету України](http://www.minfin.gov.ua/control/uk/publish/archive/main?cat_id=77643)


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

