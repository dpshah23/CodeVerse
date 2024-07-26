from django.shortcuts import render,redirect
import datetime
from django.contrib import messages
import random 
import string
from .models import Users_main,resetpass
from django.http import HttpResponse
import smtplib
import os
from django.utils import timezone
from datetime import timedelta
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from django_ratelimit.decorators import ratelimit
from PIL import Image, ImageDraw, ImageFont
import io
import base64


# Create your views here.

def login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')

        try:
            user=Users_main.objects.get(email=email)

            if not user.isactive:
                messages.error(request,"Some Unusual Activity Happend in your account . So We have Blocked Your Account")
                return render(request,"login.html")
            
            islogin=user.check_password(password)
            if user.email==email and islogin:
                
                request.session['username']=user.username
                request.session['email']=user.email
                request.session['name']=user.name
                request.session['id']=user.user_id

                return redirect('/')

            else:
                messages.error(request,"Incorrect Password ....")
                return redirect('/auth/login')
        except Users_main.DoesNotExist:
            messages.error(request,"User Does Not Exist..")
            return render(request,"login.html")
        
    return render(request,"login.html")

def check_user(request,username):
    try:
        user=Users_main.objects.get(username=username)
        return HttpResponse({"success":False})
    except Users_main.DoesNotExist:
        return HttpResponse({"success":True})
    
def signup( request):
    if request.method=="POST":
        username=request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_id = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
        time_stamp = datetime.today()
        profile_pic = generate_avatar_base64(email)
        
        obj = Users_main(username = username , email=email ,user_id = user_id  , name = None , phone = None , city = None , qualification =None , profile_pic = profile_pic , dob = None , bio = None , description = None , time_stamp = time_stamp , is_active = False , level = None , tech = None)
        obj.set_password(password)
        obj.save()
        return redirect('/more_info/<user_id>/')

    return render (request , 'login.html')

def more_info(request , user_id):
    if request.method == "POST":
        pass

@ratelimit(key='ip', rate='10/m')
def reset(request):
    if request.method == "POST":
        email = request.POST.get('email')
        try:
            user = Users_main.objects.get(email=email)
            
        except Users_main.DoesNotExist:
            messages.error(request, 'Invalid Email')
            return render(request, 'reset.html')
        except Exception as e:
            print(e)
            messages.error(request, 'Invalid Email')
            return render(request, 'reset.html')
        try:
            load_dotenv()

            from_email = os.getenv('EMAIL')
            password = os.getenv('PASSWORD1')

            subject = "Reset Password"
            length = 8
            x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(32))
            expiry_duration = timedelta(hours=1)  
            expires_at = timezone.now() + expiry_duration
            resetpass1 = resetpass(email=email, keys=x, usage=False, expires_at=expires_at)
            resetpass1.save()
            final_str_link = "http://127.0.0.1:8000/auth/resetpass?email=" + email + "&key=" + x

            body = f"""
            <div style="font-family: Arial, sans-serif; color: #333;">
    <h1 style="text-align: center; color: #4CAF50;">Password Reset Request</h1>

    <p>Dear User,</p>

    <p>We understand that you are having trouble logging into your CodeVerse account. To help you get back on track, we have received a request to reset your password.</p>

    <p>If you initiated this request, you can reset your password by clicking the link below. For security reasons, this link will expire in 1 hour:</p>

    <div style="text-align: center; margin: 20px 0;">
        <h2 style="display: inline-block; background: #f4f4f4; padding: 10px 20px; border: 1px solid #ddd; border-radius: 5px;">
            <a href="{final_str_link}" style="text-decoration: none; color: #4CAF50;">Reset Password</a>
        </h2>
    </div>

    <p>If you did not request a password reset, please ignore this message. Your account will remain secure, and no changes will be made.</p>

    <p>If you have any questions or need further assistance, please do not hesitate to contact our team.</p>

    <p>Thank you for your understanding and cooperation.</p>

    <p>Best regards,<br><strong>The CodeVerse Team</strong></p>
</div>
            
            """
            msg = MIMEMultipart()
            msg['Subject'] = subject
            msg['From'] = from_email
            msg['To'] = email
            msg.attach(MIMEText(body, 'html'))

            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(from_email, password)
                server.sendmail(from_email, email, msg.as_string())

            messages.success(request, 'Reset link sent to your email')
            return redirect('/auth/login')
        except Users_main.DoesNotExist:
            messages.error(request, 'Invalid Email')
            return render(request, 'reset.html')
        
        except Exception as e:
            print(e)
            messages.error(request, 'Invalid Email')
            return render(request, 'reset.html')

    return render(request, 'reset.html')

def generate_avatar_base64(email, size=128):
    image = Image.new('RGB', (size, size), color='white')
    draw = ImageDraw.Draw(image)

    circle_color = tuple(random.randint(0, 255) for _ in range(3))
    draw.ellipse([(0, 0), (size, size)], fill=circle_color, outline=None)

    text = email[0].upper()
    font_size = size // 2
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    text_x = (size - text_width) / 2
    text_y = (size - text_height) / 2
    draw.text((text_x, text_y), text, font=font, fill='white')

    buffer = io.BytesIO()
    image.save(buffer, format="PNG")

    img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return img_str

