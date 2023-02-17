from django.contrib import admin
# from ckeditor_uloader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe
# from django import forms
from .models import Post, Category, Comment


# class BlogAdminForm(forms.ModelForm)
#     body = forms.CharField(widget=CKEditorUploadingWidget)
#
#     class Meta:
#         model = 'Post'
#         fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    # form = BlogAdminForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'author', 'title', 'cat', 'created',
                    'status', 'updated', 'photo', 'publish')
    list_display_links = ('id', 'title', 'created', 'author', 'updated')
    search_fields = ('title', 'body')
    list_editable = ('status',)
    list_filter = ('status', 'created', 'updated', 'publish')
    # fields = ('title', 'slug', 'cat', 'body', 'author',
    #           'get_html_photo', 'publish', 'status')
    # readonly_fields = ('get_html_photo', 'created', 'updated')

    # def get_html_photo(self, object):
    #     if object.photo:
    #         return mark_safe(f"<img src='{object.photo.url}' width='50'>")
    #
    # get_html_photo.shot_description = "Миниатюра"


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'path', 'article_id', 'author_id', 'content', 'pub_date')
#     list_filter = ('pub_date',)
#     search_fields = ('name', 'email', 'content')
#     # actions = ['approve_comments']
#
#     # def approve_comments(self, request, queryset):
#     #     queryset.update(active=True)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

# admin.site.site_header = 'Panel of Admin hello_world_07_01_2023'
# admin.site.site_title = "Panel Of Admin hello_world_07_01_2023"
