
---

### 1. Блокирующая ошибка при запуске на Ubuntu [Linux]

**Шаги:**
1. Запустить приложение без аргументов

**Ожидаемое поведение:** запуск приложения, вывод справки

**Фактическое поведение:** ошибка `[PYI-3736:ERROR] Failed to load Python shared library '/tmp/_MEIJF1TqL/libpython3.12.so': dlopen: /lib/x86_64-linux-gnu/libm.so.6: version GLIBC_2.38 not found (required by /tmp/_MEIJF1TqL/libpython3.12.so)`

****Дополнительные комментарии:****
Судя по информации из репозитория Pyinstaller, пакет был собран на системе с более высокой версией библиотеки:
[https://github.com/orgs/pyinstaller/discussions/7541#discussioncomment-5534584](https://github.com/orgs/pyinstaller/discussions/7541#discussioncomment-5534584)

---

### 2. Необработанное исключение при принудительном выключении  [Linux, Windows]

**Шаги:**
1. Запустить приложение с аргументом `--meaning 50` или `--weather Sydney` 
2. Не дожидаясь завершения функции остановить процесс комбинацией `CRTL + C`

**Ожидаемое поведение:** выводится сообщение об отмене операции

**Фактическое поведение:** необработанное исключение

---

### 3. Ошибка сложения [Windows]

**Шаги:**
1. Запустить приложение с аргументом `--add 10 10`

**Ожидаемое поведение:** вывод приложением числа 20

**Фактическое поведение:** вывод приложением числа 21

**Дополнительные комментарии:** "лишняя" единица прибавляется при всех операциях сложения на платформе Windows

---

### 4. Ошибка вычитания [Linux]

**Шаги:**
1. Запустить приложение с аргументом `--subtract 10 10`
**Ожидаемое поведение:** вывод приложением числа 0

**Фактическое поведение:** вывод приложением числа -1

**Дополнительные комментарии:** "лишняя" единица убавляется при всех операциях сложения на платформе Linux

---

### 5. Деление на ноль (0/0) [Windows, Linux]

**Шаги:**
1. Запустить приложение с аргументом `--divide 0 0`

**Ожидаемое поведение:** сообщение об ошибке

**Фактическое поведение:** вывод приложением числа 0

---

### 6. Деление на 0 (число!=0/0) [Windows, Linix]

**Шаги:**
1. Запустить приложение с аргументом `--divide 123 0

**Ожидаемое поведение:** сообщение об ошибке

**Фактическое поведение:** вывод приложением огромного числа

---

### 7. Ошибка при умножении крупных чисел  [Windows, Linux]

**Шаги:**
1. Запустить приложение с аргументом `--multiply 1337 -1000

**Ожидаемое поведение:** вывод приложением числа -1337000
Фактические поведение: вывод приложением числа 1787569000

**Дополнительные комментарии:** 
Ошибка происходит, если один или оба операнда являются положительным числом >=1337. Результат выражения при этом остается положительным даже в случае, если второй операнд является отрицательным числом

---

### 8. Неверная шкала градусов в чекере погоды [Windows, Linux]

**Шаги:** 
1. Запустить приложение с аргументом `--weather Dubai

**Ожидаемое поведение:** вывод приложением корректной температуры в градусах Цельсия

**Фактическое поведение:** вывод приложением сильно завышенного числа

**Дополнительные комментарии:** фактический результат не является Градусами фаренгейта или любой другой единицей, которая возвращается в ответе API запроса. Вероятно причина в вычислениях.

---

### 9. Некотролируемый пользовательский ввод в чекере погоды [Windows, Linux]

**Шаги:**
1. Запустить приложение с аргументом `--weather "Moscow" "API_KEY&q=Dubai"`
2. Запустить приложение с аргументом `--weather "Moscow"`
3. Запустить приложение с аргументом `--weather "Dubai"

**Ожидаемое поведение:** приложение экранирует и отбрасывает символы, за исключением тех, которые могут быть частью названия населенного пункта или его индекса [функционал заявлен в документации API]. Выводится погода Москвы

**Фактическое поведение:** пользователь имеет возможность менять структуру API запроса, вводить неадекватные значения. Выводится погода из подмененного запроса.

---

### 10. Вывод чувствительной информации при ошибочном пользовательском вводе  [Windows, Linux]

**Шаги:** 
1. Запустить приложение с аргументом `--weather "1"
2. Запустить приложение с аргументом `--weather "Moscow" "1"

**Ожидаемое поведение:** сообщение об ошибке "Weather data not available."

**Фактическое поведение:** приложение раскрывает пользователю код ошибки, структуру запроса, API-ключ

---

### 11. Ошибка о недоступности данных о погоде для городов, которые начинаются с английских гласных букв [Windows, Linux]

**Шаги:**
1. Запустить приложение с аргументом `--weather "Ankara"

**Ожидаемое поведение:** приложение отображает текущую погоду для города

**Фактическое поведение:** ошибка "Weather data not available."

**Дополнительные комментарии:** ручная проверка через API показывает, что проблема находятся на стороне приложения.

---

### 12. Запрос текущей погоды без подключения к сети приводит к необработанному исключению [Windows, Linux]
**Шаги:**

1. Отключить интернет-соединение на устройстве или виртуальной машине
2. Запустить приложение с параметром `--weather "Moscow"

**Ожидаемое поведение:** приложение сообщает о недоступности сети или выдает ошибку ошибка "Weather data not available."

**Фактическое поведение:** приложение выводит ошибку библиотеки urllib

---

### 13. Граничные значения чекера "значения жизни" приводят к неверному выводу [Windows, Linux]

**Шаги:**
1. Запустить приложение с параметром `--meaning 100

**Ожидаемое поведение:** приложение выводит число 42

**Фактическое поведение:** приложение выводит число 56154

---

### 14. Дробные значения чекера "значения жизни" приводят к утечке памяти [Windows, Linux]

**Шаги:** 
1. Запустить приложение с параметром `--meaning 50.12345`

**Ожидаемое поведение:** приложение потребляет не более 1ГБ ОЗУ

**Фактическое поведение:** приложение потребляет в разы больший объем ОЗУ

---

### 15. Любые значения чекера "значения жизни" приводят к излишнему потреблению ОЗУ [Linux]

**Шаги:** 
1. Запустить приложение с параметром `--meaning 10`

**Ожидаемое поведение:** приложение потребляет не более 1ГБ ОЗУ

**Фактическое поведение:** приложение потребляет около 3ГБ ОЗУ

---

### 16. Неверные значения чекера "значения жизни" приводят к лишнему выводу [Windows, Linux]

**Шаги:** 
1. Запустить приложение с параметром `--meaning a`

**Ожидаемое поведение:** приложение выводит ошибку о недопустимом вводе

**Фактическое поведение:** приложение выводит ошибку о недопустимом вводе и выводит значение None

---

### 17. Крайне малое дробное значение чекера "значения жизни" позволяют выйти за границы [Windows, Linux]

**Шаги:** 
1. Запустить приложение с параметром `--meaning 100.00000000000000000000000000001`

**Ожидаемое поведение:** приложение сообщает о выходе за рамки

**Фактическое поведение:** приложение выводит число 56154

---

### 18. Ошибочное название алгоритма шифрования [Windows, Linux]

**Шаги:** 
1. Запустить приложение с параметром `--encrypt HELLO HELLO`

**Ожидаемое поведение:** происходит шифрование текста

**Фактическое поведение:** приложение выводит строку нулей, что очень похоже на XOR операцию, а не шифрование AES

---

### 19. Ошибка дешифрования текста [Windows, Linux]

**Шаги:** 
1. Запустить приложение с параметром `--encrypt HELLO 123
2. Запустить приложение с параметром `--decrypt 79777f7d7d 123

**Ожидаемое поведение:** приложение выводит сообщение "HELLO"

**Фактическое поведение:** приложение выводит сообщение "HELL"

**Дополнительные комментарии:**
Если шифровался один символ, то при дешифрации приложение выводит пустую строку

---

### 20. Вызов программы с аррументом без операндов приводит к исключению

**Шаги:** 
1. Запустить приложение с параметром `--add`
2. Запустить приложение с параметром `--add 123`

**Ожидаемое поведение:** приложение выводит сообщение об ошибочном вводе

**Фактическое поведение:** приложение выводит сообщение о необработанном исключении

**Дополнительные комментарии:** 
`KeyboardInterrupt`
`[PYI-24108:ERROR] Failed to execute script 'OptimusMuneris' due to unhandled exception!`


