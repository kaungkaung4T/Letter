from django.shortcuts import render

# Create your views here.


class home:
    def index(self, request):
        return render(request, 'index.html')