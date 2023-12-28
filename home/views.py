from django.shortcuts import render , HttpResponse , redirect 
from home.models import CustomUser
from django.contrib.auth import login, authenticate, logout
def home(request):
     return render(request,'home/index.html')

def sign_in(request):
     if request.method == "POST":
          email=request.POST.get('email')
          password = request.POST.get('password')
          user = authenticate(request, email=email, password=password)
          if user is not None:
               login(request,user)
               return redirect('prediction')
          else:
               context={'error':'Invalid Email or Password'}
               return render(request,"home/sign-in.html",context)
     return render(request,'home/sign-in.html')
def sign_out(request):
     logout(request)
     return redirect('home')

def sign_up(request):
     if request.method == "POST":
          email=request.POST.get('email')
          password = request.POST.get('password')
          name = request.POST.get('name')
          number = request.POST.get('number')
          if CustomUser.objects.filter(email=email).exists():
               context = {'error_message': 'This email is already registered.'}
               return render(request,'Author/sign-up.html',context)
          new_user = CustomUser.objects.create_user(
                email=email,
                password=password,
                name=name,
                number=number
               )
          new_user.save()
          context={
               'success_message':"Account Created Successfully!"
          }
          return render(request,'home/sign-up.html',context)
     else:
          return render(request,'home/sign-up.html')


from .ml import load_and_compile_model, train_model, make_predictions
# model, training_set, testing_set = load_and_compile_model()
import os
# Create the directory if it doesn't exist
directory = 'C:/Users/HP/Desktop/ml_project/eye/eye/upload_images/'
os.makedirs(directory, exist_ok=True)
# model, training_set, testing_set = load_and_compile_model()
from .ml import load_and_compile_model, train_model, make_predictions
model, training_set = load_and_compile_model(batch_size=32, subset_fraction=0.5)
            # Train the model (optional)
train_model(model, training_set, epochs=5)
def prediction(request):
    if request.user.is_authenticated:
        if request.method == "POST" and request.FILES.get('photo'):
            # Get the uploaded file
            uploaded_file = request.FILES.get('photo')
            # Save the file to a temporary location
            temp_path = 'C:/Users/HP/Desktop/ml_project/eye/eye/upload_images/image.jpg'
            with open(temp_path, 'wb') as f:
                for chunk in uploaded_file.chunks():
                    f.write(chunk)
            # Make predictions
            predictions = make_predictions(model, temp_path)
            context = {
                'image_path': temp_path,
                'predictions': predictions,
            }
            return render(request, 'home/prediction.html', context)

        return render(request, 'home/prediction.html')

    else:
        return redirect('home')
