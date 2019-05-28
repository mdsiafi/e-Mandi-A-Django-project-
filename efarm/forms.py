from django import forms
from django.forms import ModelForm
from efarm.models import UserModel, Crop,feedback
from bootstrap_datepicker_plus import DatePickerInput

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#
# class SignUpForm2(UserCreationForm):
#     first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
#     mobile = models.CharField(max_length=254)
#     type = models.CharField(max_length=254,choices=(('customer','Customer'),('farmer','Farmer')) )
#     address = models.CharField(max_length=100)
#     zip_code = models.CharField(max_length=20)
#     state = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)
#     gender = models.CharField(max_length=254,choices=(('male','Male'),('female','Female')) )
#     dob = models.DateField()
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(max_length=500, blank=True)
#     location = models.CharField(max_length=30, blank=True)
#     birth_date = models.DateField(null=True, blank=True)
#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
#     mobile = models.CharField(max_length=254)
    #     type = models.CharField(max_length=254,choices=(('customer','Customer'),('farmer','Farmer')) )
    #     address = models.CharField(max_length=100)
    #     zip_code = models.CharField(max_length=20)
    #     state = models.CharField(max_length=100)
    #     country = models.CharField(max_length=100)
    #     gender = models.CharField(max_length=254,choices=(('male','Male'),('female','Female')) )
    #     dob = models.DateField()

class SignupForm(ModelForm):
    f_name = forms.CharField(widget=forms.TextInput(attrs={'class':'input--style-4','placeholder':'Enter First Name'}), required=True ,max_length = 20)
    l_name = forms.CharField(widget=forms.TextInput(attrs={'class':'input--style-4','placeholder':'Enter Lastname Name'}), required=True ,max_length = 20)
    mobile = forms.CharField(widget=forms.NumberInput(attrs={'class':'input--style-4','placeholder':'Enter Mobile No'}), required=True , max_length=12)
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'input--style-4','placeholder':'Enter Valid Email'}), required=True ,max_length = 30)
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'input--style-4','placeholder':'Enter Valid Address'}), required=True ,max_length = 30)
    zip_code = forms.CharField(widget=forms.NumberInput(attrs={'class':'input--style-4','placeholder':'Enter Zip Code'}), required=True ,max_length = 30)
    state = forms.CharField(widget=forms.TextInput(attrs={'class':'input--style-4','placeholder':'Enter Valid State'}), required=True ,max_length = 30)
    country = forms.CharField(widget=forms.TextInput(attrs={'class':'input--style-4','placeholder':'Enter Valid Country'}), required=True ,max_length = 30)
    dob = forms.DateField(widget=forms.DateInput(attrs={'class':'input--style-4','type': 'date'}),required=True)
    type = forms.ChoiceField(widget=forms.Select(attrs={'class':'input--style-4'}),choices=(('customer','Customer'),('farmer','Farmer')),required=True)
    gender = forms.ChoiceField(widget=forms.Select(attrs={'class':''}),choices=(('male','Male'),('female','Female')),required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input--style-4','placeholder':'Enter Password'}), required=True , max_length=12)
    class Meta:
        model = UserModel
        fields=['f_name','l_name','dob','gender','mobile','type','password','address','zip_code','state','country','email']


class CropForm(ModelForm):
    # crop_name = forms.CharField(widget=forms.TextInput(attrs={'class':'input--style-4','placeholder':'Enter Full Name'}), required=True ,max_length = 20)
    # crop_description = forms.CharField(widget=forms.TextInput(attrs={'class':'input--style-4','placeholder':'Enter Full Name'}), required=True ,max_length = 20)
    # crop_image = forms.ImageField(widget=forms.(attrs={'class':'input--style-4','placeholder':'Enter Full Name'}), required=True ,max_length = 20)
    # crop_thumbnail = ImageSpecField(source='avatar',
    #                                   processors=[ResizeToFill(100, 50)],
    #                                   format='JPEG',
    #                                   options={'quality': 60})
    # location = models.CharField(max_length=100)
    # contact_no = models.IntegerField(default=0)
    # zip_code = models.CharField(max_length=20)
    # state = models.CharField(max_length=100)
    # country = models.CharField(max_length=100)
    # gender = models.CharField(max_length=254)
    # now = models.DateTimeField()
    # exp = models.DateTimeField()
    # price = models.FloatField(default=0.0)
    # quantity = models.IntegerField(default=0)
    #
    # f_name = forms.CharField(widget=forms.TextInput(attrs={'class':'input--style-4','placeholder':'Enter Full Name'}), required=True ,max_length = 20)
    # l_name = forms.CharField(widget=forms.TextInput(attrs={'class':'input--style-4','placeholder':'Enter Full Name'}), required=True ,max_length = 20)
    # mobile = forms.CharField(widget=forms.NumberInput(attrs={'class':'input--style-4','placeholder':'Enter AKTU University Rollno'}), required=True , max_length=12)
    # email = forms.CharField(widget=forms.TextInput(attrs={'class':'input--style-4','placeholder':'Enter Valid Email'}), required=True ,max_length = 30)
    # address = forms.CharField(widget=forms.TextInput(attrs={'class':'input--style-4','placeholder':'Enter Valid Email'}), required=True ,max_length = 30)
    # zip_code = forms.CharField(widget=forms.NumberInput(attrs={'class':'input--style-4','placeholder':'Enter Valid Email'}), required=True ,max_length = 30)
    # state = forms.CharField(widget=forms.TextInput(attrs={'class':'input--style-4','placeholder':'Enter Valid Email'}), required=True ,max_length = 30)
    # country = forms.CharField(widget=forms.TextInput(attrs={'class':'input--style-4','placeholder':'Enter Valid Email'}), required=True ,max_length = 30)
    # dob = forms.DateField(widget=forms.DateInput(attrs={'class':'input--style-4','type': 'date'}),required=True)
    # type = forms.ChoiceField(widget=forms.Select(attrs={'class':'input--style-4'}),choices=(('customer','Customer'),('farmer','Farmer')),required=True)
    # gender = forms.ChoiceField(widget=forms.Select(attrs={'class':'rs-select2 js-select-simple select--no-search'}),choices=(('male','Male'),('female','Female')),required=True)

    class Meta:
        model = Crop
        fields=['farmer_id','crop_name','slug','category','crop_description','crop_image','location','location','contact_no', 'zip_code' , 'state' , 'country'  , 'price' ,'quantity' ]
        # widgets = {'exp': DateInput(attrs={'type': 'date'}),}



class feedbackform(ModelForm):
    cust_name = forms.CharField(widget=forms.TextInput(attrs={'class':'input--style-4','placeholder':'Enter Your Name'}), required=True ,max_length = 20)
    cust_email = forms.CharField(widget=forms.TextInput(attrs={'class':'input--style-4','placeholder':'Enter your Email'}), required=True ,max_length = 20)
    subject = forms.CharField(widget=forms.TextInput(attrs={'class':'input--style-4','placeholder':'Enter Subject'}), required=True , max_length=12)
    cust_msg = forms.CharField(widget=forms.TextInput(attrs={'class':'input--style-4','placeholder':'Enter your message'}), required=True ,max_length = 30)
    class Meta:
        model = feedback
        fields=['cust_name','cust_email','subject','cust_msg']