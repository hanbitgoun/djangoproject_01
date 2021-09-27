FROM python:3.9.0

WORKDIR /home/

RUN echo "dueno"

RUN git clone https://github.com/hanbitgoun/djangoproject_01.git

WORKDIR /home/djangoproject_01/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=djangoProject_2.settings.deploy && python manage.py migrate --settings=djangoProject_2.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=djangoProject_2.settings.deploy djangoProject_2.wsgi --bind 0.0.0.0:8000"]