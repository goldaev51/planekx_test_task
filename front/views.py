from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def data_schemas(request):
    return render(request, template_name='front/data_schemas.html')
