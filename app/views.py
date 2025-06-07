from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response



class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

# AdminHOD Views
class AdminHODListView(ListView):
    model = AdminHOD
    template_name = 'app/adminhod_list.html'
class AdminHODCreateView(CreateView):
    model = AdminHOD
    fields = '__all__'
    template_name = 'app/adminhod_form.html'
    success_url = reverse_lazy('adminhod_list')
class AdminHODUpdateView(UpdateView):
    model = AdminHOD
    fields = '__all__'
    template_name = 'app/adminhod_form.html'
    success_url = reverse_lazy('adminhod_list')
class AdminHODDeleteView(DeleteView):
    model = AdminHOD
    template_name = 'app/adminhod_confirm_delete.html'
    success_url = reverse_lazy('adminhod_list')

# Staffs Views
class StaffsListView(ListView):
    model = Staffs
    template_name = 'app/staffs_adminhod_list.html'
class StaffsCreateView(CreateView):
    model = Staffs
    fields = '__all__'
    template_name = 'app/staffs_adminhod_form.html'
    success_url = reverse_lazy('staffs_list')
class StaffsUpdateView(UpdateView):
    model = Staffs
    fields = '__all__'
    template_name = 'app/staffs_adminhod_form.html'
    success_url = reverse_lazy('staffs_list')
class StaffsDeleteView(DeleteView):
    model = Staffs
    template_name = 'app/staffs_adminhod_confirm_delete.html'
    success_url = reverse_lazy('staffs_list')

# Courses Views
class CoursesListView(ListView):
    model = Courses
    template_name = 'app/courses_adminhod_list.html'
class CoursesCreateView(CreateView):
    model = Courses
    fields = '__all__'
    template_name = 'app/courses_adminhod_form.html'
    success_url = reverse_lazy('courses_list')
class CoursesUpdateView(UpdateView):
    model = Courses
    fields = '__all__'
    template_name = 'app/courses_adminhod_form.html'
    success_url = reverse_lazy('courses_list')
class CoursesDeleteView(DeleteView):
    model = Courses
    template_name = 'app/courses_adminhod_confirm_delete.html'
    success_url = reverse_lazy('courses_list')

    def post(self, request, *args, **kwargs):
        course = self.get_object()
        if course.subject_set.exists():
            messages.error(request, "Cannot delete course; it has related subjects.")
            return redirect('courses_list')
        return super().post(request, *args, **kwargs)

# Subjects Views
class SubjectsListView(ListView):
    model = Subjects
    template_name = 'app/subjects_adminhod_list.html'
class SubjectsCreateView(CreateView):
    model = Subjects
    fields = '__all__'
    template_name = 'app/subjects_adminhod_form.html'
    success_url = reverse_lazy('subjects_list')
class SubjectsUpdateView(UpdateView):
    model = Subjects
    fields = '__all__'
    template_name = 'app/subjects_adminhod_form.html'
    success_url = reverse_lazy('subjects_list')
class SubjectsDeleteView(DeleteView):
    model = Subjects
    template_name = 'app/subjects_adminhod_confirm_delete.html'
    success_url = reverse_lazy('subjects_list')

# Students Views
class StudentsListView(ListView):
    model = Students
    template_name = 'app/students_adminhod_list.html'
class StudentsCreateView(CreateView):
    model = Students
    fields = '__all__'
    template_name = 'app/students_adminhod_form.html'
    success_url = reverse_lazy('students_list')
class StudentsUpdateView(UpdateView):
    model = Students
    fields = '__all__'
    template_name = 'app/students_adminhod_form.html'
    success_url = reverse_lazy('students_list')
class StudentsDeleteView(DeleteView):
    model = Students
    template_name = 'app/students_adminhod_confirm_delete.html'
    success_url = reverse_lazy('students_list')

# Attendance Views
class AttendanceListView(ListView):
    model = Attendance
    template_name = 'app/attendance_adminhod_list.html'
class AttendanceCreateView(CreateView):
    model = Attendance
    fields = '__all__'
    template_name = 'app/attendance_adminhod_form.html'
    success_url = reverse_lazy('attendance_list')
class AttendanceUpdateView(UpdateView):
    model = Attendance
    fields = '__all__'
    template_name = 'app/attendance_adminhod_form.html'
    success_url = reverse_lazy('attendance_list')
class AttendanceDeleteView(DeleteView):
    model = Attendance
    template_name = 'app/attendance_adminhod_confirm_delete.html'
    success_url = reverse_lazy('attendance_list')

# AttendanceReport Views
class AttendanceReportListView(ListView):
    model = AttendanceReport
    template_name = 'app/attendancereport_adminhod_list.html'
class AttendanceReportCreateView(CreateView):
    model = AttendanceReport
    fields = '__all__'
    template_name = 'app/attendancereport_adminhod_form.html'
    success_url = reverse_lazy('attendancereport_list')
class AttendanceReportUpdateView(UpdateView):
    model = AttendanceReport
    fields = '__all__'
    template_name = 'app/attendancereport_adminhod_form.html'
    success_url = reverse_lazy('attendancereport_list')
class AttendanceReportDeleteView(DeleteView):
    model = AttendanceReport
    template_name = 'app/attendancereport_adminhod_confirm_delete.html'
    success_url = reverse_lazy('attendancereport_list')


def grade_list(request):
    grades = Grade.objects.select_related('student_id', 'subject_id').all()
    return render(request, 'app/grades_list_grades.html', {'grades': grades})


def grade_create(request):
    students = Students.objects.all()
    subjects = Subjects.objects.all()

    if request.method == 'POST':
        student_id = request.POST['student_id']
        subject_id = request.POST['subject_id']
        grade = request.POST['grade']
        remarks = request.POST.get('remarks', '')

        Grade.objects.create(
            student_id_id=student_id,
            subject_id_id=subject_id,
            grade=grade,
            remarks=remarks
        )
        messages.success(request, "Grade added successfully!")
        return redirect('grade_list')

    return render(request, 'app/grades_add_grades.html', {'students': students, 'subjects': subjects})


def grade_edit(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    students = Students.objects.all()
    subjects = Subjects.objects.all()

    if request.method == 'POST':
        grade.student_id_id = request.POST['student_id']
        grade.subject_id_id = request.POST['subject_id']
        grade.grade = request.POST['grade']
        grade.remarks = request.POST.get('remarks', '')
        grade.save()
        messages.success(request, "Grade updated successfully!")
        return redirect('grade_list')

    return render(request, 'app/grades_edit_grade.html', {'grade': grade, 'students': students, 'subjects': subjects})


def grade_delete(request, pk):
    grade = get_object_or_404(Grade, pk=pk)

    if request.method == 'POST':
        grade.delete()
        messages.success(request, "Grade deleted successfully!")
        return redirect('grade_list')

    return render(request, 'app/grades_delete_grades.html', {'grade': grade})

def home(request):
    students = Students.objects.all()
    courses = Courses.objects.all()
    subjects = Subjects.objects.all()
    attendance = Attendance.objects.all()
    grades = Grade.objects.all()

    context = {
        'students': students,
        'courses': courses,
        'subjects': subjects,
        'attendance': attendance,
        'grades': grades,
    }
    return render(request, 'app/home.html', context)