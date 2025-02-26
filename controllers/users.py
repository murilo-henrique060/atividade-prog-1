from services.users import get_by_email

user = None

def login(email: str, password: str) -> dict | None:
  global user

  user_data = get_by_email(email)

  if user_data and user_data["password"] == password:
    user = user_data
    return user_data
  return None