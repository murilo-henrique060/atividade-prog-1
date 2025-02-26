file_path = "data/usuarios.csv"
user_fields = ['id', 'name', 'email', 'password'] 

def create_file() -> None:
    """Creates the file that will store the users data.
    """

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(",".join(user_fields) + '\n')

def get_all() -> list:
    """Returns all users from the database. If the file does not exist, it creates it.

    Returns:
        list: List of users.
    """

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return [dict(zip(user_fields, line.strip().split(","))) for line in file.readlines()[1:]]
    except FileNotFoundError:
        create_file()
        return []
    
def get_by_email(email: str) -> dict | None:
    """Returns a user by email.

    Args:
        email (str): User email.

    Returns:
        dict | None: User data.
    """

    users = get_all()
    for user in users:
        if user["email"] == email:
            return user
    return None

def create_user(user_data: dict) -> dict:
    """Creates a new user.

    Args:
        user_data (dict): User data.

    Returns:
        dict: User data.
    """

    users = get_all()
    last_id = int(users[-1]["id"])
    user_data["id"] = str(last_id + 1)

    with open(file_path, "a", encoding="utf-8") as file:
        file.write(",".join([str(user_data[field]) for field in user_fields]) + '\n')

    return user_data