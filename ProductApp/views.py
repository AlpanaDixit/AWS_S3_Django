from django.shortcuts import render
# from django.core.files.storage import 

def index(request):
    return render(template_name="index.html", request=request)

def upload_file(request):
    file = request.FILES.get("file")