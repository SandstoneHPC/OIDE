import os
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))



DEBUG = True
LOGIN_URL = '/auth/login'
COOKIE_SECRET = 'YouShouldProbablyChangeThisValueForYourProject'

TERMINAL_API_KEY = 'GateOneAPIKey'
TERMINAL_SECRET = 'GateOneServerSecret'
GATEONE_URL = 'https://localhost:10443'
GATEONE_ORIGINS_URL = 'http://localhost:8888'
GATEONE_STATIC_URL = 'https://remotehost:10443'

MONGO_URI = 'localhost'
MONGO_PORT = 27017

INSTALLED_MODULES = (
        {
            'name': 'Code Editor',
            'link': '/codeeditor',
            'description': 'A simple online editor for your code and other files.'
        },
        {
            'name': 'File Browser',
            'link': '/filebrowser',
            'description': 'A powerful online file browser.'
        },
        {
            'name': 'Web Terminal',
            'link': '/webterminal',
            'description': 'The GateOne web terminal.'
        },
        {
            'name': 'Testing Grounds',
            'link': '/test',
            'description': 'Open space for testing new features.'
        },
    )

FILESYSTEM_ROOT_DIRECTORIES = (
    '/home/{{USERNAME}}/',
    '/tmp/',
    )

NGINX_UPLOAD_DIR = '/tmp/oide-upload'

try:
    from local_settings import *
except:
    pass
