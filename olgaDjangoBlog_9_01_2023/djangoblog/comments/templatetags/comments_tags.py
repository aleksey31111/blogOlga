from django import template

register = template.Library()


@register.simple_tag
def parse_commenttree(commentlist, comment):
    """Получить список дочерних комментариев
    текущего комментария
        Применение: {% parse_commenttree article_comments comment as childcomments %}
    """
    datas = []

    def parse(c):
        childs = commentlist.filter(parent_comment=c, is_enable=True)
        for child in childs:
            datas.append(child)
            parse(child)

    parse(comment)
    return datas


@register.inclusion_tag('comments/tags/comment_item.html')
def show_comment_item(comment, ischild):
    """Комментарий"""
    depth = 1 if ischild else 2
    return {
        'comment_item': comment,
        'depth': depth
    }
