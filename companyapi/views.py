from django.http import HttpResponse, JsonResponse


# this method is just for sending any response from django to the client
def HomePage(request):
    print("Home page rerquested")
    return HttpResponse("This is a response")


# this method id for sendng JSON response to the client
def JsonResp(request):
    users = {"users":["User 1","User 2","User 3","User 4",]}
    return JsonResponse(users)

def GetOnlyList(request):
    users = ["User 1","User 2","User 3","User 4",]
    return JsonResponse(users, safe=False)