# from django.db import models
# from blog.models import Post
#
#
# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='Отношение к статъе')
#     name = models.CharField(max_length=100, verbose_name='Имя')
#     email = models.EmailField(verbose_name='Электронный адрес')
#     body = models.TextField(verbose_name='Содержание комментария')
#     created_on = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
#     active = models.BooleanField(default=False, verbose_name='Активный')
#
#     def __str__(self):
#         return 'Comment {} by {}'.format(self.body, self.name)
#
#     class Meta:
#         verbose_name = 'Комментарий'
#         verbose_name_plural = 'Комментарии'
#         ordering = ['-created_on']
