import pickle
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Product, Patient,ProductDetails
from pymongo import MongoClient
from bson.binary import Binary
import numpy as np
from PIL import Image
import io
from django.contrib import messages
# Create your views here.


def homepage(request):
    contex = {
        'I': Product.objects.all()

    }
    return render(request, 'storeapp/home.html', contex)


def about_us(user_response):
    return render(user_response, 'storeapp/about.html', {'title': 'about'})


def Patient(request):
    contex_page = {
        'K': Patient.objects.all()
    }
    return render(request, 'storeapp/Customers.html', contex_page )
    #return render(user_response, 'store/home.html', contex)


def details(request):
    contex_page = {
        'L': ProductDetails.objects.all()
    }
    return render(request, 'storeapp/Details.html', contex_page )
    #return render(user_response, 'store/home.html', contex)

CLUSTER="mongodb+srv://BMD:12345G@cluster0.zlpfwmb.mongodb.net/?retryWrites=true&w=majority"

def patient(request):
    return render(request,"storeapp/pat_data.html",)

def ret_patient(request):
    if request.method=="POST":
        if "pat_id" in request.POST:
            query=request.POST.get("pat_id")
            client=MongoClient(CLUSTER)
            db=client.BMD
            patient_data=db.data
            res=patient_data.find_one({"patient_id":query})

            if "x_ray_img" in list(res):
                pil_img = Image.open(io.BytesIO(res["x_ray_img"]))
                result = Image.fromarray((np.array(pil_img)).astype(np.uint8))
                result.save('storeapp/static/images/out.jpg')
                data={"pat_id":res["patient_id"],
                    "pat_name":res["patient_name"],
                    "pat_med":res["patient_medicines"],
                    "blood_type":res["blood_type"],
                    "pat_img":res["x_ray_img"],
                    "Diagnose":res["Diagnose"],
                    "SocialSecurityNumber":res["SocialSecurityNumber"],
                    "Age": res["Age"],
                    "Dateofexamination": res["Dateofexamination"],
                    "Dateofsecondexamination": res["Dateofsecondexamination"],
                    "rad":"Added"
                    }
                client.close()
                return render(request,"storeapp/ret_patient.html",data)
            else:
                data={"pat_id":res["patient_id"],
                    "pat_name":res["patient_name"],
                    "pat_med":res["patient_medicines"],
                    "blood_type":res["blood_type"],
                    "Diagnose": res["Diagnose"],
                    "SocialSecurityNumber": res["SocialSecurityNumber"],
                    "Age": res["Age"],
                    "Dateofexamination": res["Dateofexamination"],
                    "Dateofsecondexamination": res["Dateofsecondexamination"],
                    "rad":res["needed_rad"]
                     }
                client.close()
                return render(request,"storeapp/ret_patient.html",data)

def add_patient(request):
    if request.method=="POST":
        if "image" in request.POST:
            pat_id=request.POST.get("pat_id")
            img=request.POST.get("image")
            if img:
                im = Image.open("storeapp/static/images/"+str(img))
                image_bytes = io.BytesIO()
                im.save(image_bytes, format='JPEG')
            if not img:
                messages.error(request, 'Invalid')
                redirect("pat")
            client=MongoClient(CLUSTER)
            db=client.BMD
            patient_data=db.data
            res=patient_data.find_one({"patient_id":pat_id})
            if res:
                name=res["patient_name"]
                med=res["patient_medicines"]
                blood_type=res["blood_type"]
                Diagnose=res["Diagnose"]
                SocialSecurityNumber = res["SocialSecurityNumber"]
                Age = res["Age"]
                Dateofexamination = res["Dateofexamination"]
                Dateofsecondexamination = res["Dateofsecondexamination"]
                p_data={
                        "patient_id":pat_id,
                        "patient_name":name,
                        "patient_medicines":med,
                        "blood_type": blood_type,
                        "Diagnose": Diagnose,
                        "SocialSecurityNumber": SocialSecurityNumber,
                        "Age": Age,
                        "Dateofexamination": Dateofexamination,
                        "Dateofsecondexamination": Dateofsecondexamination,
                    "x_ray_img": image_bytes.getvalue()
                        }
                patient_data.delete_one({"patient_id":pat_id})
                client.close()
                client=MongoClient(CLUSTER)
                db=client.BMD
                patient_data=db.data
                patient_data.insert_one(p_data)
                client.close()
                messages.success(request,"Image added Successfully to the patient with id: "+str(pat_id))
                return redirect("pat")

            else:
                client.close()
                messages.error(request, 'Invalid ID')
                return redirect("pat")