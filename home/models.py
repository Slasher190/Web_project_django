from django.db import models

# Create your models here.
#this is what which defines databases
#https://docs.djangoproject.com/en/3.0/ref/models/fields/
class Contact(models.Model):
    #put here those things which is used in contact us profile
    name = models.CharField(max_length = 122)
    email = models.CharField(max_length = 122)
    phone = models.CharField(max_length = 12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name


#python manage.py makemigrations {
#           !1 = register model in model.py and then
#            !2 = register app in settings}

#1:52:11  database 

# to save in database
# run command 