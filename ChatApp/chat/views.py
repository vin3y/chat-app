from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from chat.models import Message
from chat.serializers import UserSerializers, MessageSerializers
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# Create your views here.



#users view
@csrf_exempt
def users_list(request, pk = None):
    """
    List all required messages, or create a new message.

    """
    if request.method == 'GET':
        
        if pk:    # If PrimaryKey (id) of the user is specified in the url
            users = User.objects.filter(id = pk)   # Select only that particular user
        else:
            users = User.objects.all()   # Else get all user list
        serializer = UserSerializers(users, many = True, context = {'request' : request})
        return JsonResponse(serializer.data, safe = False)    # Return serialized data
    
    elif request.method == 'POST':
            data = JSONParser().parse(request)      # On POST, parse the request object to obtain the data in json  
            serializer = UserSerializers(data = data)       # Seraialize the data
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status = 201)   # Return back the data on success
            return JsonResponse(serializer.errors, status = 400)
        
@csrf_exempt
def message_list(request, sender = None, receiver = None):
     
     if request.method == 'GET':
         messages = Message.objects.filter(sender_id = sender, reciever_id = receiver)
         serializer = MessageSerializers(messages, many = True, context={'request': request})
         return JsonResponse(serializers.data, safe = False)
     elif request.method == "POST":
         data = JSONParser.parse(request)
         serializer = UserSerializers(data= data)
         if serializer.is_valid():
             serializer.save()
             return JsonResponse(serializer.data, status = 201)
         return JsonResponse(serializer.errors, status = 400)
     
     
def index(request):
    if request.user.is_authenticated:
        return redirect('chats')
    if request.method == 'GET':
        return render(request, 'chats/index.html', {})
    elif request.method == 'POST': #authentication of user
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
        else:
            return HttpResponse('{"error" : "USER DOES NOT EXSIST"}')
        return redirect('chats')
        
def register_view(request):
    if request.user.is_authenticated:
        return render('index')
    return render(request, 'chat/register.html', {})

def chat_view(request):
    if not request.user.is_authenticated:
        return render('index')
    if request.method == 'GET':
        return render(request, 'chat/chat.html',{'users' : User.objects.exclude(username = request.user.username)}) #Returning context for all users except the current logged-in user
    
def message_view(request, sender, reciever):
    if not request.user.is_authenticated:
        return render('index')
    if request.method == 'GET':
        return render(request, 'chat/message.html', {'users' : User.objects.exclude(username = request.user.username), 'receiver' : User.objects.get(id = reciever), 'messages' : User.objects.filter(sender_id = sender, reciever_id = receiver) | User.objects.filter(sender_id =reciever, reciever_id = sender)})
    
    
@login_required
def logout(request):
    logout(request)
    return redirect('index')