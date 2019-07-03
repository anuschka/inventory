from django.db import models
from datetime import date
from django.core.exceptions import ValidationError
from django.db import transaction


# Products have a name and a manufacturer
# Manufacturer could be a table of suppliers.
class Product(models.Model):
    name = models.CharField(max_length=64)
    manufacturer = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name} from {self.manufacturer}"

# Batch always belongs to exactly one product. 
# It represents a set of items of one product, where all items were produced and delivered together (as a single batch). 
# All items in the batch will have the same production date and expire date for example.
class Batch(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_in_batch")
    units = models.IntegerField()
    date_produced = models.DateField()
    expiry_date = models.DateField()
    total = models.IntegerField(blank=True, editable=False)

    #overwrite save method
    def save(self, *args, **kwargs):
        if not self.id:
            # if object is a new instance set total to number of units
            self.total=self.units
            super(Batch, self).save(*args, **kwargs)
        else:
            super(Batch, self).save(*args, **kwargs)
                    

    @property
    def freshness(self):
        # returns the freshness of the food in the warehouse
        # food that is less then 3 days from expiry date is considered expiring
        if (date.today() - self.expiry_date).days >0:
            return "expired"
        elif (self.expiry_date - date.today()).days <=3:
            return "expiring"
        else:
            return "fresh"

    def __str__(self):
        return f"{self.id} - {self.product} - expiry {self.expiry_date}"

# Keeps track of outgoing orders
class Order(models.Model):
    order_date = models.DateField()
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name="batch_in_order")
    units = models.IntegerField()
    company = models.CharField(max_length=64)

    #overwrite save method
    def save(self, *args, **kwargs):

        if not self.id:
            # if object is a new instance and number of units ordered are less then the total number of units in the batch
            # update the total number of units in the batch and save the order
            if self.units < self.batch.total:
                self.batch.total -= self.units
                self.batch.save()
                super(Order, self).save(*args, **kwargs)
            else:
                #do not save the order
                return
              
        
    def __str__(self):
        return f"{self.order_date} - {self.units} from {self.batch}"