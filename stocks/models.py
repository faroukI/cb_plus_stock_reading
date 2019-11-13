from django.db import models

class Stock_reading(models.Model):
  product_id  = models.CharField(max_length=13)
  expiry_date = models.DateField()
  ts          = models.DateTimeField() 
  quantity    = models.IntegerField()


  def __str__(self):
    return 'id : ' + self.product_id + ' - quantity : ' + str(self.quantity) + ' - expiry date : ' + str(self.expiry_date)

  def stock_id(self):
    return self.__str__()
