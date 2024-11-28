1. Активировать VENV
a) Win:
  PS> `python -m venv venv`
  PS> `.\venv\Scripts\activate`
  (venv) PS> `python -m pip install -r requirements.txt`

b) Unix/Mac:
  $ `python -m venv venv`
  $ `source venv/bin/activate`
  (venv) $ `python -m pip install -r requirements.txt`

2. Поменять API ключ в файле pytest.ini

3. Поместить бинарные файлы проекта в папку project
4. Запустить тесты командой `pytest` из корня директории int24test
