
from flask import Flask, jsonify, request


app = Flask(__name__)
#  app.config["DEBUG"] = True

#  @app.route("/")
#  def index():
#      return "Ok"

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

