from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.site_header = 'MRI ADMIN'
admin.site.site_title = 'MRI ADMIN AREA'
admin.site.index_title = 'WELCOME TO MRI ADMIN'


class MarksInline(admin.TabularInline):
    model = Marks


class ExamAdmin(admin.ModelAdmin):

    inlines = [MarksInline]


class UserAdmins(UserAdmin):
    list_display = ('username', 'joined_date', 'is_staff')
    search_fields = ('username',)
    readonly_fields = ('joined_date', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(News)
admin.site.register(Calendar)
admin.site.register(User, UserAdmins)
admin.site.register(Student)
admin.site.register(Class_room)
admin.site.register(Exam, ExamAdmin)
