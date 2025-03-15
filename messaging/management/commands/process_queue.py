import datetime
from django.core.management.base import BaseCommand
from messaging.models import CustomerQueue
from messaging.utils import send_sms

class Command(BaseCommand):
    help = "Process scheduled messages in the customer queue"

    def handle(self, *args, **kwargs):
        now = datetime.datetime.now()
        pending_messages = CustomerQueue.objects.filter(scheduled_time__lte=now, status="pending")

        for message in pending_messages:
            success = send_sms(message.customerMobile, f"Hi {message.customerName}, Thank you for visiting IronPalmTattoos. Please rate your overall experience at our shop from 1 through 5, with 1 being the worst service and 5 being the best service.")
            if success:
                message.status = "sent"
                message.save()
                self.stdout.write(self.style.SUCCESS(f"Message successfully sent to {message.customerMobile}"))
            else:
                self.stdout.write(self.style.ERROR(f"Failed to send message to {message.customerMobile}"))
