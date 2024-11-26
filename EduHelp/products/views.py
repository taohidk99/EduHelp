from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from .forms import CourseForm

# Add a new course
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()  
            return redirect('home')  
    else:
        form = CourseForm()  
    return render(request, 'courseform.html', {'form': form})  

# Update an existing course
def update_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id) 
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)  
        if form.is_valid():
            form.save()  
            return redirect('course') 
    else:
        form = CourseForm(instance=course) 
    return render(request, 'courseform.html', {'form': form})  


def delete_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)  
    course.delete()  
    return redirect('course')