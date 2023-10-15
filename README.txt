#активируем виртуальное окружение 
venv/scripts/activate

#обновляем пакетный менеджер
python -m pip install --upgrade pip

#устанавливаем framework
pip install django

#создаем проект
django-admin startproject blog_project

#переходим папку с проектами
cd blog_project

#создаем приложение 
python manage.py startapp blog

#полключаем базу данных и создаем вспомогательные таблицы
python manage.py migrate 

#запускаем сервер 
python manage.py runserver

#при изменении базы данных
python manage.py makemigrations
python manage.py migrate 

#регистрация админа
python manage.py createsuperuser

#работа с изображениями
 pip install Pillow