from fastapi.utils import is_body_allowed_for_status_code
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse, PlainTextResponse, Response
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from starlette.status import HTTP_400_BAD_REQUEST


async def http_exception_handler(request: Request, exc: HTTPException) -> Response:
    headers = getattr(exc, "headers", None)
    if not is_body_allowed_for_status_code(exc.status_code):
        return Response(status_code=exc.status_code, headers=headers)
    return JSONResponse({"detail": exc.detail}, status_code=exc.status_code, headers=headers)


async def unhandled_exception_handler(request: Request, exc: Exception) -> PlainTextResponse:
    """
    This middleware will log all unhandled exceptions.
    Unhandled exceptions are all exceptions that are not HTTPExceptions or RequestValidationErrors.
    """
    headers = getattr(exc, "headers", None)
    status_code = getattr(exc, "status_code", 500)
    error = getattr(exc, "error", "Internal Server Error")

    return JSONResponse({
        "message": str(exc),
        "error": error,
    }, status_code=status_code, headers=headers)

async def request_validation_exception_handler(request: Request, exc: RequestValidationError) -> Response:
    return JSONResponse(
        status_code=HTTP_400_BAD_REQUEST,
        content={"detail": jsonable_encoder(exc.errors())},
    )