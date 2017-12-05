from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm
from django.views import generic
from .models import Reservation
from django.views.generic.edit import CreateView

class HomeView(generic.ListView):
    template_name = 'accounts/home.html'
    context_object_name = 'all_reservations'

    def get_queryset(self):
        return Reservation.objects.all()

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)

class ReservationView(generic.DetailView):
    model = Reservation
    template_name = 'accounts/reservations.html'

class ReservationCreate(CreateView):
    model = Reservation
    fields = ['userid','roomid','time1', 'time2']