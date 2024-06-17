from django.http import HttpResponse, JsonResponse
# Create your views here.

def data(request):
    return HttpResponse("here is your response from the server.")

# def json_data(request):
#     data = {"name": "Jun", "age": 17, "city": "Seoul"}
#     return JsonResponse(data)

# def random_data(request, num):
#     data = {
#         'my_num' : num
#     }
#     return JsonResponse(data)

