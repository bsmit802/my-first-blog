#from and import lines add bits from other files instead of copying them again
from django.conf import settings
from django.db import models
from django.utils import timezone


#class is a keyword that indicates that we are defining and object
# Post is the name of our model (no whitespace or special characters must be used)
#models.Model means that the Post is a Django mode, so Django knows that it should be saved in the database.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

 #publish method
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
