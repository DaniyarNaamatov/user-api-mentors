from django.contrib import admin
from users_backend.models import User


@admin.register(User)
class CollectionAdmin(admin.ModelAdmin):

    list_display = ('username', 'email', )



