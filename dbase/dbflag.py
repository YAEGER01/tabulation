import platform
from django.conf import settings

def ensure_database_exists():
    """
    Ensures the database exists (for MySQL). In Django, this is handled by migrations.
    """
    from django.db import connections
    db_name = settings.DATABASES['default']['NAME']
    try:
        with connections['default'].cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}`;")
    except Exception as e:
        print(f"Database creation failed: {e}")
        return False
    return True

def get_pc_name():
    return platform.node()

titlename = "MR PASUC 2017"
    try:
        # Connect to the 'mysql' database to create a new one
        with connections['default'].cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}`;")
    except OperationalError as e:
        print(f"Database creation failed: {e}")
        return False
    return True

def get_machine_name():
    import platform
    return platform.node()

if __name__ == "__main__":
    # Example usage: create the database and print machine name
    db_name = settings.DATABASES['default']['NAME']
    created = create_database_if_not_exists(db_name)
    if created:
        print(f"Database '{db_name}' ensured.")
    print(f"Machine name: {get_machine_name()}")
