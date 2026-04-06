from enum import Enum, unique


@unique
class UserPermissions(Enum):
    ADD_TRANSACTION   = 0b0001
    ADD_BUDGET        = 0b0010
    LIST_TRANSACTION  = 0b0100
    EDIT_TRANSACTION  = 0b1000
    DELETE_TRANSACTION= 0b10000
    
def has_permission(user_permissions: int, permission: UserPermissions) -> bool:
    if user_permissions == -1:
        return True
    return (user_permissions & permission.value) == permission.value