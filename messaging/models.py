from django.db import models

# Create your models here.
class CustomerQueue(models.Model):
    customerId = models.CharField(max_length=50, unique=True)
    customerName = models.CharField(max_length=255)
    jobType = models.IntegerField(choices=[(1, "Type 1"), (2, "Type 2")])
    customerPhone = models.CharField(max_length=15)
    queueTime = models.DateTimeField(auto_now_add=True)
    scheduledTime = models.DateTimeField()
    messageSent = models.BooleanField(default=False),
    responseReceived = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.customerName} - {self.customerPhone}"

class CustomerResponse(models.Model):
    customer = models.ForeignKey(CustomerQueue, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")])
    responseTime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Response from {self.customer.customer_name}: {self.rating}"