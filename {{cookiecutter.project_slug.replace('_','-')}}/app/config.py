import os

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://sivpack:sivpack_dev@db:5432/sivdev')  # noqa
