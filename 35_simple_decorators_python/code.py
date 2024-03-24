import functools
user = {"username": "jose", "access_level": "guest"}


def get_admin_password():
    return "1234"


print(get_admin_password())  # Can do this even though I'm a "guest"

# Now this only runs if I'm an admin... but
if user["access_level"] == "admin":
    print(get_admin_password())

print(get_admin_password())  # The function itself is still unsecured

# -- "secure" function --


def secure_get_admin():
    if user["access_level"] == "admin":
        print(get_admin_password())


# Now secure_get_admin() is secure.
# But get_admin_password() is still around, and I could call it:

secure_get_admin()
print(get_admin_password(), 'dupa')

# We want to get rid of get_admin_password so that only the secure function remains!
# Maybe something like this?


def secure_function(func):
    if user["access_level"] == "admin":
        return func


user = {"username": "bob", "access_level": "admin"}

get_admin_password = secure_function(get_admin_password)
print(get_admin_password(), 'dupa1')  # Error!

# When we ran `secure_function`, we checked the user's access level. Because at that point the user was not an admin, the function did not `return func`. Therefore `get_admin_password` is set to `None`.

# We want to delay overwriting until we run the function


def get_admin_password():
    return "1234"


def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()

    return secure_function


get_admin_password = make_secure(
    get_admin_password
)  # `get_admin_password` is now `secure_func` from above

user = {"username": "jose", "access_level": "guest"}
print(get_admin_password())  # Now we check access level

user = {"username": "bob", "access_level": "admin"}
print(get_admin_password())  # Now we check access level

# -- More information or error handling --





def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function
def get_admin_password():
    return "1234"

get_admin_password = make_secure(
    get_admin_password
)  # `get_admin_password` is now `secure_func` from above

user = {"username": "jose", "access_level": "guest"}
print(get_admin_password(), 'dupa')  # Now we check access level

user = {"username": "bob", "access_level": "admin"}
print(get_admin_password())  # Now we check access level

user = {"access" : "admin"}
def bezpieczna():
    return "jestem bezpieczna bo wykonam sie druga"


def ja_dekoruje(func):
    @functools.wraps(func)
    def jestem_udekorowana():
        if user['access'] == 'admin':
            return func()
        print("wykonam sie pierwsza i sprawdze czy mozna wykonac druga")
    return jestem_udekorowana


bezpieczna = ja_dekoruje(bezpieczna) # to jest nasz dekorator

print(bezpieczna())
print(bezpieczna.__name__)
