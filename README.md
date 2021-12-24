# Week number API
## Web-приложение для получения номера недели по дате (отсчет начинается с воскресенья)

### API
- Запрос
```
GET /?date=2020-10-14
```
- Ответ
  
```json
{"week_number":42,"date":"2020-10-14"}
```

  
### Запуск проекта
- создать виртуальное окружение
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
 


