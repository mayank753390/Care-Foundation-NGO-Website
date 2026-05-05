from django.db import models

class Activity(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='activities/', blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return self.title

class Donation(models.Model):
    citizenship = models.CharField(max_length=50)
    frequency = models.CharField(max_length=50)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"₹{self.amount} - {self.frequency} ({self.citizenship})"
