from django.contrib import admin
from django.utils.html import mark_safe
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User



admin.site.register(Category)


""""
customize the models display in the admin panel

"""

class CustomUserDisplay(UserAdmin):
    list_display = ["id","username","first_name","email","is_staff","date_joined"]


# reregister the user with its Custom display 
admin.site.unregister(User)
admin.site.register(User,CustomUserDisplay)



class ShowProfile(admin.ModelAdmin):
    list_display = ['id','name','profile_tag','bio','link','link_2','phone_number']

    # display the profile image 
    def profile_tag(self, object):
        return mark_safe('<img src="{}" width="100" height="100"></img>'.format(object.profile.url))
    
    # provide a custom name for the profile in the admin panel
    profile_tag.short_description = 'My profile'

admin.site.register(Myprofile,ShowProfile)


class ShowIntroduction(admin.ModelAdmin):
    list_display = ["id", "category", "title", "text"]


admin.site.register(Introduction, ShowIntroduction)


class ShowPost(admin.ModelAdmin):
    list_display = ['category', 'author', 'title', 'video_tag','text', 'image_tag', 
                    'text_2', 'image_2_tag', 'text_3', 'image_3_tag', 
                    'video_2', 'created_at', 'updated_at' ]

    # display videos
    def video_tag(self, object):
        if object.video:
            return mark_safe('<video width="320" height="240" controls> <source src="{}" type="video/mp4" </source> </video>'.format(object.video.url))   

        return "-"
    
    def video_2_tag(self, object):
        if object.video_2:
            return mark_safe('<video width="320" height="240" controls> <source src="{}" type="video/mp4" </source> </video>'.format(object.video_2.url))   

        return "-"
    
    
    # display images 
    def image_tag(self, obj):
        return mark_safe('<img src="{}" width="100" height="100"></img>'.format(obj.image.url))
    
    def image_2_tag(self, obj):
        if obj.image_2:
            return mark_safe('<img src="{}" width="100" height="100"></img>'.format(obj.image_2.url))
        
        else:
            return '-'
        
    def image_3_tag(self, obj):
        if obj.image_3:
           return mark_safe('<img src="{}" width="100" height="100"></img>'.format(obj.image_3.url))
        
        else:
            return '-'
        
    video_tag.short_description = "First Video"
    video_2_tag.short_description = "Second Video"
    image_tag.short_description = " Image 1"
    image_2_tag.short_description = "Image 2"
    image_3_tag.short_description = "Image 3"
    
admin.site.register(Post, ShowPost)

       


