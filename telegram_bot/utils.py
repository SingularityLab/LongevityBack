```python
import re

def validate_test_results(test_results):
    """
    Validate the format of the test results.
    """
    # This is a simple validation. You may need to adjust it based on your actual test results format.
    if not isinstance(test_results, dict):
        return False

    for key, value in test_results.items():
        if not isinstance(key, str) or not isinstance(value, (int, float)):
            return False

    return True

def validate_telegram_username(username):
    """
    Validate the format of the telegram username.
    """
    if not isinstance(username, str):
        return False

    # Telegram username should be 5-32 characters long, start with a letter, and may contain letters, numbers and underscores.
    if not re.match(r'^[a-zA-Z][a-zA-Z0-9_]{4,31}$', username):
        return False

    return True
```