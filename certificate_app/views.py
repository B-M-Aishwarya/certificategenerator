from django.shortcuts import render, get_object_or_404, HttpResponse, reverse, redirect
from django.http import JsonResponse
from .models import Certificate, VerificationToken
from django.contrib.auth.decorators import login_required
import datetime

def create_certificate(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            certificate = Certificate.objects.create(title=title, content=content)
            print("Certificate Created:", certificate) 
            return JsonResponse({'certificate_id': str(certificate.id)})
            return redirect('certificate_details', certificate_id=certificate.id)
        else:
            return HttpResponse('Please provide both title and content for the certificate.', status=400)
    elif request.method == 'GET':
        return render(request, 'create_certificate.html')
    else:
        return HttpResponse('Method not allowed.', status=405)

def verify_certificate(request):
    if request.method == 'POST':
        token = request.POST.get('token')
        print("Received Token:", token)  
        try:
            verification_token = VerificationToken.objects.get(token=token)
            print("Token in Database:", verification_token.token)  
            return JsonResponse({'valid': True, 'certificate_id': str(verification_token.certificate.id)})
        except VerificationToken.DoesNotExist:
            print("Token Not Found in Database")  
            return JsonResponse({'valid': False})
    elif request.method == 'GET':
        return render(request, 'verify_certificate.html')
    else:
        return HttpResponse('Method not allowed.', status=405)

@login_required
def customize_certificate(request, certificate_id):
    certificate = get_object_or_404(Certificate, id=certificate_id)
    if request.method == 'POST':
        new_title = request.POST['new_title']
        new_content = request.POST['new_content']
        certificate.title = new_title
        certificate.content = new_content
        certificate.save()
    return render(request, 'customize_certificate.html', {'certificate': certificate})

def certificate_details(request, certificate_id):
    certificate = Certificate.objects.get(id=certificate_id)
    current_date = datetime.date.today()
    return render(request, 'certificate_details.html', {'certificate': certificate, 'current_date': current_date})