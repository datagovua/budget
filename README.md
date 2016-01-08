Бюджетні дані
=============

Існують наступні рівні бюджетних даних:

* Державний бюджет
* Обласний бюджет
* Міський бюджет

Бюджет приймається раз на рік та коригується на протязі року.

Також протягом року подаються оперативні дані про виконання бюджету - фактичні транзакції.

У кінці року чи на початку наступного публікується остаточний звіт про виконання бюджету.

## Джерела даних

Офіційні джерела даних:

* [Бюджетний кодекс](http://zakon5.rada.gov.ua/laws/show/2456-17)
* Закони про держбюджет (Верховна Рада)
* Проекти держбюджету (Мінфін)
* Рішення про бюджет (обласні та міські ради)
* Звіти про виконання бюджету

### Державний бюджет

* 2016
  * [бюджет](http://zakon3.rada.gov.ua/laws/show/928-19/page2) (створено 24 грудня 2015)
* 2015
  * [бюджет](http://zakon3.rada.gov.ua/laws/show/80-19) (змінено 24 грудня 2015)
  * [виконання](http://www.treasury.gov.ua/main/uk/doccatalog/list?currDir=264515) (оперативна інформація)
* 2014
  * [бюджет](http://zakon4.rada.gov.ua/laws/show/719-18) (змінено 25 грудня 2014)
  * [виконання](http://www.treasury.gov.ua/main/uk/doccatalog/list?currDir=257806) (звіт станом на 01 квітня 2015)

### Обласні бюджети

* Одеська область
  * 2016
    * [бюджет](http://oblrada.odessa.gov.ua/wp-content/uploads/49-VII.pdf) (створено 21 грудня 2015)

### Міські бюджети

* Одеса
  * 2016
    * [бюджет (проект)](http://omr.gov.ua/ru/67025/) (змінено 18 листопада 2015)
    * виконання
  * 2015
    * [бюджет](http://omr.gov.ua/ru/acts/council/67004/) (змінено 16 грудня 2015)
    * [виконання](http://omr.gov.ua/ru/news/79118/) (станом на 6 січня 2016)
  * 2014
    * [бюджет](http://omr.gov.ua/ru/acts/council/57231/) (змінено 4 грудня 2014)
    * [виконання](http://omr.gov.ua/ru/acts/council/66397/) (звіт затверджено 24 грудня 2014)

## Структура бюджетних даних

### Розділи

* доходи
* дефіцит/профіцит
* видатки
  * за класифікацією (функцією)
  * за розпорядниками
  * за об’єктом (для місцевих та регіональних бюджетів)
  * за регіональною програмою (для регіональних бюджетів)
  * за держпрограмою (для держбюджетів)
* надання кредитів
* міжбюджетні трансферти

### Класифікація (ст.8 Бюджетного кодексу)

Бюджетна класифікація має такі складові частини:

* класифікація доходів бюджету
  * податкові надходження
  * неподаткові надходження
    * доходи від власності та підприємницької діяльності
    * адміністративні збори та платежі, доходи від некомерційної господарської діяльності
    * інші неподаткові надходження
  * доходи від операцій з капіталом
  * трансферти
* класифікація видатків та кредитування бюджету
  * програмна класифікація видатків та кредитування бюджету
  * відомча класифікація видатків та кредитування бюджету
  * функціональна класифікація видатків та кредитування бюджету
* класифікація фінансування бюджету
  * типом кредитора
  * типом боргового зобов'язання
* класифікація боргу
  * типом кредитора
  * типом боргового зобов'язання

#### Абревіатури

* КФК - код функціональної класифікації видатків
* КЕКВ - код економічної класифікації видатків
* КТКВ - код тимчасової класифікації видатків
* КПКВ (КПКВК) - код програмної класифікації видатків (та кредитування)
* КТКВМБ (КТКВКМБ) - код тимчасової класифікації видатків (та кредитування) місцевих бюджетів
* ТПКВКМБ - тимчасова програмна класифікація видатків (та кредитування) місцевих бюджетів
* ТКВКБМС - тимчасова класифікація видатків (та кредитування) місцевого самоврядування

## Стандартизація даних

Найбільш відомий проект зі стандартизації бюджетних даних - [Fiscal Data Package](http://fiscal.dataprotocols.org/spec/#data-files)

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

