from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail


def contacto(request):
    if request.method == 'POST':    
        
         
        subject = request.POST['asunto']                                                        
        message = request.POST['mensaje']+'\n\nMensaje escrito por:\n'+request.POST['nombre']+' // '+request.POST['email']  
        email_from= settings.EMAIL_HOST_USER                                                       
        recipient_list = ['centenojhon100598@gmail.com']                                            
        
        send_mail(subject, message, email_from, recipient_list)           
        
        return render(request, 'E.2mensaje_enviado.html')  
    return render(request, 'Econtacto.html')