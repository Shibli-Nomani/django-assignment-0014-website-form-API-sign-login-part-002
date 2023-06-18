from django.shortcuts import render

#to create usercreation form (Registration)
from django.contrib.auth.forms import UserCreationForm
#to import modified UserCreationForm from forms.py
from . forms import usercf

#to login
from django.contrib.auth.forms import AuthenticationForm
#user login authetication verification
from django.contrib.auth import authenticate, login, logout

#to change password using django default product
from django.contrib.auth.forms import PasswordChangeForm

#to save the change password by the help of old password and logged in state
from django.contrib.auth import update_session_auth_hash

#change password without old password
from django.contrib.auth.forms import SetPasswordForm


#to show successful login notification and use HttpResponseRedirect
from django.shortcuts import HttpResponseRedirect


# Create your views here.
def About_Us(request):

    #dict = {'f0':50, 'f1': 7}

    return render(request,'aboutus/about.html')

def Profiles(request):

    return render(request, 'aboutus/profile.html')

def portfolio(request):

    return render(request, 'aboutus/portfolio.html')


#usercreation form for registration
def usercfrm(request):
    #to store into database
    if request.method == "POST":
        frm = usercf(request.POST) #replace the UserCreationForm by modified class
        if frm.is_valid():
            frm.save()

    #if not valid, it will remain at same page
    else:
        frm = usercf()
    return render(request, 'aboutus/usercreateform.html', {'form' : frm})

def login_form(request):
    if request.method == "POST":
        #user login request will store in request parameter of login_form function
        frm = AuthenticationForm(request = request, data = request.POST)
        if frm.is_valid():
            uname = frm.cleaned_data['username']
            upass = frm.cleaned_data['password']
            #to verify user detials with registration details while login
            user = authenticate(username = uname, password = upass)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/success/')
    #not valid remains same page        
    else:
        frm = AuthenticationForm()       
    return render(request, 'aboutus/login.html', {'form' : frm})

#successful login function

def slogin(request):
    return render(request, "aboutus/success.html") 


#for logout
def logout_form(request):
    logout(request)
    return HttpResponseRedirect('/login/')

#change_password using old password at login condition
def change_password(request):
    if request.user.is_authenticated:
        if request.method == "POST":

            #matching the current login user
            frm = PasswordChangeForm(user=request.user, data = request.POST)
            #matching condition and validation. then proceed to save the change password 
            if frm.is_valid():
                frm.save()
                update_session_auth_hash(request, frm.user)
                return HttpResponseRedirect('/success/')
        else:     
            frm = PasswordChangeForm(user= request.user) #cuurent user password change after login

        return render(request, 'aboutus/changepass.html', {'form' : frm})
    #not authenticaate redirect to login page
    else:
        return HttpResponseRedirect('/login')
    
#change password without old password
def change_without_old_password(request):
    if request.user.is_authenticated:
        if request.method == "POST":

            #matching the current login user
            frm = SetPasswordForm(user=request.user, data = request.POST)
            #matching condition and validation. then proceed to save the change password 
            if frm.is_valid():
                frm.save()
                update_session_auth_hash(request, frm.user)
                return HttpResponseRedirect('/success/')
        else:     
            frm = SetPasswordForm(user= request.user) #cuurent user password change after login

        return render(request, 'aboutus/changepass.html', {'form' : frm})
    
    #not authenticaate redirect to login page
    else:
        return HttpResponseRedirect('/login')




