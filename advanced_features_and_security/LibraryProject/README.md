# Advanced Features and Security - Custom User Model

This Django project demonstrates the implementation of a custom user model with additional fields and functionality.

## Features Implemented

### 1. Custom User Model
- **Location**: `accounts/models.py`
- **Base Class**: `AbstractUser`
- **Additional Fields**:
  - `date_of_birth`: DateField for storing user's birth date
  - `profile_photo`: ImageField for storing user profile pictures

### 2. Custom User Manager
- **Location**: `accounts/models.py`
- **Class**: `CustomUserManager`
- **Methods**:
  - `create_user()`: Creates regular users with additional fields
  - `create_superuser()`: Creates admin users with proper permissions

### 3. Django Admin Integration
- **Location**: `accounts/admin.py`
- **Class**: `CustomUserAdmin`
- **Features**:
  - Custom list display with additional fields
  - Enhanced filtering options
  - Search functionality
  - Organized fieldsets for better UX

### 4. Settings Configuration
- **Location**: `LibraryProject/settings.py`
- **Key Settings**:
  - `AUTH_USER_MODEL = 'accounts.CustomUser'`
  - Media files configuration for profile photos
  - Added 'accounts' app to INSTALLED_APPS

## Project Structure

```
advanced_features_and_security/LibraryProject/
├── accounts/                    # Custom user app
│   ├── models.py               # CustomUser and CustomUserManager
│   ├── admin.py                # CustomUserAdmin configuration
│   └── migrations/             # Database migrations
├── LibraryProject/
│   ├── settings.py             # Updated with custom user model
│   └── urls.py                 # Media files serving configuration
└── media/                      # Directory for uploaded profile photos
    └── profile_photos/         # Profile photo uploads
```

## Usage

### Creating Users Programmatically

```python
from accounts.models import CustomUser

# Create a regular user
user = CustomUser.objects.create_user(
    username='john_doe',
    email='john@example.com',
    password='secure_password',
    date_of_birth='1990-01-01'
)

# Create a superuser
admin = CustomUser.objects.create_superuser(
    username='admin',
    email='admin@example.com',
    password='admin_password'
)
```

### Admin Interface
1. Run the development server: `python manage.py runserver`
2. Navigate to `/admin/`
3. Login with superuser credentials
4. Manage users with the enhanced admin interface

## Database Migrations

The project includes proper migrations for the custom user model:

```bash
python manage.py makemigrations accounts
python manage.py migrate
```

## Security Considerations

- Profile photos are stored in a dedicated media directory
- Custom user manager ensures proper user creation
- Admin interface provides secure user management
- All Django security best practices are maintained

## Dependencies

- Django 5.2.1
- Pillow (for ImageField support)

## Installation

1. Install required packages:
   ```bash
   pip install Django Pillow
   ```

2. Run migrations:
   ```bash
   python manage.py migrate
   ```

3. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

4. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Testing

The custom user model can be tested through:
- Django admin interface
- Django shell for programmatic testing
- Unit tests (can be added in `accounts/tests.py`)