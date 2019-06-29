from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length = 255)
	publish_date = models.DateTimeField()
	image = models.ImageField(upload_to = 'images/')
	body = models.TextField()

	def summary(self):
		#return body from character 0 to 13 e.g Coding Article
		return self.body[:14]

	def only_date(self):
		#return only date not time.
		return self.publish_date.strftime('%b %e, %Y')


	#chnaging default name of object in admin panel
	def __str__(self):
		return self.title

