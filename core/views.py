from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .models import Student, Teacher
from .utils import generate_jwt
import jwt
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from .models import Event
from .models import Review, Student
from .forms import ReviewForm
from django.utils.timezone import now


def Main(request):
    return render(request,"main.html")

def Home(request):
    reviews = Review.objects.all().order_by('-created_at')  # Fetch latest reviews
    return render(request, "index.html", {"reviews": reviews})

# Student Signup
def student_signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        age = request.POST.get("age")  
        branch = request.POST.get("branch")  

        if Student.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect("student_signup")

        student = Student(username=username, email=email, age=age, branch=branch)
        student.set_password(password)
        student.save()
        messages.success(request, "Account created! Please login.")
        return redirect("student_login")

    return render(request, "student_signup.html")


def student_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            student = Student.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request, "User not found!")
            return redirect("student_login")

        if not student.check_password(password):
            messages.error(request, "Incorrect password!")
            return redirect("student_login")

        token = generate_jwt(student)
        response = redirect("student_profile")
        response.set_cookie("jwt", token, httponly=True, max_age=900)  
        return response

    return render(request, "student_login.html")

# Teacher Signup
def teacher_signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if Teacher.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect("teacher_signup")

        teacher = Teacher(username=username, email=email)
        teacher.set_password(password)
        teacher.save()
        messages.success(request, "Account created! Please login.")
        return redirect("teacher_login")

    return render(request, "teacher_signup.html")

# Teacher Login
def teacher_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            teacher = Teacher.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request, "User not found!")
            return redirect("teacher_login")

        if not teacher.check_password(password):
            messages.error(request, "Incorrect password!")
            return redirect("teacher_login")

        token = generate_jwt(teacher)
        response = redirect("home")
        response.set_cookie("jwt", token, httponly=True, max_age=900)  # 15 min expiry
        return response

    return render(request, "teacher_login.html")

# Logout
def logout_view(request):
    response = redirect("home")
    response.delete_cookie("jwt")
    return response
    
# Student profile
def student_profile(request):
    token = request.COOKIES.get("jwt")

    if not token:
        messages.error(request, "You must be logged in to view this page!")
        return redirect("home")

    try:
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        student_id = decoded_token.get("id")
        student = Student.objects.get(id=student_id)

        # Fetch upcoming events
        upcoming_events = Event.objects.filter(date__gte=now()).order_by("date")

    except (jwt.ExpiredSignatureError, jwt.DecodeError, ObjectDoesNotExist):
        messages.error(request, "Invalid or expired session! Please log in again.")
        return redirect("student_login")

    return render(request, "student_profile.html", {"student": student, "upcoming_events": upcoming_events})

def campus_map(request):
    return render(request, 'map.html')

def event_list(request):
    upcoming_events = Event.objects.filter(date__gte=now()).order_by("date")
    past_events = Event.objects.filter(date__lt=now()).order_by("-date")
    return render(request, "events.html", {"upcoming_events": upcoming_events, "past_events": past_events})

@login_required
def submit_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.student = Student.objects.get(username=request.user.username)
            review.save()
            return redirect("home")
    else:
        form = ReviewForm()
    return render(request, "submit_review.html", {"form": form})

def kjc_view(request):
    return render(request,"kjc.html")

def mvj_view(request):
    return render(request,"MVJ.html")

def about(request):
    return render(request,"about.html")

def school(request):
    return render(request,"school.html")

def hostel(request):
    return render(request,"hostel.html")

def leadership(request):
    return render(request,"leadership.html")

def school_arch(request):
    return render(request,"school_arch.html")

def school_eco(request):
    return render(request,"school_eco.html")

def school_eng(request):
    return render(request,"school_eng.html")

def school_legal(request):
    return render(request,"school_legal.html")

def school_libral(request):
    return render(request,"school_libral.html")

def school_mgnt(request):
    return render(request,"school_mgnt.html")

def school_sscs(request):
    return render(request,"school_sscs.html")