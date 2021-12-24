# Week number API
## Web-приложение для получения номера недели по дате (отчет начинается с воскресенья)

### Приложение предоставляет один URL
  - Запрос
  GET /
  {
  "date": "2020-10-14"
  }
  ```
  - Ответ
  ```
  {
  {"week_number":42,"date":"2020-10-14"}
  }
  ```

  
### Запуск проекта

```shell script
python3.9 -m venv venv
```
- активировать виртуальное окружение
```shell script
source venv/bin/activate
```
- установить зависимости
```shell script
pip install -r requirements.txt
```
- запустить
```shell script
./uvicorn main:app --reload
```
- открыть в браузере http://localhost:8000 
 


