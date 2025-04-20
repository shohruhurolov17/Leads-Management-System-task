from django.contrib import admin
from django.contrib.auth.models import User, Group
from unfold.admin import ModelAdmin
from unfold.forms import (
    UserChangeForm,
    AdminPasswordChangeForm,
    UserCreationForm
)
from django.contrib.auth.admin import UserAdmin, GroupAdmin


admin.site.unregister(Group)
admin.site.unregister(User)


@admin.register(Group)
class GroupAdmin(GroupAdmin, ModelAdmin):
    
    model = Group
    list_display = ('name', )


@admin.register(User)
class UserAdmin(UserAdmin, ModelAdmin):
    model = User
    list_display = [
        'id',  
        'first_name', 
        'last_name', 
        'email'
    ]

    form = UserChangeForm

    change_password_form = AdminPasswordChangeForm

    add_form = UserCreationForm

    search_fields = ('first_name', 'last_name', 'email')

    list_filter_submit = True

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('username', 'password1', 'password2')
            }
        ),
    )

    fieldsets = (
        (
        'Shaxsiy ma\'lumolari',
         {
             'fields': (
                     'first_name', 'last_name', 'username', 'email') 
        }
        ),
        (
        'Ruxsatlar',
         {'fields': ('is_staff', 'is_superuser', 'is_active', 'groups', 'password')}
    ),
    )