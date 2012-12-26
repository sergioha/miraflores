import datetime

def get_fechahora():
    """
    Retorna un objeto con la fecha y hora actual.
    """
    try:
        from django.utils import timezone
        return timezone.now()
    except ImportError:
        return datetime.datetime.now()
