from django.db import models


class Bank(models.Model):
    id=models.DecimalField(max_digits=50)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return "{}".format(self.name)


class Branch(models.Model):
    ifsc = models.CharField(max_length=500, unique=True)
    bank_id = models.ForeignKey(Bank, on_delete=models.PROTECT)
    branch = models.CharField(max_length=256)
    address = models.TextField()
    city = models.CharField(max_length=500)
    district = models.CharField(max_length=500)
    state = models.CharField(max_length=500)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Branch'
        verbose_name_plural = 'Branch'

    def __str__(self):
        return "{} - {} - {}".format(self.name, self.city, self.bank)