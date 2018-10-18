from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from . import ocr
# Create your views here.
def index(request):
    return render(request, 'index.html')

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        topleft_width = int(request.POST['topleft_width'])
        topleft_hieght = int(request.POST['topleft_hieght'])
        bottomright_width = int(request.POST['bottomright_width'])
        bottomright_hieght = int(request.POST['bottomright_hieght'])
        myfile = request.FILES['myfile']

        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        extracted_text = ocr.extract(myfile,(topleft_width,topleft_hieght),(bottomright_width,bottomright_hieght))
        print(extracted_text)
        return render(request, 'simple_upload.html', {'uploaded_file_url': uploaded_file_url,"text":extracted_text})

    return render(request,'simple_upload.html')
