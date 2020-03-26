class InternalServerError(Exception):
    pass


class NotFoundError(Exception):
    pass


errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    "NotFoundError": {
        "message": "Not found",
        "status": 404
    }
}
