import os

from flask import Flask

print(os.environ)

app = Flask(__name__)

if __name__ == '__main__':
    if eval(os.getenv('DEBUG', 'True')):
        port = int(os.environ.get('PORT', 80))
        print("App is running on port " + str(port))
        app.run(host='0.0.0.0', port=port, threaded=True, debug=True, use_reloader=True)
    else:
        port = int(os.environ.get('PORT', 80))
        app.run(host='0.0.0.0', port=port, threaded=True, debug=False, use_reloader=False)
