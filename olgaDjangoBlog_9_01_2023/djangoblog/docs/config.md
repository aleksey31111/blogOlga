主要功能配置介绍:
缓存：
缓存默认使用localmem缓存，
如果你有redis环境，
可以设置DJANGO_REDIS_URL环境变量，
则会自动使用该redis来作为缓存，
或者你也可以直接修改如下代码来使用。
    Введение в конфигурацию 
    основных функций:
    кеш:
    По умолчанию кеш использует 
    кеш localmem.Если у вас есть 
    среда Redis, вы можете установить 
    переменную среды DJANGO_REDIS_URL, 
    и Redis будет автоматически 
    использоваться в качестве кеша, 
    или вы можете напрямую изменить 
    следующий код, чтобы использовать его.
    Zhǔyào gōngnéng pèizhì jièshào: 
    Huǎncún: Huǎncún mòrèn shǐyòng 
    localmem huǎncún, rúguǒ nǐ yǒu 
    redis huánjìng, kěyǐ shèzhì 
    DJANGO_REDIS_URL huánjìng biànliàng, 
    zé huì zìdòng shǐyòng gāi redis lái 
    zuòwéi huǎncún, huòzhě nǐ yě kěyǐ 
    zhíjiē xiūgǎi rúxià dàimǎ lái shǐyòng.

DjangoBlog/djangoblog/settings.py

Lines 185 to 199 in ffcb2c3

 CACHES = { 
     'default': { 
         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache', 
         'TIMEOUT': 10800, 
         'LOCATION': 'unique-snowflake', 
     } 
 } 
# 使用redis作为缓存
# Использовать Redis в качестве кеша
# Shǐyòng redis zuòwéi huǎncún
 if os.environ.get("DJANGO_REDIS_URL"): 
     CACHES = { 
         'default': { 
             'BACKEND': 'django.core.cache.backends.redis.RedisCache', 
              'LOCATION': f'redis://{os.environ.get("DJANGO_REDIS_URL")}', 
         } 
     } 
 oauth登录:
现在已经支持QQ，微博，Google，GitHub，Facebook登录，需要在其对应的开放平台申请oauth登录权限，然后在
后台->Oauth 配置中新增配置，填写对应的appkey和appsecret以及回调地址。

回调地址示例：
qq：http://你的域名/oauth/authorize?type=qq
微博：http://你的域名/oauth/authorize?type=weibo
type对应在oauthmanager中的type字段。

owntracks：
owntracks是一个位置追踪软件，可以定时的将你的坐标提交到你的服务器上，现在简单的支持owntracks功能，需要安装owntracks的app，然后将api地址设置为: 你的域名/owntracks/logtracks就可以了。然后访问你的域名/owntracks/show_dates就可以看到有经纬度记录的日期，点击之后就可以看到运动轨迹了。地图是使用高德地图绘制。

邮件功能：
同样，将settings.py中的ADMINS = [('liangliang', 'liangliangyy@gmail.com')]配置为你自己的错误接收邮箱，另外修改:

EMAIL_HOST = 'smtp.zoho.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('DJANGO_EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('DJANGO_EMAIL_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = os.environ.get('DJANGO_EMAIL_USER')
为你自己的邮箱配置。

微信公众号
集成了简单的微信公众号功能，在微信后台将token地址设置为:你的域名/robot 即可，默认token为lylinux，当然你可以修改为你自己的，在servermanager/robot.py中。 然后在后台->Servermanager->命令中新增命令，这样就可以使用微信公众号来管理了。

网站配置介绍
在后台->BLOG->网站配置中,可以新增网站配置，比如关键字，描述等，以及谷歌广告，网站统计代码及备案号等等。
其中的静态文件保存地址是保存oauth用户登录的头像路径，填写绝对路径，默认是代码目录。

代码高亮
如果你发现你文章的代码没有高亮，请这样书写代码块:
    логин oauth:
    Теперь он поддерживает вход в QQ, Weibo, Google, GitHub, 
    Facebook, вам необходимо подать заявку на разрешение 
    входа в систему oauth на соответствующей открытой платформе, 
    а затем в
    Добавьте новую конфигурацию в фоновом режиме -> Конфигурация Oauth, 
    заполните соответствующий ключ приложения, секрет приложения и 
    адрес обратного вызова.

    Пример обратного адреса:
    qq: http://ваше доменное имя/oauth/authorize?type=qq
    Weibo: http://ваше доменное имя/oauth/authorize?type=weibo
    type соответствует полю type в oauthmanager.

    собственные треки:
    owntracks — это программное обеспечение для отслеживания 
    местоположения, которое может регулярно отправлять ваши 
    координаты на ваш сервер.Теперь оно просто поддерживает 
    функцию owntracks.Вам нужно установить приложение owntracks, 
    а затем указать адрес API: ваше доменное имя/owntracks/logtracks up. 
    Затем зайдите на свое доменное имя/owntracks/show_dates, 
    чтобы увидеть дату с записями широты и долготы, и нажмите, 
    чтобы увидеть трек движения. Карта нарисована с 
    использованием карты Gaode.

    Функция почты:
    Точно так же настройте 
    ADMINS = [('liangliang', 'liangliangyy@gmail.com')] 
    в settings.py как собственный почтовый ящик с ошибкой 
    получения и измените:

EMAIL_HOST = 'smtp.zoho.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('DJANGO_EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('DJANGO_EMAIL_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = os.environ.get('DJANGO_EMAIL_USER')
    Настройте свой собственный почтовый ящик.

    Публичный аккаунт WeChat
    Интегрируйте простую функцию официальной учетной 
    записи WeChat, установите адрес токена как: ваше 
    доменное имя/робот в фоновом режиме WeChat, 
    токен по умолчанию — lylinux, конечно, вы 
    можете изменить его на свой собственный, 
    в servermanager/robot.py. Затем добавьте 
    новую команду в 
    фоновом режиме -> Servermanager -> command, 
    чтобы вы могли использовать официальную учетную 
    запись WeChat для управления.

Введение в настройку веб-сайта
В фоновом режиме->БЛОГ->настройка веб-сайта вы можете 
добавить конфигурации веб-сайта, такие как ключевые слова, 
описания и т. д., а также рекламу Google, коды статистики 
веб-сайта и номера записей и т. д.
Статический адрес хранилища файлов — это путь аватара для 
сохранения логина пользователя oauth, укажите абсолютный путь, 
а по умолчанию — каталог кода.

подсветка кода
Если вы обнаружите, что код вашей 
статьи не выделен, 
напишите блок кода следующим образом:
Oauth dēnglù: 
Xiànzài yǐjīng zhīchí QQ,
wēi bó,Google,GitHub,Facebook 
dēnglù, xūyào zài qí duìyìng 
de kāifàng píngtái shēnqǐng oauth 
dēnglù quánxiàn, ránhòu zài 
hòutái->Oauth pèizhì zhōng xīn zēng 
pèizhì, tiánxiě duìyìng de appkey hé 
appsecret yǐjí huítiáo dìzhǐ. 
Huítiáo dìzhǐ shìlì: Qq:Http://Nǐ 
de yùmíng/oauth/authorize?Type=qq 
wēi bó:Http://Nǐ de 
yùmíng/oauth/authorize?Type=weibo 
type duìyìng zài oauthmanager zhōng 
de type zìduàn. Owntracks: Owntracks 
shì yīgè wèizhì zhuīzōng ruǎnjiàn, 
kěyǐ dìngshí de jiāng nǐ de zuòbiāo 
tíjiāo dào nǐ de fúwùqì shàng, 
xiànzài jiǎndān de zhīchí 
owntracks gōngnéng, xūyào ānzhuāng 
owntracks de app, ránhòu jiāng api 
dìzhǐ shèzhì wèi: Nǐ de 
yùmíng/owntracks/logtracks 
jiù kěyǐle. Ránhòu fǎngwèn 
nǐ de yùmíng/owntracks/show_dates 
jiù kěyǐ kàn dào yǒu jīngwěidù jìlù 
de rìqí, diǎnjī zhīhòu jiù kěyǐ kàn 
dào yùndòng guǐjīle. Dìtú shì shǐyòng 
gāo dé dìtú huìzhì. Yóujiàn gōngnéng: 
Tóngyàng, jiāng settings.Py zhōng de 
ADMINS = [('liangliang', 
'liangliangyy@gmail.Com')] 
pèizhì wèi nǐ zìjǐ de cuòwù 
jiēshōu yóuxiāng, lìngwài xiūgǎi: 
EMAIL_HOST ='smtp.Zoho.Com' 
EMAIL_PORT = 587 
EMAIL_HOST_USER = os.Environ.Get('DJANGO_EMAIL_USER') 
EMAIL_HOST_PASSWORD = os.Environ.Get('DJANGO_EMAIL_PASSWORD') 
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER SERVER_EMAIL = os.Environ.Get('DJANGO_EMAIL_USER') 
wèi nǐ zìjǐ de yóuxiāng pèizhì. 
Wēixìn gōngzhòng hào jíchéngle 
jiǎndān de wéi xìn gōngzhòng hào gōngnéng, 
zài wēixìn hòutái jiāng token dìzhǐ shèzhì 
wèi: Nǐ de yùmíng/robot jí kě, mòrèn token 
wèi lylinux, dāngrán nǐ kěyǐ xiūgǎi wèi 
nǐ zìjǐ de, zài servermanager/robot.
Py zhōng. Ránhòu zài 
hòutái->Servermanager->mìnglìng 
zhōng xīn zēng mìnglìng, zhèyàng 
jiù kěyǐ shǐyòng wēixìn gōngzhòng 
hào lái guǎnlǐle. Wǎngzhàn pèizhì 
jièshào zài hòutái->BLOG->wǎngzhàn 
pèizhì zhōng, kěyǐ xīn zēng wǎngzhàn 
pèizhì, bǐrú guānjiàn zì, miáoshù děng, 
yǐjí gǔgē guǎnggào, wǎngzhàn tǒngjì 
dàimǎ jí bèi'àn hào děng děng. 
Qízhōng de jìngtài wénjiàn bǎocún 
dìzhǐ shì bǎocún oauth yònghù dēnglù 
de tóuxiàng lùjìng, tiánxiě juéduì 
lùjìng, mòrèn shì dàimǎ mùlù. 
Dàimǎ gāo liàng rúguǒ nǐ fāxiàn 
nǐ wénzhāng de dàimǎ méiyǒu gāo 
liàng, qǐng zhèyàng shūxiě dàimǎ kuài:

也就是说，需要在代码块开始位置加入这段代码对应的语言。
update
如果你发现执行数据库迁移的时候出现如下报错：
    Другими словами, вам нужно добавить язык, 
    соответствующий этому коду, в начале блока кода.
    Обновить
    Если вы обнаружите, что при переносе базы данных возникает 
    следующая ошибка:
    Yě jiùshì shuō, xūyào zài dàimǎ kuài kāishǐ 
    wèizhì jiārù zhè duàn dàimǎ duìyìng de yǔyán. 
    Update rúguǒ nǐ fāxiàn zhíxíng shǔ jù kù qiānyí 
    de shíhòu chūxiàn rúxià bàocuò:
django.db.migrations.exceptions.MigrationSchemaMissing: 
    Unable to create the django_migrations table 
    ((1064, "You have an error in your SQL syntax; 
    check the manual that corresponds to your MySQL 
    server version for the right syntax to use near 
    '(6) NOT NULL)' at line 1"))

可能是因为你的mysql版本低于5.6，需要升级mysql版本>=5.6即可。
django 4.0登录可能会报错CSRF，需要配置下settings.py中的CSRF_TRUSTED_ORIGINS
https://github.com/liangliangyy/DjangoBlog/blob/master/djangoblog
/settings.py#L39
    Это может быть связано с тем, что ваша версия mysql ниже 5.6, 
    вам необходимо обновить версию mysql >= 5.6.
    Вход в систему Django 4.0 может сообщать об ошибке CSRF, 
    вам необходимо настроить CSRF_TRUSTED_ORIGINS в settings.py
    Kěnéng shì yīnwèi nǐ de mysql bǎnběn dī yú 5.6, 
    Xūyào shēngjí mysql bǎnběn >=5.6 Jí kě. 
    Django 4.0 Dēnglù kěnéng huì bàocuò CSRF, 
    xūyào pèizhì xià settings.Py zhōng de CSRF_TRUSTED_ORIGINS
