from django.shortcuts import *
from django.views.decorators.csrf import csrf_protect
from django.conf import settings
from django.core.mail import *
import datetime

import requests
import json
from app1.models import *




def mainpage(request):
    if(request.method=="POST"):
        gname = request.POST.get("name")
        gEmail = request.POST.get("email")
        gMobile = request.POST.get("no")
        hName = request.POST.get("hostname")
        hEmail = request.POST.get("hostemail")
        hMobile = request.POST.get("hostno")
        checkintime = timeInStandardform()
        print(100)

        try:
            #SENDING EMAIL
            subject = hName + "is here to visit you"
            message = "Visitor's Detail :\n" + "Name - " + gname + "\n"+ "Email -" + gEmail + "\n" + "Phone -" +gMobile + "\n"+"Checkin Time - "+ checkintime
            from_email = settings.EMAIL_HOST_USER
            to_list = [str(hEmail)]
            send_mail(subject,message,from_email,to_list,fail_silently=False)
            print(200)

            #sending sms
            URL = 'https://www.way2sms.com/api/v1/sendCampaign'
            response = sendPostRequest(URL, 'Enter you api key', 'Secret key', 'stage', hMobile, 'Enter you id', message )
            print(response.text)

            # storing vlue in database
            print(300)
            a = checkin(name=gname,email=gEmail,no=gMobile,hostname=hName,hostemail=hEmail,hostno=hMobile,checkInTime=checkintime,isCheckOut=False)
            a.save()



            return render(request,'app1/mainpage.html',{"error":"You have successfully requested for check-in "})

        except:
            return render(request,'app1/mainpage.html',{"error":"Please check the email you have entered"})
    else:
        return render(request,'app1/mainpage.html')




def checkout(req):
    if(req.method=="POST"):
        email = req.POST.get("email")
        try:
            #checking if person wih entered email check-n or not
            a = checkin.objects.get(email=email,isCheckOut=False)

            current_time = timeInStandardform()
            a.isCheckOut = True
            a.checkOutTime = current_time
            a.save()

            #sending email to guest on check-out
            subject = 'Your Visit Details'
            message = "\nName " +a.name + "\nPhone -" + a.no + "\nCheck-in Time - "+ a.checkInTime + "\nCheck-out time - "+a.checkOutTime+"\nHostname - "+a.hostname
            from_email = settings.EMAIL_HOST_USER
            to_list = [str(a.email),]
            send_mail(subject,message,from_email,to_list,fail_silently=False)

            #sending sms to guest on check-out
            URL = 'https://www.way2sms.com/api/v1/sendCampaign'
            response = sendPostRequest(URL, 'Enter your api key', 'Entere you secret key', 'stage', a.hostmobileNo, 'enter api id', message )



            return render(req,'app1/checkout.html',{"error":"You are successfully checked out "})

        except:
            return render(req,'app1/checkout.html',{"error":"The person with this email didn't check-in ."})
    else:
        return render(req,'app1/checkout.html',{})

def timeInStandardform():
    current_hour = datetime.datetime.now().time().hour
    current_minute = datetime.datetime.now().time().minute
    current_time = ""
    if(current_minute>9):
        current_minute = str(current_minute)
    else:
        current_minute = "0"+ str(current_minute)
    if(current_hour>12):
        current_hour -= 12
        current_time +=str(current_hour)+":"+current_minute+" PM IST"
    else:
        current_time +=str(current_hour)+":"+current_minute+" AM IST"

    return current_time


def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
    print("hello")
    req_params = {
        'apikey':apiKey,
        'secret':secretKey,
        'usetype':useType,
        'phone': phoneNo,
        'message':textMessage,
        'senderid':senderId
        }
    return requests.post(reqUrl, req_params)
