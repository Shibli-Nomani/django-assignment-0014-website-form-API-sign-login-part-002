from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

#works on class based view, template view and redirect view
#to import class based view
from django.views import View
#to import template view
from django.views.generic.base import TemplateView
#redirectview has redirecting the page to given url 
# and no need to define class in views.pyand call the RedirectView in urls.py
from django.views.generic.base import RedirectView

#class based View
class DestinationPackage(View):
    def get(self, request):
        return render (request, 'attractions/attraction.html')
#class based TemplateView
class DestinationPackageTemplateView(TemplateView):
    template_name = "attractions/blogs.html"

#


# Create your views here.
def Attractions(request):

    location1 = "United State Of America"
    location2 = "United Kingdom"
    location3 = "UNITED ARAB EMIRATES"

    locs = {'l1' : location1, 'l2' : location2, 'l3' : location3 }


    return render(request,'attractions/attraction.html', locs)

def Blogs(request):

    #name1 = "John is satisfied about his trip."
    #name2 = "Ron had a very bad experience with other team members."
    #name3 = "Richal has been booked another trip."

    #user_experience = {'u1': name1, 'u2': name2, 'u3': name3}

    return render(request, 'attractions/blogs.html')

