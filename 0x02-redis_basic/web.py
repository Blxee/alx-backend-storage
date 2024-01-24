#!/usr/bin/env python3
"""5. Implementing an expiring web cache and tracker."""
import requests


def get_page(url: str) -> str:
    """Retrieves the content of an html page."""
    return requests.get(url, timeout=10).text
