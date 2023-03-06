from django.shortcuts import render, redirect
from application.models import AppModel
from application.form import AppModelForm
from application.serializer import AppModelSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

from django.core.mail import send_mail, EmailMessage
class Home:
    def index(self, request):
        
        if request.method == "POST":
            title = "title"
            body = "wefiwefjiowejfoiewf"
            e = EmailMessage(subject=title, body=body, from_email="mrkaungminnkhan@gmail.com",
                             to=['kaungminkhant4t99@gmail.com'])
            e.send()
            return redirect("/")
        
        p = request

        return render(request, 'index.html',
                        {"p": p})



class Post:
    def post(self, request):
        if request.method == 'POST':    
            # name = request.POST['namer']
            app = AppModelForm(request.POST, request.FILES)
            
            if app.is_valid():
                print("hello")
                s_app = app.save(commit=False)
                s_app.user = request.user
                app.save()
            
            return redirect('post')
        

        app = AppModel.objects.all()

        app2 = AppModelForm()
        context = {
            'app':app,
            'app2':app2
        }

        return render(request, 'post.html',
                        context)


    def update(self, request, id):
        if request.method == 'POST':
            name = request.POST['namer']

            app = AppModel.objects.get(id=id)
            
            return redirect('post')


        app = AppModel.objects.get(id=id)
        context = {
            'app':app
        }
        return render(request, 'update.html',
                        context)


    def delete(self, request, id):
        
        m = AppModel.objects.get(id=id)
        m.delete()

        return redirect('post')



class API(APIView):
    serializer_class = AppModelSerializer
    
    def get(self, request, *args, **kwargs):
        am = AppModel.objects.all()
        ams = AppModelSerializer(am, many=True)
        return Response(ams.data)

    def post(self, request, *args, **kwargs):
        ams = AppModelSerializer(data=request.data)
        if ams.is_valid():
            ams.save()
            return Response(ams.data)
        return Response(ams.errors)

    def put(self, request, id, *args, **kwargs):
        am = AppModel.objects.get(id=id)
        ams = AppModelSerializer(am, data=request.data)
        if ams.is_valid():
            ams.save()
            return Response(ams.data)
        return Response(ams.errors)

    def delete(self, request, id, *args, **kwargs):
        am = AppModel.objects.get(id=id)
        am.delete()
        data = {
            "success":"success"
        }
        return Response(data=data)


