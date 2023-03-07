from rest_framework.exceptions import APIException

"""Custom errors"""


class ImageNotFound(APIException):
    status_code = 404
    default_detail = "The requested image does not exist"


class TimeValueError(APIException):
    status_code = 400
    default_detail = "The value should be in range 300 - 30000 seconds"


class LinkExpiredError(APIException):
    status_code = 200
    default_detail = "This link expired"


