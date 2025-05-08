from typing import Dict, List, Optional
from totem.notifications.services import send_notification_to_user
from totem.users.models import User


def notify_users(users: List[User], title: str, body: str, data: Optional[Dict[str, str]] = None) -> Dict[int, bool]:
    """
    Send a notification to multiple users

    Args:
        users: List of User instances or user IDs
        title: Notification title
        body: Notification body
        data: Additional data payload

    Returns:
        dict: Mapping of user IDs to success status
    """
    results = {}
    for user in users:
        results[user.pk] = send_notification_to_user(user, title, body, data)
    return results
