from enum import Flag

class Role(Flag):
    OWNER = 8
    POWER_USER = 4
    USER = 2
    SUPERVISOR = 1
    ADMIN = OWNER | POWER_USER | USER | SUPERVISOR


john_roles = Role.USER | Role.SUPERVISOR
john_roles


type(john_roles)


if Role.USER in john_roles:
    print("John, you're a user")



if Role.SUPERVISOR in john_roles:
    print("John, you're a supervisor")



print(Role.OWNER in Role.ADMIN)
print(Role.SUPERVISOR in Role.ADMIN)
# Role.ADMIN + 1 this is not supported
