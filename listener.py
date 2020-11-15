from flask import Flask, jsonify, request
from hashlib import sha256
import hmac

app = Flask(__name__)
# config
app.config.from_object("config")

try:
    app.config.from_envvar("PROD_APP_SETTINGS")
except:
    #  print("[INFO]: Env variable PROD_APP_SETTINGS not set. Using default settings")
    app.logger.info(
        "Env variable PROD_APP_SETTINGS not set. Using default settings\nDo NOT use in production."
    )


@app.route("/api/github/push", methods=["POST"])
def push_received():
    try:
        github_signature = request.headers.get("X-Hub-Signature-256")
        github_event = request.headers.get("X-Github-Event")

        app.logger.info(f"Github signature: {github_signature}")
        app.logger.info(f"Github event: {github_event}")

        token = bytes(app.config["TOKEN"], "utf-8")
        app.logger.debug(f"Token: {app.config['TOKEN']}")

        signature = (
            "sha256=" + hmac.new(token, msg=request.data, digestmod=sha256).hexdigest()
        )

        # secure compare
        if hmac.compare_digest(github_signature, signature):
            print("Signatures match!")
        else:
            app.logger.error(
                f"Signatures do not match\nGithub: {github_signature}\n  Ours: {signature}"
            )

    except Exception as err:
        app.logger.error(err)
    finally:
        return ""


if __name__ == "__main__":
    app.run(port=5000)
