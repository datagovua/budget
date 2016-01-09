## Open Budget

Open Budget - ініціатива Sergey Gerasimov @ SoftServe (mail[at]grsmv.com).

Ідея:

* зібрати оригінальні файли бюджетів в одному місці
* обробити в ручному режимі
* надати API
* візуалізувати

Переваги:

* реалізовано API
* частково реалізована візуалізація

Недоліки:

* ручний режим збору файлів
* ручний режим обробки файлів (https://github.com/open-budget/data/issues/55)

Реалізація:

* http://open-budget.org/
* https://github.com/open-budget/

## Конвертація Open Budget у CSV стандарту OpenSpending

    ./import-from-openbudget.py > data/expenses.csv
