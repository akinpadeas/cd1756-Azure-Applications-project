"""
This script runs the FlaskWebProject application using a development server.
"""

#from os import environ
#from FlaskWebProject import app

#if __name__ == '__main__':
#    HOST = environ.get('SERVER_HOST', 'localhost')
#    try:
#        PORT = int(environ.get('SERVER_PORT', '5555'))
#    except ValueError:
#        PORT = 5555
#    app.run(HOST, PORT, ssl_context='adhoc')

from os import environ
from FlaskWebProject import app

if __name__ == '__main__':
    # Detect environment (local vs. production)
    ENV = environ.get('FLASK_ENV', 'development')  # Default to 'development' for local

    if ENV == 'production':
        # In production, Azure Web App handles host, port, and SSL
        app.run()  # Let Azure manage the configuration
    else:
        # Local development settings
        HOST = environ.get('SERVER_HOST', 'localhost')
        try:
            PORT = int(environ.get('SERVER_PORT', '5555'))
        except ValueError:
            PORT = 5555
        app.run(HOST, PORT, ssl_context='adhoc')  # Enable HTTPS locally
