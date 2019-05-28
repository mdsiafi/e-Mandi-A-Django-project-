from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.urls import reverse
import datetime
# Create your models here.
# class Author(models.Model):
#     author_id = models.AutoField(primary_key=True)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=40)
#     email = models.EmailField()
#     age=models.IntegerField()
#
#     class Meta:
#     db_table=u'Author'
#
#     def __unicode__(self):
#         return u"%d %s %s %s %d" % (self.pk, self.first_name, self.last_name, self.email,self.age)


class UserModel(models.Model):
    f_name = models.CharField(max_length=254)
    l_name = models.CharField(max_length=254)
    mobile = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    type = models.CharField(max_length=254,choices=(('customer','Customer'),('farmer','Farmer')) )
    password = models.CharField(max_length=254)
    address = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    gender = models.CharField(max_length=254)
    dob = models.DateField()

    def __str__(self):
        return "FirstName:  {0}\nLastName:   {1}\nEmail:   {2}".format(self.f_name, self.l_name, self.email)
    def get_absolute_url(self):
        return reverse('efarm:welcome', args=[self.id])



class CropCategory(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('efarm:crop_list_by_category', args=[self.slug])



class Crop(models.Model):
    farmer_id= models.IntegerField()
    crop_name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=100, db_index=True)
    category = models.ForeignKey(CropCategory, related_name='crops', on_delete=models.CASCADE)
    crop_description = models.CharField(max_length=254)
    crop_image = models.ImageField(upload_to='crop_image')
    crop_thumbnail = ImageSpecField(source='crop_image',
                                      processors=[ResizeToFill(100, 50)],
                                      format='JPEG',
                                      options={'quality': 60})
    location = models.CharField(max_length=100)
    contact_no = models.IntegerField()
    zip_code = models.CharField(max_length=20)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    now = models.DateTimeField(auto_now_add=True, blank=True)
    exp = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=0)
    class meta:
        ordering = ('crop_name', )
        index_together = (('id', 'slug'),)
        
    
    
    def __str__(self):
        return "{0}".format(self.crop_name)

    def get_absolute_url(self):
        return reverse('efarm:crop_detail', args=[self.id, self.slug])
    

class feedback(models.Model):
    cust_name=models.CharField(max_length=254)
    cust_email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=50)
    cust_msg = models.TextField(max_length=254)
    def __str__(self):
        return self.subject