from .base import *

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DEBUG = True



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':get_secret('DB_NAME'), # para el resto de las variables sensibles se haría lo mismo
        'USER':'miguelro33',
        'PASSWORD':'Daniro11',
        'HOST':'localhost',
        'PORT':'5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(Path(__file__).resolve().parent.parent.parent, 'static')]
MEDIA_URL ='/media/'
MEDIA_ROOT = os.path.join(Path(__file__).resolve().parent, 'media')

# Ahora vienen las configuraciones locales de acceso al e-mail
# E-MAIL SETTINGS
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'frrgcsocial@gamil.com'
EMAIL_HOST_PASSWORD ='******' # Ver en el vídeo cómo ocultarlo
EMAL_PORT = 587
