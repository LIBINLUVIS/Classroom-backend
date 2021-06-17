from django.contrib.auth.models import User
from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import login
from .models import User, classcreate, Addwork, Submitedworks
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from .serializers import UserSerializer, classcreateSerializer, AddworkSerializer, SubmitedWorksSerializer, EditClassSerializer
from django.contrib.auth.decorators import login_required
import json

# Register API


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


@api_view(['GET'])
def users(request):
	tasks = User.objects.all()
	serializer = UserSerializer(tasks, many=True)
	return Response(serializer.data)


@api_view(['POST'])
def CreateClass(request):
    user = request.user
    data = request.data
    datas = classcreate.objects.create(
        user=user,
        classname=data['classname']

    )

    return Response("class created")


@api_view(['GET'])
def classes(request):
    
    classes = classcreate.objects.all()
    serializer = classcreateSerializer(classes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def classview(request, pk):
    viewclass = classcreate.objects.get(id=pk)
    serializer = classcreateSerializer(viewclass)
    return Response(serializer.data)


@api_view(['GET'])
def userinfo(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['GET'])
def userclass(request):
    user = request.user
    serializer = UserSerializer(user)
    data = serializer.data
    values = data.values()
    value_iter = iter(values)
    user_id = next(value_iter)
    user_class = classcreate.objects.all()
    userclasses = []
    for x in user_class:
        if(x.user.id==user_id):
            temp = classcreateSerializer(x)
            userclasses.append(temp.data)

    return Response(userclasses)


@api_view(['POST'])
def Addworks(request, pk):
    user = request.user
    room = classcreate.objects.all().get(id=pk)
    data = request.data
    file = request.data['file']
    datas = Addwork.objects.create(
        auther=user,
        room=room,
        discription=data['discription'],
        submition=data['submition'],
        file=file

    )

    return Response("Work Created Successfully !!!")


@api_view(['GET'])
def Works(request, pk):
    temp = []
    works = Addwork.objects.all()
    for work in works:
        if(work.room.id == pk):
            item = AddworkSerializer(work)
            temp.append(item.data)

        else:
            print("work not founded")

    return Response(temp)


@api_view(['GET'])
def Submitwork(request, pk):
    temp = []
    work = Addwork.objects.all()
    for x in work:
        if(x.id == pk):
            res = AddworkSerializer(x)
            temp.append(res.data)
            break

    return Response(temp)


@api_view(['POST'])
def StudentWork(request, pk):
    user = request.user
    work = Addwork.objects.all().get(id=pk)
    data = request.data
    file = request.data['file']
    datas = Submitedworks.objects.create(
        student=user,
        work=work,
        Message=data['Message'],
        file=file,
        status=True

    )

    return Response("Work Submited Successfully !!!")


@api_view(['GET'])
def getresponses(request, pk):
    Responses = []
    works = Submitedworks.objects.all()
    for x in works:
        if(x.work.id == pk):
            
            Res = SubmitedWorksSerializer(x)
                
            Responses.append(Res.data)
    

    return Response(Responses)


@api_view(['POST'])
def updateclass(request,pk):
    item=classcreate.objects.all().get(id=pk)
    serializer=EditClassSerializer(instance=item,data=request.data)

    if serializer.is_valid():
        serializer.save();

    return Response(serializer.data)



@api_view(['GET'])
def Joinclass(request,pk):
  
    obj=classcreate.objects.all().get(id=pk)
    obj.accessors.add(request.user)
    return Response("Joined class Successfully")

@api_view(['GET'])
def getJoinclass(request):
    temp=[]
    obj=classcreate.objects.all()
    for x in obj:
        if x.accessors.filter(id=request.user.id).exists():
            serializer=classcreateSerializer(x)
            temp.append(serializer.data)

    return Response(temp)

@api_view(['GET'])
def submitstatus(request):
    completed_works=[]
    workstatus=Submitedworks.objects.all()
    user=request.user.id
    for x in workstatus:
        if(x.student.id==user and x.status):
            if(x.work.id not in completed_works):

                completed_works.append(x.work.id)
            
        else:
            print('no data found')

    result=json.dumps(completed_works)

    return Response(completed_works)
    





    
