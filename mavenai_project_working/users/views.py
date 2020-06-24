from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate , logout
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, LoginForm
from .models import RegisterUser
import hashlib, random
import string  
import os
from django.views import View
from django.http import JsonResponse
from users.amazonupload import MediaStorage




# Create your views here.
def register(request):
    form = SignUpForm(request.POST , request.FILES)
    # print(form.cleaned_data.get('username'))
    if(request.method=="POST"):
        if form.is_valid():
            temp = RegisterUser()
            temp.user_email=request.POST['email']
            temp.user_name = form.cleaned_data.get('full_name')
            temp.user_mobile_no=form.cleaned_data.get('mobile_no')
            temp.user_passport_no=form.cleaned_data.get('passport_num')
            temp.user_age = form.cleaned_data.get('age')
            print(request.FILES['image'])
            if(form.cleaned_data['image']):
                file_obj = request.FILES['image']
                file_directory_within_bucket = 'user_upload_files/{username}'.format(username=temp.user_name)

                file_path_within_bucket = os.path.join(
                    file_directory_within_bucket,
                    file_obj.name
                )

                media_storage = MediaStorage()

                if not media_storage.exists(file_path_within_bucket):
                    media_storage.save(file_path_within_bucket, file_obj)
                    file_url = media_storage.url(file_path_within_bucket)

                    temp.user_image=request.FILES['image']
                else:
                    return JsonResponse({
                        'message': 'Error: file {filename} already exists at {file_directory} in bucket {bucket_name}'.format(
                            filename=file_obj.name,
                            file_directory=file_directory_within_bucket,
                            bucket_name=media_storage.bucket_name
                        ),
                    }, status=400)

            temp.user_dob=request.POST['dob']
            password = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = 7))
            print(password)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
            temp.user_password=hashlib.md5(password.encode()).hexdigest()
            temp.save()
            # 'BN0GTUJ' 'V43DY7R'
            return render(request,'users/register.html',{'form':form,'password':'Your password will be '+password})

    else:
        form = SignUpForm()
        args = {}
        args['form']=form
        return  render(request,'users/register.html',{'form':form})

def login(request):
    if(request.POST):
        form = LoginForm(request.POST)
        if(form.is_valid):
            username= request.POST['user_name']
            password = request.POST['password']
            temp = RegisterUser.objects.filter(user_email=username)
            for user in temp:
                if(user.user_password!=None):
                    print(user.user_password)
                    mdPass = hashlib.md5(password.encode()).hexdigest()
                    dbPass = hashlib.sha256(user.user_password.encode()).hexdigest()
                    uiPass = hashlib.sha256(mdPass.encode()).hexdigest()
                    if(dbPass==uiPass):
                        request.session['loginUser']=username
                        return redirect('dashboard')
                        # return redirect('http://127.0.0.1:8000/dashboard',{'form':form,'user':user})
                        # return render(request,'users/dashboard.html',{'form':form,'user':user})
                    else:
                        return render(request,'users/login.html',{'form':form,'message':'Wrong password'})
    else:
        form = LoginForm()
        return render(request,'users/login.html',{'form':form})

def dashboard(request):
    if(request.POST):
        oldPassword= request.POST['oldpassword']
        password = request.POST['password']
        newPassword = request.POST['newpassword']
        
        if(password==newPassword):
            temp = RegisterUser.objects.get(user_password=hashlib.md5(oldPassword.encode()).hexdigest(),user_email=request.session['loginUser'])
            if(temp):
                temp.user_password=hashlib.md5(password.encode()).hexdigest()
                temp.save()
                logout(request)
                return render(request,'users/dashboard.html',{'message':"password changed succesfully"})
        else:
            return render(request,'users/dashboard.html',{'message':"passwords did not match"})
    else:
        try:
            print(request.session['loginUser'])
            # logout(request)
            return render(request,'users/dashboard.html',{'loginUser':request.session['loginUser']})
        except Exception as identifier:
            logout(request)
            return redirect('login')
            