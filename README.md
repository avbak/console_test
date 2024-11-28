1. Активировать VENV
Win: `.\venv\Scripts\activate` или Unix/Mac: `source venv/bin/activate`
  
2. Установить зависимости (venv) `python -m pip install -r requirements.txt`

3. Поменять API ключ в файле pytest.ini

4. Поместить бинарные файлы проекта в папку project

5. При запуске на Linux заменить путь к бинарным файлам в ./tests/funcs.py: `./project/OptimusMuneris.exe`

5. Запустить тесты командой `pytest` из корня директории int24test
