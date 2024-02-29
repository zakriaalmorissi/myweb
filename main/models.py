from django.db import models 
from django.contrib.auth.models import User, AbstractUser

# create models for personal data  
class Myprofile(models.Model):
    name = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name="Name")
    profile = models.ImageField(upload_to='private/images/',blank=True)
    bio = models.CharField(max_length=75)
    link = models.URLField(blank=True)
    link_2 = models.URLField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    class Meta: 
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f"{self.name}: {self.bio}"


class Introduction(models.Model):
    title =  models.CharField(max_length=20)
    text = models.TextField(max_length=10000)


# ====================================================================================================================================

# create a category model for categorizing the posts 
class Category(models.Model):
    name = models.CharField(max_length=50,verbose_name='Category name')


    class Meta :
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f"{self.name}"


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")
    title = models.CharField(max_length=200,default='', verbose_name="Title")
    text = models.TextField(max_length=10000, verbose_name="Text")
    image = models.ImageField(upload_to='images')
    text_2 = models.TextField(max_length=10000, blank=True, verbose_name="Second Text")
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='images/', blank=True, null=True)
    text_3 = models.TextField(max_length=10000, blank=True, verbose_name="Third Text")
    image_3 = models.ImageField(upload_to='images/', blank=True, null=True)
    video_2 = models.FileField(upload_to='videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At", db_index=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        indexes = [
            models.Index(fields=['created_at']),  # Add index for created_at field
        ]

    def __str__(self):
        return f"Post by {self.author.username} ({self.created_at})"
    

#=======================================================================================================================
    
# give the user the chance to make a profile
class UserProfile(models.Model):
    user_profile = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name='User profile')
    name = models.CharField(max_length=20, blank=True, null=True)
    bio = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='user_images',blank=True)


    class Meta:
        verbose_name = 'User profile'
        verbose_name_plural = 'User profiles'

    def __str__(self):
        return f'{self.user_profile.username}: {self.name} {self.bio}'
    


