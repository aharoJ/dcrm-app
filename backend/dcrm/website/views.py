from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .froms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.


def home(request):
    records = Record.objects.all()

    # check to see if logging in
    if request.method == "POST":
        # attribute is what we passed in html `name="name_attribute"`
        username = request.POST["username"]
        password = request.POST["password"]

        # Authenticate
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully loged in!")
            return redirect("home")
        else:
            messages.error(
                request, "There was an error logging in, please try again..."
            )
            return redirect("home")
    else:
        return render(request, "home.html", {"records": records})


def login_user(request):
    pass
    # tutorial guy decided to not include auth here (come back and change this)


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect("home")


# Views is the controller here was we return is the response.VIEW
def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)

            login(request, user)
            messages.success(request, "You have sucessfuly register!")
            return redirect("home")
    else:
        form = SignUpForm()
        return render(request, "register.html", {"form": form})
    return render(request, "register.html", {"form": form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        # look up records
        customer_record = Record.objects.get(id=pk)
        return render(request, "record.html", {"customer_record": customer_record})
    else:
        messages.error(request, "You must be logged in to access this resource!")
        return redirect("home")

def delete_customer_record(request, pk):
    if request.user.is_authenticated:
        delete_customer= Record.objects.get(id=pk)
        delete_customer.delete()
        messages.success(request, "Account deleted :(")
        return redirect("home")
    else: 
        messages.error(request, "There was an error deleted your account. Please try again later...")
        return redirect("home")

def add_customer_record(request):
    form= AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method=="POST":
            if form.is_valid():
                add_record= form.save()
                messages.success(request, "Customer created!")
                return redirect("home")
        return render(request, "add_record.html", {"form": form})
    messages.error(request, "Please login...")
    return redirect("home")

def update_customer_record(request, pk):
    if request.user.is_authenticated:
        update_customer= Record.objects.get(id=pk)
        # -- instance= pulls the CURRENT user
        form= AddRecordForm(request.POST or None, instance=update_customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated profile sucessfully!")
            return redirect("home")
        # return render(request, "update_record.html", {"form" :form})
        # -- updated from above 
        return render(request, "update_record.html", {"form": form, "customer_record": update_customer})

    else:
        messages.error(request, "Please login...")
        return redirect("home")

