from django.urls import path
from .views import *
from . import views
from .views import AboutPageView



urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    # AdminHOD
    path('adminhod/', AdminHODListView.as_view(), name='adminhod_list'),
    path('adminhod/create/', AdminHODCreateView.as_view(), name='adminhod_create'),
    path('adminhod/update/<int:pk>/', AdminHODUpdateView.as_view(), name='adminhod_update'),
    path('adminhod/delete/<int:pk>/', AdminHODDeleteView.as_view(), name='adminhod_delete'),

    # Staffs
    path('staffs/', StaffsListView.as_view(), name='staffs_list'),
    path('staffs/create/', StaffsCreateView.as_view(), name='staffs_create'),
    path('staffs/update/<int:pk>/', StaffsUpdateView.as_view(), name='staffs_update'),
    path('staffs/delete/<int:pk>/', StaffsDeleteView.as_view(), name='staffs_delete'),

    # Courses
    path('courses/', CoursesListView.as_view(), name='courses_list'),
    path('courses/create/', CoursesCreateView.as_view(), name='courses_create'),
    path('courses/update/<int:pk>/', CoursesUpdateView.as_view(), name='courses_update'),
    path('courses/delete/<int:pk>/', CoursesDeleteView.as_view(), name='courses_delete'),

    # Subjects
    path('subjects/', SubjectsListView.as_view(), name='subjects_list'),
    path('subjects/create/', SubjectsCreateView.as_view(), name='subjects_create'),
    path('subjects/update/<int:pk>/', SubjectsUpdateView.as_view(), name='subjects_update'),
    path('subjects/delete/<int:pk>/', SubjectsDeleteView.as_view(), name='subjects_delete'),

    # Students
    path('students/', StudentsListView.as_view(), name='students_list'),
    path('students/create/', StudentsCreateView.as_view(), name='students_create'),
    path('students/update/<int:pk>/', StudentsUpdateView.as_view(), name='students_update'),
    path('students/delete/<int:pk>/', StudentsDeleteView.as_view(), name='students_delete'),

    # Attendance
    path('attendance/', AttendanceListView.as_view(), name='attendance_list'),
    path('attendance/create/', AttendanceCreateView.as_view(), name='attendance_create'),
    path('attendance/update/<int:pk>/', AttendanceUpdateView.as_view(), name='attendance_update'),
    path('attendance/delete/<int:pk>/', AttendanceDeleteView.as_view(), name='attendance_delete'),

    # AttendanceReport
    path('attendancereport/', AttendanceReportListView.as_view(), name='attendancereport_list'),
    path('attendancereport/create/', AttendanceReportCreateView.as_view(), name='attendancereport_create'),
    path('attendancereport/update/<int:pk>/', AttendanceReportUpdateView.as_view(), name='attendancereport_update'),
    path('attendancereport/delete/<int:pk>/', AttendanceReportDeleteView.as_view(), name='attendancereport_delete'),

    path('grades/', views.grade_list, name='grade_list'),
    path('grades/add/', views.grade_create, name='grade_create'),
    path('grades/edit/<int:pk>/', views.grade_edit, name='grade_edit'),
    path('grades/delete/<int:pk>/', views.grade_delete, name='grade_delete'),

    path('', views.home, name='home'),
]

