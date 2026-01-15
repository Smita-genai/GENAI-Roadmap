"""
Standard Library modules demonstration.
Shows practical examples of commonly used modules from Python's standard library:
- random: Generate random numbers and choices
- os: File and directory operations
- json: Data serialization and deserialization
- datetime: Date and time operations
- time: Time-related functions
- re: Regular expression pattern matching
"""

import random
import os
import json
from datetime import datetime, timedelta
import time
import re


def demo_random():
    """Demonstrate random module functions."""
    print("=== Random Module ===")
    print(random.randint(1, 20))
    print(random.choice(["Smita", "Jay", "Pradeep"]))


def demo_os():
    """Demonstrate os module functions."""
    print("\n=== File and Directory Access ===")
    print(os.getcwd())
    # Note: Uncomment to create a test directory
    # os.mkdir("Test_Directory")


def demo_json():
    """Demonstrate JSON serialization and deserialization."""
    print("\n=== Data Serialization (JSON) ===")
    
    # Dictionary
    data = {'name': 'Jay', 'age': 25}
    
    # Converting to JSON string
    json_str = json.dumps(data)
    print(json_str)
    print(type(json_str))
    
    # Converting String to Dictionary
    parsed_data = json.loads(json_str)
    print(parsed_data)
    print(type(parsed_data))


def demo_datetime():
    """Demonstrate datetime module functions."""
    print("\n=== DateTime Operations ===")
    
    now = datetime.now()  # Current date and time
    print(now)
    
    yesterday = now - timedelta(days=1)
    print(yesterday)


def demo_time():
    """Demonstrate time module functions."""
    print("\n=== Time Module ===")
    
    print(time.time())
    time.sleep(2)
    print(time.time())


def demo_regex():
    """Demonstrate regular expressions."""
    print("\n=== Regular Expressions ===")
    
    pattern = r'\d+'
    text = "There are 50 oranges"
    match = re.search(pattern, text)
    print(match.group())


if __name__ == "__main__":
    demo_random()
    demo_os()
    demo_json()
    demo_datetime()
    demo_time()
    demo_regex()
