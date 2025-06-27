from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt  # Optional if using {% csrf_token %}
from django.conf import settings

def index(request):
    return HttpResponse("<h1>hello</h1>")

def about(request):
    return render(request,"index.html")
def demo(request):
    return render(request,"demo.html")
@csrf_exempt  # Only use this if you're NOT using {% csrf_token %} in the form
@require_POST
def contact_view(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')

    if not all([name, email, subject, message]):
        return JsonResponse({'error': 'Please fill all the fields.'}, status=400)

    full_message = f"From: {name} <{email}>\n\nMessage:\n{message}"

    try:
        send_mail(
            subject=subject,
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,  # defined in settings.py
            recipient_list=['elumalaimurugan75@gmail.com'],  # your email
            fail_silently=False,
        )
        return JsonResponse({'message': 'Your message was sent successfully!'})
    except Exception as e:
        return JsonResponse({'error': f'Failed to send email: {str(e)}'}, status=500)