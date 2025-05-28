from django.shortcuts import render, redirect
from .forms import StudentProfileForm
from .models import StudentProfile
from django.db.models import Avg

def create_profile(request):
    if request.method == 'POST':
        form = StudentProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profiles_list')
    else:
        form = StudentProfileForm()
    return render(request, 'profile_app/create_profile.html', {'form': form})

def profiles_list(request):
    sort_by = request.GET.get('sort', 'name')
    direction = request.GET.get('direction', 'asc')
    selected_program = request.GET.get('program', '')

    profiles = StudentProfile.objects.all()

    if selected_program:
        profiles = profiles.filter(program=selected_program)

    if direction == 'desc':
        order = '-' + sort_by
    else:
        order = sort_by

    profiles = profiles.order_by(order)

    avg_gpa = profiles.aggregate(Avg('gpa'))['gpa__avg']
    programs = StudentProfile.objects.values_list('program', flat=True).distinct()

    context = {
        'profiles': profiles,
        'avg_gpa': avg_gpa,
        'programs': programs,
        'selected_program': selected_program,
        'current_sort': sort_by,
        'current_direction': direction,
    }

    return render(request, 'profile_app/profiles_list.html', context)
