import re       #regex = regular expressions

def is_valid_email(email:str)-> bool:
    """Valida si el email tiene el formato correcto"""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None