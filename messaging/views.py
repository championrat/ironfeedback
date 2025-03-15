from django.shortcuts import render
from django.utils.timezone import now, timedelta
from django.http import JsonResponse
from .models import CustomerQueue, CustomerResponse

# Create your views here.
def form_submission(request):
    try:
        if request.method == "POST":
            customer_id = request.POST.get("customerID")
            customer_name = request.POST.get("customerName")
            job_type = int(request.POST.get("jobType"))
            customer_mobile = request.POST.get("customerMobile")
            
            if not all([customer_id, customer_name, job_type, customer_mobile]):
                return JsonResponse({"status": "error"}, {"message": "Invalid request payload. customer_id, customer_name, job_type and customer_mobile are required."}, status = 400)
            
            # calculate scheduled_time
            delay = timedelta(hours=1) if job_type == 1 else timedelta(hours=8)
            scheduled_time = now() + delay
            
            # add customer to DB queue
            CustomerQueue.objects.create(
                customerId=customer_id,
                customerName=customer_name,
                jobType=job_type,
                customerPhone=customer_mobile,
                queueTime=now(),
                scheduledTime=scheduled_time,
                messageSent=False
            )
            
            # responses
            return JsonResponse({"status": "success"}, {"message": "Customer queued successfully"}, status = 201)
        else:
            return JsonResponse({"status": "error"}, {"message": "Invalid request method"}, status = 405)
    
    except:
        return JsonResponse({"status": "error"}, {"message": "Server error"}, status = 500)