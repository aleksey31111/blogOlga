import logging

from djangoblog.utils import get_current_site
from djangoblog.utils import send_email

logger = logging.getLogger(__name__)


def send_comment_email(comment):
    site = get_current_site().domain
    subject = 'Спасибо за ваш комментарий'
    article_url = "https://{site}{path}".format(
        site=site, path=comment.article.get_absolute_url())
    html_content = """
                   <p>Большое спасибо за ваши комментарии 
                        на этом сайте</p>
                   Вы можете посетить
                   <a href="%s" rel="bookmark">%s</a>
                   чтобы просмотреть ваши комментарии,
                   Еще раз спасибо!
                   <br />
                   Если ссылка выше не работает, 
                   скопируйте ее в браузер.
                   %s
                   """ % (article_url, comment.article.title, article_url)
    tomail = comment.author.email
    send_email([tomail], subject, html_content)
    try:
        if comment.parent_comment:
            html_content = """
                    Ваш <a href="%s" rel="bookmark">%s</a> комментарий <br/> %s <br/> Я получил ответ, иди проверь
                    <br/>
                    Если ссылка выше не работает, скопируйте ее в браузер.
                    %s
                    """ % (article_url, comment.article.title, comment.parent_comment.body, article_url)
            tomail = comment.parent_comment.author.email
            send_email([tomail], subject, html_content)
    except Exception as e:
        logger.error(e)
