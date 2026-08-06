from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile, Plant, MyPlant, Profile, DiseaseInfo, ScanHistory, Contact
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.conf import settings
from ai_model.predictor import predict_disease
import requests
from django.core.files.storage import FileSystemStorage
import re
from difflib import get_close_matches


def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def features(request):
    return render(request, 'features.html')

def contacts(request):

    if request.method == "POST":

        Contact.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )

        messages.success(request, "Your message has been sent successfully!")

        return redirect("contacts")

    return render(request, "contacts.html")

@login_required(login_url="login")
def dashboard(request):

    myplant_count = MyPlant.objects.filter(user=request.user).count()
    scan_count = ScanHistory.objects.filter(user=request.user).count()

    profile, created = Profile.objects.get_or_create(user=request.user)

    recent_scans = ScanHistory.objects.filter(
        user=request.user
    ).order_by("-scanned_at")

    context = {
        "myplant_count": myplant_count,
        "scan_count": scan_count,
        "profile": profile,
        "recent_scans": recent_scans,
    }

    return render(request, "dashboard.html", context)

@login_required(login_url="login")
def diseases(request):

    myplants = MyPlant.objects.filter(user=request.user)
    saved_plants = [item.plant.id for item in myplants]

    return render(request, "diseases.html", {
        "saved_plants": saved_plants
    })

def neem(request):
    return render(request, "neem.html")

def tomato(request):
    return render(request, "tomato.html")

def sunflower(request):
    return render(request, "sunflower.html")

def rose(request):
    return render(request, "rose.html")

def papaya(request):
    return render(request, "papaya.html")

def mango(request):
    return render(request, "mango.html")

def lotus(request):
    return render(request, "lotus.html")

def hibiscus(request):
    return render(request, "hibiscus.html")

def haldi(request):
    return render(request, "haldi.html")

def guava(request):
    return render(request, "guava.html")

def coconut(request):
    return render(request, "coconut.html")

def banyan(request):
    return render(request, "banyan.html")

def banana(request):
    return render(request, "banana.html")

def ashoka(request):
    return render(request, "ashoka.html")

def aloe_vera(request):
    return render(request, "aloe_vera.html")

def register(request):

    if request.method == "POST":

        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect("register")

        username = email.split("@")[0]

        # Make username unique
        if User.objects.filter(username=username).exists():
            count = 1
            while User.objects.filter(username=f"{username}{count}").exists():
                count += 1
            username = f"{username}{count}"

        user = User.objects.create_user(
            username=username,
            first_name=full_name,
            email=email,
            password=password
        )

        UserProfile.objects.create(
            user=user,
            phone=phone
        )

        messages.success(request, "Registration successful. Please login.")
        return redirect("login")

    return render(request, "register.html")

def login(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Invalid email or password.")
            return redirect("login")

        user = authenticate(
            request,
            username=user_obj.username,
            password=password
        )

        if user is not None:
            auth_login(request, user)
            return redirect("dashboard")

        messages.error(request, "Invalid email or password.")

    return render(request, "login.html")



def logout_user(request):
    logout(request)
    return redirect("login")

def scanplant(request):

    disease_name = ""
    disease_info = None
    api_data = None
    message = ""
    
    uploaded_image = None

    if request.method == "POST":


        # Manual Search
        if request.POST.get("search_disease"):

           disease_name = request.POST.get("search_disease").strip()

           search_name = (
                disease_name.lower()
               .replace(" ", "_")
               .replace("-", "_")
         )

        # AI Detection
        elif request.FILES.get("plant_image"):

            image = request.FILES.get("plant_image")

            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            uploaded_image = fs.url(filename)
            image_path_db = filename

            print("Image:", image)

            image_path = "temp_image.jpg"

            with open(image_path, "wb+") as destination:
                for chunk in image.chunks():
                    destination.write(chunk)


            disease_name, confidence = predict_disease(image_path)
            if confidence < 50:
                messages.warning(
                    request,
                    "⚠️ Sorry! This AI currently supports only Tomato, Potato, and Pepper plant diseases. Please upload a supported plant image."
                 )
                return redirect("scanplant")
                print("Confidence:", confidence)
            plant_name = disease_name.split("_")[0]

            print("Detected Disease:", disease_name)



        # 1) Check Local Database First

        try:

            disease_info = DiseaseInfo.objects.get(

            disease_name__iexact=disease_name.replace(" ", "_")
            )

            print("Disease found in database")


        except DiseaseInfo.DoesNotExist:


            # 2) Check Perenual API

            url = "https://perenual.com/api/pest-disease-list"


            params = {
                "key": settings.PERENUAL_API_KEY,
                "q": disease_name
            }


            response = requests.get(
                url,
                params=params
            )


            api_data = response.json()

            print("Perenual Response:", api_data)



            # 3) If API also has no data

            if not api_data.get("data"):

                message = "Disease information is not available yet."

            
        if request.user.is_authenticated and uploaded_image:
        
                           ScanHistory.objects.create(
                               user=request.user,
                               plant_name=plant_name,
                               disease_name=disease_name,
                               image=image_path_db
                           )
        return render(request, "result.html", {

            "disease_name": disease_name,
            "disease_info": disease_info,
            "api_data": api_data,
            "message": message,
            "uploaded_image": uploaded_image,

        })


    return render(request, "scanplant.html")

@login_required(login_url="login")
def myplants(request):

    myplants = MyPlant.objects.filter(user=request.user)

    return render(request, "myplants.html", {
        "myplants": myplants
    })

from django.shortcuts import get_object_or_404

@login_required(login_url="login")
def add_myplant(request, plant_id):

    plant = get_object_or_404(Plant, id=plant_id)

    MyPlant.objects.get_or_create(
        user=request.user,
        plant=plant
    )

    return redirect("myplants")

@login_required(login_url="login")
def delete_myplant(request, plant_id):

    MyPlant.objects.filter(
        user=request.user,
        plant_id=plant_id
    ).delete()

    return redirect("myplants")

@login_required(login_url="login")
def profile(request):

    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":

        request.user.first_name = request.POST.get("name")
        request.user.email = request.POST.get("email")
        request.user.save()

        if "delete_photo" in request.POST:
            if profile.photo:
                profile.photo.delete(save=False)
                profile.photo = None

        elif request.FILES.get("photo"):
            profile.photo = request.FILES["photo"]

        profile.save()

        return redirect("profile")

    return render(request, "profile.html", {
        "profile": profile
    })

def result(request):

    return render(request, "result.html", {
        "disease_name": "",
        "disease_info": None,
        "api_data": None,
        "message": ""
    })


# Create your views here.
