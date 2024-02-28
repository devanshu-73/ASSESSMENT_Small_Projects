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

def register(request):
    return render(request,'institute_app/person.html')

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
            teacher = Teacher(person=new_person, compensation=compensation)
            teacher.save()
        elif person_type == 'student':
            # Get the last roll number used for students
            last_student = Student.objects.last()
            if last_student:
                last_roll_number = int(last_student.roll_number)
            else:
                last_roll_number = 0
                
            # Increment the last roll number by 1 for the new student
            roll_number = str(last_roll_number + 1)
            
            student = Student(person=new_person, roll_number=roll_number)
            student.save()

        messages.success(request, 'Person added successfully!')
        return redirect('index')  

    return render(request, 'institute_app/add_person.html')

def student_detail_view(request, student_id):
    students = Student.objects.filter(id=student_id)
    if students.exists():
        student = students.first()
        return render(request, 'institute_app/student_detail.html', {'student': student})
    else:
        return render(request, 'institute_app/student_detail_view.html')

def index(request):
    if 'username' in request.session:
        # User is logged in, render home page
        username = request.session['username']
        try:
            user = People.objects.get(username=username)
            context = {"user": user}
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
