<p align="center"> 
  <img  src="https://lms.mipt.ru/pluginfile.php/1/core_admin/logo/0x200/1714642582/logo.png" data-canonical-src="https://lms.mipt.ru/pluginfile.php/1/core_admin/logo/0x200/1714642582/logo.png" width="400" />
</p>

<h1 align="center">
  Разработка Web-приложения на Django в рамках ЦК
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-green">
</p>

## Содержание
- [Описание проекта](#опись)
- [Презентация](#преза)
- [Начало работы](#начало)
- [Тестирование](#тестирование)


## Описание проекта

В рамка проекта был реализован сайт на образовательную тематику по предмету **Физика**.

Реализовано 4 слайда, а также admin для работы с базой данных (задачи по предметам).

### Слайды:
| Ссылка                  | Значение               |
|-------------------------|------------------------|
|         ```/```         |Начальная страница      |
|      ```/quiz/```       |Страница с тестом       |
|  ```/quiz/result/```    |Страница с результатами |
|  ```/'все что другое'```|Страница 404            |


## 💻 Ссылка на видеозапись презентации проекта

      
 [Видео презентация на яндекс диске](https://disk.yandex.ru/i/jXcWkSGwYcwPAg)
    

## 🛠️ Установка проекта 


1) Установить poetry:

        pip install poetry

2) Клонировать репозиторий:

        git clone https://github.com/Sheldd/Django-project.git
   
3) Установить зависимости (запустить внутри директории Django-project) :

        poetry install

4) Запустить веб приложение:

        poetry run python manage.py runserver

5) Вставить ссылку в браузер:

         http://127.0.0.1:8000/



## 💻 Тестирование

- Оценка Pylint = 9.05/10
- Flake8

  

   
