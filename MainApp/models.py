from django.db import models

# Create your models here.

class pizza(models.Model):
    pizza_name = models.CharField(max_length=20)
    def __str__(self):
        return self.pizza_name

class Toppings(models.Model):
    pizza = models.ForeignKey(pizza, on_delete=models.CASCADE)
    topping_name = models.CharField(max_length=15)
    def __str__(self):
        return self.topping_name

class Comment(models.Model):
    pizza = models.ForeignKey(pizza, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text

