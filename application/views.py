from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from application.models import Student
from application.form import student_Form
from django.db.models import Q
from django.core.paginator import Paginator


# ✅ Register View
def register_view(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('useremail')
        password = request.POST.get('userpassword')
        confirm_password = request.POST.get('confirmpassword')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
        elif User.objects.filter(username=name).exists():
            messages.error(request, "Username already exists!")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
        else:
            User.objects.create_user(username=name, email=email, password=password)
            messages.success(request, "Registered successfully. Please login.")
            return redirect('login')

    return render(request, 'studentapp/registerpage.html')


# ✅ Login View (Handles ?next= redirect)
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('loginname')
        password = request.POST.get('loginpassword')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            next_url = request.GET.get('next')
            return redirect(next_url) if next_url else redirect('landingpage')
        else:
            messages.error(request, "Invalid credentials!")

    return render(request, 'studentapp/login.html')


# ✅ Landing Page – Accessible without login
def landingpage(request):
    messages.info(request, "Welcome to the Student Management App!")
    return render(request, 'studentapp/landingpage.html')


# ✅ Add Details – Login Required
@login_required(login_url='login')
def adddetails(request):
    form = student_Form()
    if request.method == 'POST':
        form = student_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showdetails')
    return render(request, 'studentapp/adddetails.html', {'form': form})


# ✅ Show Details – Login Required + Search + Pagination
@login_required(login_url='login')
def showdetails(request):
    query = request.GET.get('q', '')
    if query:
        students = Student.objects.filter(
            Q(Name__icontains=query) |
            Q(Branch__icontains=query) |
            Q(College__icontains=query)
        ).order_by('id')
    else:
        students = Student.objects.all().order_by('id')

    paginator = Paginator(students, 5)  # 5 per page
    page = request.GET.get('page')
    students_paginated = paginator.get_page(page)

    return render(request, 'studentapp/showdetails.html', {
        'Students': students_paginated,
        'query': query
    })


# ✅ Update – No login required
def update(request, id):
    print("Update View Called")  # Optional debug
    data = get_object_or_404(Student, id=id)
    form = student_Form(instance=data)
    if request.method == 'POST':
        form = student_Form(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('showdetails')
    return render(request, 'studentapp/updatedetails.html', {'form': form})


# ✅ Delete – No login required
def delete(request, id):
    student_data = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student_data.delete()
        return redirect('showdetails')
    return render(request, 'studentapp/deletedetails.html', {'Student': student_data})


# ✅ Logout View – Redirect to register page
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('landingpage')
