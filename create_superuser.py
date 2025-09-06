import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
User = get_user_model()

# Default to 'admin' if environment variables are not set
username = os.environ.get('API_USER', 'admin')
password = os.environ.get('API_PASS', 'admin')

if not User.objects.filter(username = username).exists():
    User.objects.create_superuser(username = username, password = password)
    print(f"Superuser '{username}' created.")
else:
    print(f"Superuser '{username}' already exists.")
