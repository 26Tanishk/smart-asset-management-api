from enum import Enum


class AssetStatus(str, Enum):
    ACTIVE = "active"
    UNDER_MAINTENANCE = "under_maintenance"
    RETIRED = "retired"

ALLOWED_STATUS_TRANSITIONS = {
    "active": [
        "under_maintenance",
        "retired"
    ],

    "under_maintenance": [
        "active",
        "retired"
    ],

    "retired": []
}