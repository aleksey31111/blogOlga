Использование развертывания Docker 
поддерживает следующие два метода:
    метод зеркалирования докеров
    Этот проект уже поддерживает 
    развертывание Docker. 
    Если у вас уже есть mysql, 
    вы можете напрямую использовать 
    базовый образ. Команда запуска 
    выглядит следующим образом:

    docker pull 
        liangliangyy/djangoblog:последний
    docker run -d -p 
        8000:8000 -e 
        DJANGO_MYSQL_HOST=mysqlhost -e 
        DJANGO_MYSQL_PASSWORD=mysqlrootpassword 
        -e DJANGO_MYSQL_USER=root -e 
        DJANGO_MYSQL_DATABASE=djangoblog 
        --name djangoblog 
        liangliangyy/djangoblog:latest
    После завершения запуска посетите 
    http://127.0.0.1:8000.

использовать docker-compose
Если у вас нет базовых служб, таких как mysql, вы можете использовать docker-compose для запуска.Конкретные команды следующие:

сборка с докером
docker-compose up -d
Файлы данных mysql, сгенерированные этим методом, находятся в папке bin/datas/mysql.
После завершения запуска посетите http://127.0.0.1.

использовать эс
Если вы планируете использовать es в качестве внутренней поисковой системы, вы можете использовать следующую команду для ее запуска:

docker-compose -f docker-compose.yml -f docker-compose.es.yml сборка
docker-compose -f docker-compose.yml -f docker-compose.es.yml up -d
Файлы данных es, сгенерированные этим методом, находятся в папке bin/datas/es.

Инструкции по настройке:
Многие конфигурации этого проекта основаны на переменных среды, и все переменные среды следующие:

Имя переменной среды Значение по умолчанию Примечания
DJANGO_DEBUG Ложь
DJANGO_SECRET_KEY DJANGO_BLOG_CHANGE_ME Пожалуйста, измените его, рекомендуется генерировать случайным образом
DJANGO_MYSQL_DATABASE джангоблог
корень DJANGO_MYSQL_USER
DJANGO_MYSQL_PASSWORDdjangoblog_123
DJANGO_MYSQL_HOST 127.0.0.1
DJANGO_MYSQL_PORT 3306
DJANGO_MEMCACHED_ENABLE Истинно
DJANGO_MEMCACHED_LOCATION 127.0.0.1:11211
DJANGO_BAIDU_NOTIFY_URL http://data.zz.baidu.com/urls?site=https://www.example.org&token=CHANGE_ME Получите адрес интерфейса на платформе веб-мастеров Baidu.
DJANGO_EMAIL_TLS Ложь
DJANGO_EMAIL_SSL Верно
DJANGO_EMAIL_HOST smtp.example.org
DJANGO_EMAIL_PORT 465
DJANGO_EMAIL_USER SMTP_USER_CHANGE_ME
DJANGO_EMAIL_PASSWORD SMTP_PASSWORD_CHANGE_ME
DJANGO_ADMIN_EMAIL admin@example.org
DJANGO_WEROBOT_TOKEN DJANGO_BLOG_CHANGE_ME
DJANGO_ELASTICSEARCH_HOST
После первой загрузки используйте следующую команду для создания суперпользователя:

docker exec -it djangoblog python /code/djangoblog/manage.py создает суперпользователя