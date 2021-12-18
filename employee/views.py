from django.db.models import QuerySet
from rest_framework.request import Request
from rest_framework.response import Response
from employee.models import EmployeeModel, Counter
from employee.serializer import EmployeeSerializer
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse

@api_view(('GET',))
def get_all(request: Request) -> Response:
    employees: QuerySet[EmployeeModel] = EmployeeModel.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return JsonResponse(serializer.data, status=200, safe=False)

@api_view(('GET',))
def get_employee(request: Request, id: int) -> Response:
    employee: EmployeeModel = EmployeeModel.objects.get(id=id)
    serializer = EmployeeSerializer(employee)
    return JsonResponse(serializer.data, safe=False, status=200)


@api_view(('GET',))
def count(request: Request) -> Response:
    try:
        counter: Counter = Counter.objects.get(id=1)
    except:
        counter: Counter = Counter(id=1)

    counter.count += 1
    counter.save()

    return JsonResponse(counter.count, status=200, safe=False)
