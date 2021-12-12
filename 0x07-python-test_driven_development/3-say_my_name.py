#!/usrr/bin/python3
"""
Say my name
"""
def say_my_name(first_name, last_name=""):
    """Prints first name and last name and first_name and last_name must be str
    Args:
        first_name: first name must be str type
        last_name: last name must be str type if not given it will be empty
    """
    if (type(first_name) is not str):
        raise TypeError("first_name must be a string")
    if (type(last_name) is not str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
