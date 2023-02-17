1 主要功能： Основная функция:
    1 Zhǔyào gōngnéng:
2 文章，页面，分类目录，标签的添加，删除，
编辑等。文章、评论及页面支持Markdown，支持代码高亮。
    Добавление и удаление статей, страниц, категорий,
    тегов, редактировать и т.д. Статьи,
    комментарии и страницы поддерживают
    Markdown и подсветку кода.
    2 Wénzhāng, yèmiàn, fēnlèi mùlù,
    biāoqiān de tiānjiā, shānchú,
    biānjí děng. Wénzhāng,
    pínglùn jí yèmiàn zhīchí Markdown,
    zhīchí dàimǎ gāo liàng.

3 支持文章全文搜索。
    Поддержка полнотекстового поиска статей.
    3 Zhīchí wénzhāng quánwén sōusuǒ.

4 完整的评论功能，包括发表回复评论，以及评论的邮件提醒，
支持Markdown。
    Полная функция комментариев,
    включая публикацию ответных комментариев
    и напоминания по электронной почте о комментариях,
    Маркдаун поддерживается.
    4 Wánzhěng de pínglùn gōngnéng,
    bāokuò fābiǎo huífù pínglùn,
    yǐjí pínglùn de yóujiàn tíxǐng,
    zhīchí Markdown.

5 侧边栏功能，最新文章，最多阅读，标签云等。
    Функции боковой панели,
    последние статьи,
    самые читаемые,
    облако тегов и многое другое.
    5 Cè biān lán gōngnéng,
    zuìxīn wénzhāng,
    zuìduō yuèdú, biāoqiān yún děng.

6 支持Oauth登陆，现已有Google,GitHub,facebook,微博,QQ登录。
    Поддерживает вход Oauth и
    теперь имеет входы Google, GitHub,
    facebook, Weibo и QQ
    6 Zhīchí Oauth dēnglù,
    xiàn yǐ yǒu Google,GitHub,
    facebook, wēi bó,QQ dēnglù.

7 支持Redis缓存，支持缓存自动刷新。
    Поддерживает кеш Redis
    и автоматическое обновление кеша.
    7 Zhīchí Redis huǎncún,
    zhīchí huǎncún zìdòng shuāxīn.

8 简单的SEO功能，新建文章等会自动通知Google和百度。
    Простые функции SEO, новые статьи и т. д.
    будут автоматически уведомлять Google и Baidu.
    8 Jiǎndān de SEO gōngnéng,
    xīnjiàn wénzhāng děng huì
    zìdòng tōngzhī Google hé bǎidù.

9 集成了简单的图床功能。
    Интегрирует простую функцию кровати-картинки.
    9 Jíchéngle jiǎndān de tú chuáng gōngnéng.

10 集成django-compressor，自动压缩css，js。
    Интегрируйте django-compressor,
    автоматически сжимайте css, js.
    10 Jíchéng django-compressor, zìdòng yāsuō css,js.

11 网站异常邮件提醒，若有未捕捉到的异常会自动发送提醒邮件。
    Напоминание по электронной почте
    об исключении веб-сайта.
    Если есть неперехваченное исключение,
    электронное письмо с напоминанием будет
    отправлено автоматически.
    11 Wǎngzhàn yìcháng yóujiàn tíxǐng,
    ruò yǒu wèi bǔzhuō dào de yìcháng huì
    zìdòng fāsòng tíxǐng yóujiàn.

12 集成了微信公众号功能，现在可以使用微信公众号来管理你的vps了。
    Интегрирует функцию официальной учетной записи WeChat,
    и теперь вы можете использовать официальную
    учетную запись WeChat для управления вашим vps.
    12 Jíchéngle wēixìn gōngzhòng hào gōngnéng,
    xiànzài kěyǐ shǐyòng wēixìn gōngzhòng hào lái
    guǎnlǐ nǐ de vpsle.

13 安装 Установить 13 Ānzhuāng

14 mysql客户端从pymysql修改成了mysqlclient，具体请参考 pypi 查看安装前的准备。
    Клиент mysql был изменен с pymysql на mysqlclient.Подробности см.
    в pypi, чтобы просмотреть подготовку перед установкой.
    14 Mysql kèhù duān cóng pymysql xiūgǎi chéngle mysqlclient,
    jùtǐ qǐng cānkǎo pypi chákàn ānzhuāng qián de zhǔnbèi.


16 使用pip安装： pip install -Ur requirements.txt
    Установить с помощью pip: pip install -Ur requirements.txt
    16 Shǐyòng pip ānzhuāng: Pip install -Ur requirements.Txt

18 如果你没有pip，使用如下方式安装：
    Если у вас нет pip, установите его следующим образом:
    18 Rúguǒ nǐ méiyǒu pip, shǐyòng rúxià fāngshì ānzhuāng:

20 OS X / Linux 电脑，终端下执行:
    Компьютер OS X/Linux, выполните под терминалом:
    20 OS X/ Linux diànnǎo, zhōngduān xià zhíxíng:

22 curl http://peak.telecommunity.com/dist/ez_setup.py | python
    завиток http://peak.telecommunity.com/dist/ez_setup.py | питон
23 curl https://bootstrap.pypa.io/get-pip.py | python
    завиток https://bootstrap.pypa.io/get-pip.py | python
24 Windows电脑： Компьютер с Windows:
    24 Windows diànnǎo:

26 下载 http://peak.telecommunity.com/dist/ez_setup.py
和 https://raw.github.com/pypa/pip/master/contrib/get-pip.py
这两个文件，双击运行。
    Скачать http://peak.telecommunity.com/dist/ez_setup.py
    и https://raw.github.com/pypa/pip/master/contrib/get-pip.py.
    Эти два файла, дважды щелкните для запуска.
    26 Xiàzài http://Peak.Telecommunity.Com/dist/ez_setup.Py
    hé https://Raw.Github.Com/pypa/pip/master/contrib/get-pip.Py
    zhè liǎng gè wénjiàn, shuāngjī yùnxíng.

28 运行  бегать 28 Yùnxíng
29 修改djangoblog/setting.py 修改数据库配置，如下所示：
    Измените djangoblog/setting.py,
    чтобы изменить конфигурацию базы данных следующим образом:
    29 Xiūgǎi djangoblog/setting.Py xiūgǎi shùjùkù pèizhì, rúxià suǒ shì:

31 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangoblog',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'host',
        'PORT': 3306,
    }
}
41 创建数据库  создать базу данных
    41 Chuàngjiàn shùjùkù

42 mysql数据库中执行:
    Выполнить в базе данных mysql:
    42 Mysql shùjùkù zhōng zhíxíng:

44 CREATE DATABASE `djangoblog`
/*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
    44 СОЗДАЙТЕ БД `djangoblog`
    /*!40100 НАБОР СИМВОЛОВ ПО УМОЛЧАНИЮ utf8mb4 COLLATE utf8mb4_unicode_ci */;
45 然后终端下执行:  Затем выполните в терминале:
    45 Ránhòu zhōngduān xià zhíxíng:

47 python manage.py makemigrations
48 python manage.py migrate
49 创建超级用户  создать суперпользователя
    49 Chuàngjiàn chāojí yònghù
50 终端下执行:  Выполнить под терминалом:
    50 Zhōngduān xià zhíxíng:

52 python manage.py createsuperuser
53 创建测试数据  Создать тестовые данные
    53 Chuàngjiàn cèshì shùjù
54 终端下执行: Выполнить под терминалом:
    54 Zhōngduān xià zhíxíng:

56 python manage.py create_testdata
57 收集静态文件  Собирать статические файлы
    57 Shōují jìngtài wénjiàn
58 终端下执行:  Выполнить под терминалом:
    58 Zhōngduān xià zhíxíng:
python manage.py collectstatic --noinput
python manage.py compress --force
62 开始运行：  начать операцию:
    62 Kāishǐ yùnxíng:
63 执行：  осуществлять: 63 Zhíxíng:
63 python manage.py runserver

65 浏览器打开: http://127.0.0.1:8000/ 就可以看到效果了。
    Откройте браузер: http://127.0.0.1:8000/, чтобы увидеть эффект.
    65 Liúlǎn qì dǎkāi: Http://127.0.0.1:8000/ Jiù kěyǐ kàn dào xiàoguǒle.

67 服务器部署  развертывание сервера
    67 Fúwùqì bùshǔ
68 本地安装部署请参考 DjangoBlog部署教程 有详细的部署介绍.
    Для локальной установки и развертывания
    обратитесь к руководству по развертыванию
    DjangoBlog для подробного ознакомления с
    развертыванием.
    68 Běndì ānzhuāng bùshǔ qǐng cānkǎo
    DjangoBlog bùshǔ jiàochéng yǒu
    xiángxì de bùshǔ jièshào.

70 本项目已经支持使用docker来部署，如果你有docker环境那么可以使用docker来部署，具体请参考:docker部署
    Этот проект уже поддерживает использование Docker для развертывания.
    Если у вас есть среда Docker, вы можете использовать
    Docker для развертывания. Дополнительные сведения см.
    в разделе: развертывание Docker.
    70 Běn xiàngmù yǐjīng zhīchí shǐyòng docker lái bùshǔ,
    rúguǒ nǐ yǒu docker huánjìng nàme kěyǐ shǐyòng docker
    lái bùshǔ, jùtǐ qǐng cānkǎo:Docker bùshǔ

72 更多配置:  Больше конфигурации:
    72 Gèng duō pèizhì:
73 更多配置介绍  Подробнее о конфигурации
    73 Gèng duō pèizhì jièshào
74 集成elasticsearch  Интеграция эластичного поиска
    74 Jíchéng elasticsearch

76 问题相关  Связанный с вопросом
    76 Wèntí xiāngguān
77 有任何问题欢迎提Issue,或者将问题描述发送至我邮箱 liangliangyy#gmail.com.我会尽快解答.推荐提交Issue方式.
    Если у вас есть какие-либо вопросы,
    пожалуйста, поднимите вопрос или отправьте
    описание проблемы на мою электронную
    почту liangliangyy#gmail.com.
    Я отвечу на него как можно скорее.
    Рекомендуется отправить вопрос.
    77 Yǒu rènhé wèntí huānyíng tí Issue,
    huòzhě jiāng wèntí miáoshù fāsòng zhì
    wǒ yóuxiāng liangliangyy#gmail.Com.
    Wǒ huì jǐnkuài jiědá.
    Tuījiàn tíjiāo Issue fāngshì.

79 致大家🙋‍♀️🙋‍♂️Всем 🙋‍♀️🙋‍♂️
    79 Zhì dàjiā 🙋‍♀️🙋‍♂️
80 如果本项目帮助到了你，请在这里留下你的网址，让更多的人看到。 您的回复将会是我继续更新维护下去的动力。
    Если этот проект помог вам,
    оставьте здесь свой URL,
    чтобы его увидело больше людей.
    Ваш ответ будет мотивацией для меня продолжать обновлять и поддерживать.
    80 Rúguǒ běn xiàngmù bāngzhù dàole nǐ,
    qǐng zài zhèlǐ liú xià nǐ de wǎngzhǐ,
    ràng gèng duō de rén kàn dào.
    Nín de huífù jiāng huì shì wǒ jìxù gēngxīn wéihù xiàqù de dònglì.

82 捐赠  пожертвовать 83 Juānzèng
83 如果您觉得本项目对您有所帮助，欢迎您请我喝杯咖啡，您的支持是我最大的动力，您可以扫描下方二维码为我付款，谢谢。
    Если вы считаете, что этот проект полезен для вас,
    добро пожаловать, чтобы купить мне чашку кофе.
    Ваша поддержка - моя самая большая мотивация.
    Вы можете отсканировать QR-код ниже, чтобы заплатить за меня, спасибо.
    83 Rúguǒ nín juédé běn xiàngmù duì nín yǒu suǒ bāngzhù,
    huānyíng nín qǐng wǒ hē bēi kāfēi, nín de zhīchí shì wǒ zuìdà de dònglì,
    nín kěyǐ sǎomiáo xiàfāng èr wéi mǎ wèi wǒ fùkuǎn, xièxiè.

85 支付宝：Алипай:
    85 Zhīfùbǎo:

87 微信：  WeChat:
    87 Wēixìn:

89 感谢jetbrains
    спасибо реактивные мозги
    89 Gǎnxiè jetbrains
