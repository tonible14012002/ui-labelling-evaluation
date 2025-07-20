
class CustomException(Exception):
    status_code = 500
    error = "Geocode API Error"
    pass