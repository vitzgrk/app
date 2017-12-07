from django.http import HttpResponse, JsonResponse
import json
from .models import *

def create_user(request):
    if request.is_ajax() and not (User.objects.filter(inn__contains = request.POST['inn']) or User.objects.filter(name__contains = request.POST['name'])): 
        u = User.objects.create(**request.POST.dict())
        u.save()
        return JsonResponse({'status': 'Пользователь добавлен'}, safe=False)
    else:
        data = {'status': "Пользователь с указанным данными уже существует!"}
        return JsonResponse(data, safe=False)


def show(request):
    data = [i for i in User.objects.values()]
    return JsonResponse(data, safe=False)

def get_user_info(request):
    u = User.objects.get(name = request.POST['name'])
    data = {
        'name' : u.name,
        'inn' : u.inn,
        'email' : u.email,
        'balance': u.balance
    }
    return JsonResponse(data)

def check_balance(request):
    # print(request.POST)
    amount = float(request.POST['amount'])
    from_name = request.POST['from_name']
    from_current_amount = float(User.objects.get(name = from_name).balance)
    inns = [int(i) for i in json.loads(request.POST['inns'])]
    print(amount/float(len(inns)))
    valid_inns = 0
    for inn in inns:            
            if User.objects.filter(inn = inn).exists():
                valid_inns+=1
    if from_current_amount < amount:
        return JsonResponse({"status": "Недостаточно средств для списания!"})
    else:        
        for inn in inns:            
            if User.objects.filter(inn = inn).exists():                
                print(valid_inns)
                current_balance = float(User.objects.get(inn = inn).balance)
                new_balance = current_balance + amount / float(valid_inns)
                User.objects.filter(inn = inn).update(balance = new_balance)
                User.objects.filter(name = from_name).update(balance = from_current_amount-amount)
            else:
                return JsonResponse({"status": "Пользователь с ИНН {} не существует! Указанная сумма будет распределена между остальными участниками.".format(inn)})
        return JsonResponse({"status": "Транзакция прошла успешно!"})
    return HttpResponse()