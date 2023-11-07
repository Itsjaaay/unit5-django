from django.http import JsonResponse

def near_hundred(request, num):
    # Parse 'num' from the URL path and solve the Codingbat challenge
    num = int(num)
    result = abs(100 - num) <= 10 or abs(200 - num) <= 10
    
    # Return the result as a JSON response
    response_data = {'result': result}
    return JsonResponse(response_data)