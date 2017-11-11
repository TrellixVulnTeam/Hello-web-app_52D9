from django.contrib import admin

# import model
from collection.models import Profile

# set up automated slug creation
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}


# register model
admin.site.register(Profile, ProfileAdmin)
