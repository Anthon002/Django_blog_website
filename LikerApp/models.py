from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    add_time=models.DateTimeField(auto_now_add=True,null=True)
    profile_pic=models.ImageField(null=True,blank=True,upload_to='static/images',default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.nicepng.com%2Fourpic%2Fu2y3a9e6t4o0a9w7_profile-picture-default-png%2F&psig=AOvVaw0XZJRgHSQbfq2A0dfOcEzm&ust=1677998456366000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCKDf9b_Vwf0CFQAAAAAdAAAAABAE')
    
    def __str__(self):
        return str(self.user)

def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        
post_save.connect(create_profile,sender=User)

def update_profile(sender,instance,created,**kwargs):
    if created == False:
        instance.profile.save()
post_save.connect(update_profile,sender=User)


class Post(models.Model):
    TAG_CHOICES = (
    ("Blogging", "Blogging"),
    ("Writing", "Writing"),
    ("Tips", "Tips"),
    ("How-to", "How-to"),
    ("Reviews", "Reviews"),
    ("News", "News"),
    ("Trends", "Trends"),
    ("Opinion", "Opinion"),
    ("Personal", "Personal"),
    ("Stories", "Stories"),
    ("Humor", "Humor"),
    ("Inspiration", "Inspiration"),
    ("Education", "Education"),
    ("Entertainment", "Entertainment"),
    ("Lifestyle", "Lifestyle"),
    ("Health", "Health"),
    ("Fitness", "Fitness"),
    ("Food", "Food"),
    ("Fashion", "Fashion"),
    ("Beauty", "Beauty"),
    )
    profile=models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True,related_name='profile')
    title=models.CharField(max_length=200,null=True)
    content=models.TextField(max_length=1500,null=True)
    liked=models.ManyToManyField(User,default=None, blank=True, related_name='liked')
    tag=models.CharField(choices=TAG_CHOICES,max_length=200,default=False,null=True)
    
    def __str__(self):
        return str(self.title)
    
    @property
    def num_likes(self):
        return self.liked.all().count()
    
  
class Like(models.Model):
    LIKE_CHOICES = (
        ('Like','Like'),
        ('Unlike','Unlike')
    )
    user=models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    post=models.ForeignKey(Post,on_delete=models.SET_NULL, null=True)
    value = models.CharField(choices=LIKE_CHOICES, default=True, max_length=10)
    
    def __str__(self):
        return str(self.post)

class Comment(models.Model):
    Profile=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    post=models.ForeignKey(Post,on_delete=models.SET_NULL,null=True)
    content=models.TextField( null=True )