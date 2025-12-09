#!/usr/bin/env python
import os
import sys
import django
from django.conf import settings
from django.test.utils import get_runner

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tabulatorMsSanfermin.settings")
    django.setup()
    
    # Test basic connectivity
    from django.test.client import Client
    from django.urls import reverse
    
    client = Client()
    
    print("Testing Django connectivity...")
    try:
        response = client.get('/')
        print(f"GET / Status: {response.status_code}")
        print(f"Response content length: {len(response.content)}")
        
        # Test POST login
        response = client.post('/', {
            'username': 'admin2025',
            'cpass': 'adminpass2025'
        })
        print(f"POST / Status: {response.status_code}")
        print(f"Response location: {response.get('Location', 'None')}")
        
    except Exception as e:
        print(f"Error: {e}")