# Как запустить сея чудо

1. Скачиваем репу
2. Переходим в папку 
3. Создаём вируальное окуржение
4. Активируем его
5. Подтягиваем библиотеки из requirements.txt
6. Мигрируем(Так как тестовый проект не подключал другие БД, юзаю SQLite)
7. Из FR_test_task запускаем сервер → python survey/manage.py runserver