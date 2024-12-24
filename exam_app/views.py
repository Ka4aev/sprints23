from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .forms import Register
from django.views import generic
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User,Product,Order
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    products = Product.objects.order_by('-created_at')[:5]
    context = {'products': products}
    return render(request, 'catalog/index.html', context)

class RegisterView(generic.CreateView):
    template_name = 'registration/register.html'
    form_class = Register
    success_url = reverse_lazy('login')

def logout_user(request):
    logout(request)
    return redirect('home')

class Profile(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = 'catalog/profile.html'
    context_object_name = 'profile_user'

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(user=self.request.user)
        return context

class ServiceList(generic.ListView):
    model = Product
    template_name = 'catalog/service.html'
    context_object_name = 'products'

class ServiceDetail(generic.DetailView):
    model = Product
    template_name = 'catalog/service_detail.html'
    context_object_name = 'product'

def create_order(request, pk):
    product = Product.objects.get(pk=pk)
    Order.objects.create(user=request.user, product=product)
    return HttpResponseRedirect(reverse('profile'))

class SearchResultsView(generic.ListView):
    model = Product
    template_name = 'catalog/service.html'
    context_object_name = 'results'

    def get_queryset(self):
        query = self.request.GET.get('search', '')
        return Product.objects.filter(name__icontains=query) if query else []