# Copyright 2021 @apichick
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START app]
import base64
import json
import logging

from flask import current_app, Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)

socketio = SocketIO(app)

@socketio.on('connected')
def handle_connected(data):
    print('user connected')

# [START index]
@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')

# [START push]
@app.route('/notify', methods=['POST'])
def receive_messages_handler():
    envelope = json.loads(request.get_data().decode('utf-8'))
    payload = json.load(base64.b64decode(envelope['message']['data']))
    emit('changes', payload, namespace="/", broadcast=True)
    # Returning any 2xx status indicates successful receipt of the message.
    return 'OK', 200
# [END push]

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=8080, debug=True)
# [END app]