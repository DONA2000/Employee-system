from django.urls import path
from .views import EmployeeCreateView,EmployeeListView,EmployeeUpdateView,EmployeeDeleteView,EmployeeDetailView

urlpatterns=[
    # path('',DisplayView.as_view(), name='employee'),
    path('',EmployeeCreateView.as_view(), name='employee_create'),
    path('/EmployeeListView',EmployeeListView.as_view(), name='employee_list'),
    path('update/<int:pk>/',EmployeeUpdateView.as_view(), name='employee_update'),
    path('delete/<int:pk>/',EmployeeDeleteView.as_view(), name='employee_delete'),
    path('detail/<int:pk>/',EmployeeDetailView.as_view(), name='employee_detail')
]