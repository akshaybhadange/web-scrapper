from django.conf.urls import url
from django.urls import reverse
from wagtail.admin.menu import MenuItem
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail.core import hooks

# from .models import BlogPage,BlogIndexPage
#
#
#
# class MyPageModelAdmin(ModelAdmin):
#     model = BlogPage
#     menu_label = 'BlogPage' # ditch this to use verbose_name_plural from model
#     menu_icon = 'date' # change as required
#     menu_order = 200 # will put in 3rd place (000 being 1st, 100 2nd)
#     add_to_settings_menu = False # or True to add your model to the Settings sub-menu
#
#
# # Now you just need to register your customised ModelAdmin class with Wagtail
# modeladmin_register(MyPageModelAdmin)
#
