from fastapi import FastAPI
from app.config import settings
from app.middleware import TimingMiddleware
from app.exceptions import AppError, app_error_handler

app = FastAPI(title=settings.app_name)
app.add_middleware(TimingMiddleware)
app.add_exception_handler(AppError, app_error_handler)


@app.get("/health")
def health():
    return {"status": "ok"}


from app.routers import user
app.include_router(user.router)
from app.routers import organization
app.include_router(organization.router)
from app.routers import project
app.include_router(project.router)
from app.routers import task
app.include_router(task.router)
from app.routers import comment
app.include_router(comment.router)
from app.routers import tag
app.include_router(tag.router)
from app.routers import invoice
app.include_router(invoice.router)
from app.routers import payment
app.include_router(payment.router)
from app.routers import notification
app.include_router(notification.router)
from app.routers import webhook
app.include_router(webhook.router)
from app.routers import api_key
app.include_router(api_key.router)
from app.routers import audit_log
app.include_router(audit_log.router)
