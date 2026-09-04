from .celery import app as celery_app


# this will load up the celery app once the django starts
__all__ = ('celery_app',)