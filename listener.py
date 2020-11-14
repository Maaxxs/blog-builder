
from flask import Flask, jsonify, request


app = Flask(__name__)
# config
app.config.from_object("config")

try:
    app.config.from_envvar("PROD_APP_SETTINGS")
except:
    print("[INFO]: Env variable PROD_APP_SETTINGS not set. Using default settings")

# Printing variables for testing
#  print(app.config["DEBUG"])
#  print(app.config["TOKEN"])


@app.route("/api/github/push", methods=["POST"])
def push_received():
    try:
        print("headers:")
        print(request.headers)

        print('some data received:')

        data = request.json
        print(data)
    except:
        app.logger.error("Error in handling request. Might be malformed json")
    finally:
        return ""



if __name__ == "__main__":
    app.run(port=5000)

