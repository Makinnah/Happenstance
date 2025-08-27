import os
import django

# Step 1: Point to your Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Happenstance.settings')

# Step 2: Set up Django
django.setup()

# Step 3: Access settings
from django.conf import settings

# Step 4: Retrieve database config
db_config = settings.DATABASES.get('default', {})
db_name = db_config.get('NAME', 'Not set')
db_user = db_config.get('USER', 'Not set')

# Step 5: Print results
print(f"Database Name: {db_name}")
print(f"Database User: {db_user}")
