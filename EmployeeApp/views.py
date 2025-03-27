from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse, HttpRequest,HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings


from EmployeeApp.models import Departments, Employees
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer
# Create your views here.

# Api for Department tables
@csrf_exempt
# """ Handles CRUD operations for the Department model.
#     Supports GET, POST, PUT, and DELETE requests."""
def departmentApi(request, id=0):
    # Handle GET request: Retrieve all departments
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data,safe=False)
    
     # Handle POST request: Create a new department
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Fail to Add", safe=False)
     # Handle PUT request: Update a new department
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        departments_serializer = DepartmentSerializer(department, data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        try:
            department = Departments.objects.get(DepartmentId=id)
            department.delete()
            return JsonResponse("Deleted Successfully", safe=False)
        except ObjectDoesNotExist:
            return JsonResponse({"error": "Department not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
# Api for Employee table    
@csrf_exempt
def employeeApi(request, id=None):
    if request.method == "GET":
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employees_serializer = EmployeeSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == "PUT":
        employee_data = JSONParser().parse(request)
        employee = Employees.objects.get(EmployeeId= employee_data['EmployeeId'])
        employees_serializer = EmployeeSerializer(employee, data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        try:
            employee = Employees.objects.get(EmployeeId=id)
            employee.delete()
            return JsonResponse("Deleted Successfully", safe=False)
        except ObjectDoesNotExist:
            return JsonResponse({'error':"Employee Not Found"}, status=404)
        except Exception as e:
            return JsonResponse({"Error": str(e)}, status=500)
            
@csrf_exempt
#     """Handles file uploads for employee photos."""
def save_file(request: HttpRequest) -> JsonResponse:
    """Handles file uploads for employee photos."""
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        file_path = default_storage.save(f"Photos/{file.name}", ContentFile(file.read()))  # Store in 'Photos/' folder

        file_url = f"{settings.MEDIA_URL}{file_path}"  # Generate the accessible file URL
        return JsonResponse({"message": "File uploaded successfully", "file_url": file_url}, status=201)

    return JsonResponse({"error": "No file uploaded"}, status=400)
