from django.views.generic import TemplateView
from django.views.generic import View
from . forms import UserForm
from django.shortcuts import render


class HomePage(TemplateView):
    template_name = 'site_index.html'

class UserFormView(View):
    form_class = UserForm
    template_name = 'registration.html'

    #display a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    #process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            #cleaned and normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #to change password
            user.set_password(password)
            user.save()


            #returns user objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('music:info')

        return render(request, self.template_name, {'form':form})
