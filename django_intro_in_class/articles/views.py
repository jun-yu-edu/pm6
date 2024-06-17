from django.http import HttpResponse, JsonResponse
# Create your views here.

def data(request):
    return HttpResponse("여러분! 정신 차리세요!")

def json_data(request):
    data = {"name": "Jun", "age": 17, "city": "Seoul"}
    return JsonResponse(data)

def hello(request):
    return HttpResponse("안녕!")    

def random_data(request, num):
    data = {
        'my_num' : num
    }
    return JsonResponse(data)

def hello_name(request, name):
    # name아 안녕!
    text = f'{name}아 안녕!'

    # if name.종성 존재 :
    #     text = f'{name}아 안녕!'
    # elif name.종성 존재 X :
    #     text = f'{name}야 안녕!'

    return HttpResponse(text)    

