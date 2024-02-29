from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import random
from .utils import *
from django.shortcuts import render, get_object_or_404


def login(request):
    if 'username' in request.session:
        return redirect('index')  # Redirect to index if user is already logged in

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            try:
                user = People.objects.get(username=username, password=password)
                request.session['username'] = user.username
                return redirect('index')
            except People.DoesNotExist:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please provide both username and password.')
    
    return redirect('index')  # Redirect to index in case of GET request or login failure

def logout(request):
    if "username" in request.session:
        del request.session['username']
    return redirect('index')

def add_person(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        dob = request.POST.get('dob')
        date_of_joining = request.POST.get('doj')
        address = request.POST.get('address')
        person_type = request.POST.get('person_type')  

        new_person = People(username=username, password=password, dob=dob, date_of_joining=date_of_joining, address=address)
        new_person.save()

        if person_type == 'teacher':
            compensation = request.POST.get('compensation')
            compensation = int(compensation)
            teacher = Teacher(person=new_person, compensation=compensation)
            teacher.save()
        elif person_type == 'student':
            roll_number = request.POST.get('roll_number')
            roll_number = int(roll_number)
            student = Student(person=new_person, roll_number=roll_number)
            student.save()

        messages.success(request, 'Person added successfully!')
        return redirect('index')  

    return render(request, 'institute_app/add_person.html')

def student_detail_view(request):
    student = Student.objects.all()
    if student.exists():
        students = student.all()
        return render(request, 'institute_app/student_detail.html', {'students': students})
    else:
        return render(request, 'institute_app/index.html')

def teacher_detail_view(request):
    teacher = Teacher.objects.all()
    if teacher.exists():
        teachers = Teacher.objects.all()
        return render(request, 'institute_app/teacher_detail.html', {'teachers': teachers})
    else:
        return render(request, 'institute_app/index.html')
    
def club_detail_view(request):
    if request.method == 'POST':
        club_name = request.POST.get('club_name')
        new_club = Club.objects.create(club_name=club_name,)
        return redirect('club_detail')  # Redirect to the same page after adding a new club
    clubs = Club.objects.all()
    return render(request, 'institute_app/club_detail.html', {'clubs': clubs})
    
def book_detail_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        new_book = Book.objects.create(title=title,author=author)
        return redirect('book_detail')  # Redirect to the same page after adding a new club
    books = Book.objects.all()
    return render(request, 'institute_app/book_detail.html', {'books': books})
    
def index(request):
    if 'username' in request.session:
        # User is logged in, render home page
        username = request.session['username']
        try:
            user = People.objects.get(username=username)
            student_count = Student.objects.count() 
            teacher_count = Teacher.objects.count() 
            club_count = Club.objects.count() 
            book_count = Book.objects.count() 
            context = {"user": user,
                       "student_count":student_count,
                       "teacher_count":teacher_count,
                       "club_count":club_count,
                       "book_count":book_count
                       }
            return render(request, 'institute_app/index.html', context)
        except People.DoesNotExist:
            # If session username doesn't match any user, clear the session and render login
            del request.session['username']
    # User is not logged in, render login page
    return render(request, "institute_app/login.html")

def forgotpassword(request):
   if request.POST:
      try:
         user=People.objects.get(email=request.POST.get('email'))
         print("==========>>>> User",user)
         
         # ---------- step-2: Verify the otp -----------
         otp=request.POST.get('otp')
         print("==========>>>> OTP",otp)
         if otp is not None:
            # on correct OTP send to changepassword html
            if otp==user.otp and otp!="":
               return render(request, 'institute_app/changepassword.html',{'email':user.email})
            else:
            # on incorrect OTP
               msg="Incorrect OTP"
               return render(request, 'institute_app/forgotpassword.html',{'isOTP':True,'email':user.email,'msg':msg})
         # ----------------------------------------------
         
         # --------- step-1: otp ---------------   
         # generating otp
         user.otp=random.randint(1111,9999)
         user.save()
         
         # sending otp to the user through the mail
         mymailfunction("Forgot Password",'mailtemplate',user.email,{'email':user.email,'password':user.otp})
         # on valid email the OTP field will be unlocked
         return render(request, 'institute_app/forgotpassword.html',{'isOTP':True,'email':user.email})
         # -------------------------------------
         
      except Exception as e:
         # if email is invalid
         print("=========>>> Error :",e)
         msg="Email is not Registered"
         return render(request, 'institute_app/forgotpassword.html',{'msg':msg})
      
   return render(request, 'institute_app/forgotpassword.html')

# Note: user.email is given on almost every render to keep the view connected
