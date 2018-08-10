from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='ew4peb%u0qi2r*igg^5$m#wh4l+e7^-9h7codkl)uilvopyqfa')

DEBUG = env.bool('DJANGO_DEBUG', default=True)