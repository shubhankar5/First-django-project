from django.db import models
from django.contrib.auth.models import User
from datetime import date
from PIL import Image


class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	first_name=models.CharField(max_length=20,default='')
	last_name=models.CharField(max_length=20,default='')
	dob=models.DateField(default=date.today)

	def __str__(self):
		return f'{self.user.username} Profile'
		
	def save(self,*args,**kwargs):
		super(Profile,self).save(*args,**kwargs)

		img=Image.open(self.image.path)

		if img.height>300 or img.width>300:
			output_size=(300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)


class Address(models.Model):
    profile=models.OneToOneField(Profile,on_delete=models.CASCADE)
    city = models.CharField(max_length=60,default='')
    state = models.CharField(max_length=30,default='')
    country = models.CharField(max_length=50,default='')

    class Meta:
    	verbose_name = 'Address'
    	verbose_name_plural = 'Address'

    def __str__(self):
    	return f'{self.profile.user.username} Address'

    def save(self,*args,**kwargs):
    	super(Address,self).save(*args,**kwargs)
    	
