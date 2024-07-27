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
from datetime import datetime

# Create your views here.

def login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')

        try:
            user=Users_main.objects.get(email=email)

            if not user.is_active:
                messages.error(request,"Some Unusual Activity Happend in your account . So We have Blocked Your Account")
                return render(request,"login.html")
            
            islogin=user.check_password(password)
            if user.email==email and islogin:
                print("login done")
                request.session['username']=user.username
                request.session['email']=user.email
                request.session['name']=user.name
                request.session['id']=user.user_id

                print(request.session['email'])
                print(request.session['username'])
                print(request.session['id'])
                print(request.session['name'])

                return redirect('/',{"email":request.session['email'],"username":request.session['username']})

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
        return redirect(f'user_details/{user_id}/')

    return render (request , 'login.html')

def user_details(request , user_id):
    if request.method == "POST":
        email = Users_main.objects.get(user_id=user_id).email
        phone = request.POST.get( 'phone' )
        city = request.POST.get( 'city' )
        qualifications = request.POST.get( 'qualifications' )
        experience = request.POST.get('experience')
        profile_pic = request.POST.get('profile_pic')
        dob = request.POST.get( 'dob' )
        bio = request.POST.get( 'bio' )
        level = request.POST.get('level')


        obj, created = Users_main.objects.update_or_create(
            email=email,
            defaults={
                'phone' : phone ,
                'city' : city ,
                'qualification' : qualifications ,
                'experience': experience,
                'profile_pic' : profile_pic ,
                'dob' : dob ,
                'bio' : bio ,
                'is_active' : True , 
                'level' : level 
                
            }
        )
        return render( request , 'quiz.html' , {'level':level})
    return render (request , 'user_details.html')



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



@ratelimit(key='ip', rate='10/m')
def reset_pass(request):
    if request.method == "GET":
        email = request.GET.get('email')
        key = request.GET.get('key')
        # print(f"Received email: {email}, key: {key}")  # Debugging

        try:
            user_reset = resetpass.objects.get(email=email, keys=key)
            # print(f"Reset entry found: {user_reset}")  # Debugging

            if user_reset.usage:
                messages.error(request,"Link Is Already Used")
                return redirect('/auth/login')
            elif user_reset.is_expired():
                print("Invalid Link: Link is Expired")  # Debugging
                messages.error(request, 'Link is expired')
                return redirect('/auth/login')
            
        except resetpass.DoesNotExist:
            print(f"No reset entry found for email: {email} and key: {key}")  # Debugging
            messages.error(request, 'Invalid reset link or Link Already Used')
            return redirect('/auth/login')

    elif request.method == "POST":
        new_pass = request.POST.get('password')
        email = request.POST.get('email')
        key=request.POST.get('key')
        # print(f"New password received for email {email}: {new_pass}")  # Debugging

        try:
            user = Users_main.objects.get(email=email)
            # print(f"User found: {user}")  # Debugging
            user_reset = resetpass.objects.get(email=email, keys=key)
            # Generate a new encryption key and encrypt the new password
            

            # Update user's password and key
            user.set_password(new_pass)
    
            user.save()

            # Mark the reset pass entry as used
            user_reset.usage = True
            user_reset.save()

            user_reset.delete()

            return redirect('/auth/login')
        
        except resetpass.DoesNotExist:
            # print(f"Reset entry not found for email: {email}")  # Debugging
            messages.error(request, 'Invalid reset link')
            return render(request, 'Reset_Password.html')
        
        except Users_main.DoesNotExist:
            # print(f"User with email {email} does not exist.")  # Debugging
            messages.error(request, 'User does not exist')
            return render(request, 'Reset_Password.html', {'email': email})
        
        except Exception as e:
            # print(f"Error resetting password: {str(e)}")  # Debugging
            messages.error(request, 'Error resetting password. Please try again.')
            return render(request, 'Reset_Password.html', {'email': email})

    return render(request, 'Reset_Password.html')


def logout(request):

    if 'email' and 'username' and 'id' in request.session:
        request.session.pop('email')
        request.session.pop('username')
        request.session.pop('id')
        request.session.flush()

        return redirect('/')
