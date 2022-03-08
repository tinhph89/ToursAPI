from django.db import models

# Create your models here.
class Tours(models.Model):
    dia_diem = models.CharField(max_length=250)
    thanh_pho = models.CharField(max_length=200)
    khach_san = models.TextField(max_length=200,blank=True)
    nha_hang = models.TextField(max_length=200,blank=True)
    quan_an = models.TextField(max_length=200,blank=True)
    giai_tri = models.TextField(max_length=200,blank=True)
    ghi_chu = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return self.dia_diem
