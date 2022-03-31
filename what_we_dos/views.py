from django.shortcuts import get_object_or_404, render
from .models import What_DO

# Create your views here.
def what_we_dos(request):
    what_dos = What_DO.objects.filter(is_featured = True)
    data = {
        'what_dos': what_dos,
    } 
    
    return render(request, 'what_we_dos/what_we_dos.html', data)
def what_do_details(request, id):
    single_what = get_object_or_404(What_DO, pk=id)
    data = {
        'single_what': single_what,
    } 
    
    return render(request, 'what_we_dos/what_do_details.html',data)