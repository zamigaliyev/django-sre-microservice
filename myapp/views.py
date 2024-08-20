from django.http import JsonResponse


import logging
from django.http import JsonResponse

logger = logging.getLogger('my_logger')


def my_view(request):
    params = request.GET
    try:
        logger.info(f"Received request with params: {params}")
        # Burada bəzi kodlar istisna halı yarada bilər
        return JsonResponse({"message": "Hello, World!", "params": params})
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        return JsonResponse({"message": "An error occurred", "error": str(e)}, status=500)


