import os
print("Hello from Docker!")
print(f"Environment variable: {os.getenv('MY_VAR', 'Not set')}")
