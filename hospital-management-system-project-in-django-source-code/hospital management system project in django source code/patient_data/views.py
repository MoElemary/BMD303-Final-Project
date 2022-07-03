from django.http import JsonResponse
from django.shortcuts import redirect, render
from pymongo import MongoClient
from bson import json_util
import json
import numpy as np
from PIL import Image
import io

CLUSTER = "mongodb+srv://BMD:12345G@cluster0.zlpfwmb.mongodb.net/?retryWrites=true&w=majority"


def patient(request):
    return render(request, "pat_data.html", )


def ret_patient(request):
    if request.method == "POST":
        if "pat_id" in request.POST:
            query = request.POST.get("pat_id")
            client = MongoClient(CLUSTER)
            db = client.BMD
            patient_data = db.data
            res = patient_data.find_one({"patient_id": query})

            if "x_ray_img" in list(res):
                pil_img = Image.open(io.BytesIO(res["x_ray_img"]))
                result = Image.fromarray((np.array(pil_img)).astype(np.uint8))
                result.save('static/images/out.jpg')
                data = {"pat_id": res["patient_id"],
                        "pat_name": res["patient_name"],
                        "pat_med": res["patient_medicines"],
                        "pat_img": res["x_ray_img"],
                        "blood_type": res["blood_type"],
                        "Diagnose": res["Diagnose"],
                        "SocialSecurityNumber": res["SocialSecurityNumber"],
                        "Age": res["Age"],
                        "Dateofexamination": res["Dateofexamination"],
                        "Dateofsecondexamination": res["Dateofsecondexamination"],
                        }
                client.close()
                return render(request, "ret_patient.html", data)
            else:
                data = {"pat_id": res["patient_id"],
                        "pat_name": res["patient_name"],
                        "pat_med": res["patient_medicines"],
                        "blood_type": res["blood_type"],
                        "needed_rad": res["needed_rad"],
                        "Diagnose": res["Diagnose"],
                        "SocialSecurityNumber": res["SocialSecurityNumber"],
                        "Age": res["Age"],
                        "Dateofexamination": res["Dateofexamination"],
                        "Dateofsecondexamination": res["Dateofsecondexamination"],
                        }
                client.close()
                return render(request, "ret_patient.html", data)


def add_patient(request):
    if request.method == "POST":
        if "name" in request.POST:
            pat_id = request.POST.get("pat_id")
            pat_name = request.POST.get("name")
            med1 = request.POST.get("med1")
            med2 = request.POST.get("med2")
            needed_rad = request.POST.get("rad")
            blood_type = request.POST.get("blood_type")
            Diagnose = request.POST.get("Diagnose")
            SocialSecurityNumber = request.POST.get("SocialSecurityNumber")
            Age = request.POST.get("Age")
            Dateofexamination = request.POST.get("Dateofexamination")
            Dateofsecondexamination = request.POST.get("Dateofsecondexamination")
            # img=request.POST.get("image")
            # im = Image.open("static/images/"+str(img))
            # image_bytes = io.BytesIO()
            # print(image_bytes)
            # im.save(image_bytes, format='JPEG')
            p_data = {"patient_id": pat_id,
                      "patient_name": pat_name,
                      "patient_medicines": [med1, med2],
                      "needed_rad": needed_rad,
                      "blood_type": blood_type,
                      "Diagnose": Diagnose,
                      "SocialSecurityNumber": SocialSecurityNumber,
                      "Age": Age,
                      "Dateofexamination": Dateofexamination,
                      "Dateofsecondexamination": Dateofsecondexamination,
                      # "x_ray_img": image_bytes.getvalue()
                      }
            client = MongoClient(CLUSTER)
            db = client.BMD
            patient_data = db.data
            patient_data.insert_one(p_data)
            client.close()
            return redirect("p_data:pat")



