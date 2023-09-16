from .database import get_user_by_email


def is_email_taken(email: str) -> bool:
    user = get_user_by_email(email)
    return True if user else False
