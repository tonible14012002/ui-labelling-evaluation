

class GoogleGeocodeException(Exception):
    status_code = 500
    error = "Geocode API Error"
    pass

class DatabaseMutationException(Exception):
    status_code = 500
    pass

# DB Exceptions
class RecordNotFoundException(Exception):
    status_code = 404
    error = "Record Not Found"
    pass