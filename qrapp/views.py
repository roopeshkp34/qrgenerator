from django.shortcuts import render,redirect
from qrcode import *
from PIL import Image
from .models import Profile
from django.conf import  settings
from django.core.files import File
from django.urls import reverse
import qrtools
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
import tempfile
from svglib.svglib import svg2rlg


# Create your views here.
username=None
def index(request):
    global username
    if request.method=="POST":
        name=request.POST.get("name")
        address=request.POST.get("address")
        place=request.POST.get("place")
        username=request.POST.get("username")
        profile=Profile(name=name, address=address,place=place,username=username)
        img=make(settings.LOCALROOT+username)
        img.save(settings.MEDIA_ROOT+'\\'+username+".png")
        with open(settings.MEDIA_ROOT+'\\'+ username+".png", "rb") as reopen:
            django_file = File(reopen)
            profile.image=django_file

        
            profile.save()
        
        # return render(request,"index.html",{'data':username})
        return redirect(reverse('profile',args=[username]))

        
    return render(request,"index.html")

def profile(request,username):
    try:
        profile=Profile.objects.get(username=username)
        context={
            "profile":profile
            }
        return render(request,"profile.html",context)
    except:
        return render(request,"profile.html")

def download(request,username):
    print(username)
    point = 1
    inch = 72
    profile=Profile.objects.get(username=username)
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas("hi.pdf", pagesize=(2 * inch, 0.94 * inch))
    renderPDF.draw(profile, p, 0, 0)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(0, 0, profile.username)
    p.drawString(0, 0, profile.name)


    

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True,filename="hi.pdf")


# from django.shortcuts import render
# import qrcode
# import qrcode.image.svg
# from io import BytesIO
# def index(request):
#     context = {} 
#     if request.method == "POST": 
#         factory = qrcode.image.svg.SvgImage 
#         img = qrcode.make(request.POST.get("qr_text",""), image_factory=factory, box_size=20) 
#         stream = BytesIO() 
#         img.save(stream) 
#         context["svg"] = stream.getvalue().decode() 
#         return render(request, "index.html", context=context)