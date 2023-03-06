from rest_framework.exceptions import APIException


class ImageNotFound(APIException):
    status_code = 404
    default_detail = "The requested image does not exist"
