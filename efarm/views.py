from django.shortcuts import render
from django.http import *
from . import models
from . import forms
from django.urls import reverse
from .models import UserModel
# Create your views here.
#def index(request):
#    return render(request, "e Mandi.html")

def team(request):
    return render(request,"teams.html")

def signup(request):
    if request.method == "POST":
        signup_user = forms.SignupForm(request.POST)
        print("-------------------------------------------")
        if signup_user.is_valid():
            
            signup_user.save()
            return HttpResponseRedirect(reverse("efarm:login"))
            # msg = "Enter Valid Details"
    # return HttpResponse("Hii")
    signup_form = forms.SignupForm()
    return render(request, "signup.html",{'signup_form':signup_form})

def login(request):
    msg=""
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = models.UserModel.objects.get(email = email,password =password)
            print(user.id)
            print(user.type)
            if (user.type=="farmer"):
                type(user.id)
                #id=user.id
                print(id)
                user.UserModel.get_absolute_url
                #return reverse('efarm:welcome', args=[self.id])
            elif (user.type == "customer"):
                return HttpResponseRedirect('welcome/customer')
        except models.UserModel.DoesNotExist:
            msg = "Enter Valid Details"
    return render(request, "login.html",{'msg':msg})

from django.shortcuts import get_list_or_404, get_object_or_404
def welcomeFarmer(request,k):
    #crops = models.Crop.objects.get(farmer_id=k)
    #category1 = get_object_or_404(models.Crop, farmer_id=k)
    crops = Crop.objects.filter(farmer_id=k)
    return render(request, "farmer/welcome.html", {'crops': crops})

#def welcomeCustomer(request):
    #crops = models.Crop.objects.all()
    #return render(request, "customer/welcome.html", {'crops': crops})

def addCrop(request):
    add_crop_form = forms.CropForm()
    if request.method =="POST":
        form = forms.CropForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('-------------done-------------')
        else:
            print('-------------not done-------------')
    return render(request, "farmer/addCrop.html", {'add_crop':add_crop_form})


def cropDelete(request, object_id):
    object = get_object_or_404(models.Crop, pk=object_id)
    object.delete()
    return HttpResponseRedirect(reverse("efarm:welcome_farmer"))



from django.views.generic import UpdateView
from .models import Crop
from .forms import CropForm
class EditCrop(UpdateView): #Note that we are using UpdateView and not FormView
    model = Crop
    form_class = CropForm
    template_name = "farmer/editCrop.html"
    #
    # def get_object(self, *args, **kwargs):
    #     user = get_object_or_404(Crop, pk=self.kwargs['pk'])
    #
    #     # We can also get user object using self.request.user  but that doesnt work
    #     # for other models.
    #
    #     return user.userprofile

    def get_success_url(self, *args, **kwargs):
        return reverse("efarm:welcome_farmer")

def welcomeCustomer(request, category_slug=None):
    category = None
    categories = models.CropCategory.objects.all()
    crops = Crop.objects.all()
    if category_slug:
        category = get_object_or_404(models.CropCategory, slug=category_slug)
        crops = Crop.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'crops': crops
    }
    return render(request, 'customer/list.html', context)

from cart.forms import CartAddProductForm

def crop_detail(request, id, slug):
    crop = get_object_or_404(models.Crop, id=id, slug=slug)
    cart_product_form = CartAddProductForm()
    context = {
        'crop': crop,
        'cart_product_form': cart_product_form
    }
    return render(request,"customer/detail.html", context)

def index(request):
    if request.method == "POST":
        feedback_form = forms.feedbackform(request.POST)
        print("-------------------------------------------")
        if feedback_form.is_valid():
            
            feedback_form.save()
            return HttpResponseRedirect(reverse("efarm:index"))
            # msg = "Enter Valid Details"
    # return HttpResponse("Hii")
    feedback_form = forms.feedbackform()
    return render(request, "e Mandi.html",{'feedback_form':feedback_form})