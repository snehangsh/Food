#blueprint to create table, like name, fields, datatype etc
#model is crated using a class

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.item_name
    user_name = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.explicit.bing.net%2Fth%3Fid%3DOIP.CAXQe3AgWFel1hIzxDZ6owEsDg%26pid%3DApi&f=1&ipt=48b7246ba67049a87fdd1474a4e493a8896e496d699eb31f64f8e5b9fef84833&ipo=images")

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk":self.pk})



#https://www.gettyimages.in/detail/photo/cheese-burger-with-bacon-on-black-dark-background-royalty-free-image/1295796231

#https://www.gettyimages.in/detail/photo/french-fries-royalty-free-image/88184007

#https://www.gettyimages.in/detail/photo/pineapple-papaya-smoothie-royalty-free-image/86056886

#kwargs: keyword arguments