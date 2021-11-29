from django.db.models import QuerySet
from rest_framework.request import Request
from rest_framework.response import Response
from employee.models import EmployeeModel, Counter
from employee.serializer import EmployeeSerializer


def get_all(request: Request) -> Response:
    employees: QuerySet[EmployeeModel] = EmployeeModel.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data, status=200)

def get_employee(request: Request, id: int) -> Response:
    employee: EmployeeModel = EmployeeModel.objects.get(id=id)
    serializer = EmployeeSerializer(employee)
    return Response(serializer.data, safe=False, status=200)

def count(request: Request) -> Response:
    counter: Counter = Counter.objects.all()[0]
    counter.count += 1
    counter.save()

    return Response(counter.count, status=200)
