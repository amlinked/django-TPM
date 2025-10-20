from django.shortcuts import render , redirect 
from django.contrib import messages

from django.utils.translation import gettext_lazy as _

from django.views.generic import CreateView
from accounts.forms import UserRegisterForm , UserProfileForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy

class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/register.html'
    # success_url = reverse_lazy('login')
    def get_success_url(self) :
        login(self.request , self.object) # type: ignore
        return reverse_lazy('project_list')
    
@login_required
def profile_view(request):  
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            # messages.success(request, _('Your profile has been updated successfully!'))
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
        
    return render(request, 'profile.html', {'form': form})
