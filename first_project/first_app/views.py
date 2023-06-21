from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'insert_content':"Hello in from first app"}
    # index.html is under template folder
    return render(request,'first_app/index.html',context=my_dict)
