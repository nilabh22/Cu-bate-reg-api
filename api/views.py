from django.http import JsonResponse
from RegAPI import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework.decorators import api_view
from .serializers import RegistrationSerializer


# Create your views here.
@csrf_exempt
@api_view(['POST'])
def api(request):
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    if request.method == "POST":

        name = request.data['name']
        email = request.data['email']
        rollNo = request.data['rollNo']
        phone = request.data['phone']
        branch = request.data['branch']
        mydict = {'name':name}
        html_template = 'index.html'
        html_content = render_to_string(html_template,mydict)
        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(subject="Registration Successfull !!",
            body=text_content,
            from_email= settings.EMAIL_HOST_USER,
            to = [email]
        )

        email.attach_alternative(html_content,"text/html")
        # email.mixed_subtype = 'related'

        # for f in ['image-1.png', 'image-2.png', 'image-3.png', 'image-4.png', 'image-5.png']:
        #     fp = open(os.path.join(os.path.dirname(__file__), f), 'rb')
        #     msg_img = MIMEImage(fp.read())
        #     fp.close()
        #     msg_img.add_header('Content-ID', '<{}>'.format(f))
        #     email.attach(msg_img)

        email.send(fail_silently=False)

        # send_mail(subject='Thank You For Feedback !!',
        #     message = f"Hello {name}, We have successfully received your feedback.\nOur Team is continously working on the improvement and organizing the events for you.\n\nWe'll soon get back to you.\n\n\n\n\nTeam GeeksForGeeks\nCentral University of Haryana",
        #     from_email=settings.EMAIL_HOST_USER,
        #     recipient_list = [email],
        #     fail_silently=False)

        
    return JsonResponse({"success":"True", "data": {
        "code":200,
        "message": "Thank You for Registration!!"
    }})
