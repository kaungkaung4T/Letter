from django.shortcuts import render, redirect

# Create your views here.

from django.core.mail import send_mail, EmailMessage
class home:
    def index(self, request):
        if request.method == "POST":
            title = "title"
            body = "wefiwefjiowejfoiewf"
            e = EmailMessage(subject=title, body=body, from_email="mrkaungminnkhan@gmail.com",
                             to=['kaungminkhant4t99@gmail.com'])
            e.send()
            return redirect("/")

        return render(request, 'index.html')


