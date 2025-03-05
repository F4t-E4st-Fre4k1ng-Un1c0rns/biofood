from enum import StrEnum


class UserRole(StrEnum):
    client = "client"
    staff = "staff"
    admin = "admin"


class OrderStatus(StrEnum):
    pending = "pending"
    accepted = "accepted"
    cooking = "cooking"
    ready = "ready"
    taken = "taken"
