import logging
from flask import Flask

app = Flask(__name__)
wsgi_app = app.wsgi_app
# TODO: Set the app's logger level to "warning"
#   and any other necessary changes
app.logger.setLevel(logging.WARNING)
streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.WARNING)
app.logger.addHandler(streamHandler)

if log:
     if log == 'info':
         app.logger.info('No issue.')
     elif log == 'warning':
         app.logger.warning('Warning occurred.')
     elif log == 'error':
         app.logger.error('Error occurred.')
     elif log == 'critical':
         app.logger.critical('Critical error occurred.')


import FlaskExercise.views
