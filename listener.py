from flask import Flask, request
from hashlib import sha256
import hmac
import logging
import subprocess

app = Flask(__name__)
# config
app.config.from_object("config")

# Logging to file
logging.basicConfig(
    filename=app.config["LOGFILE"],
    format="[%(asctime)s] [%(levelname)s] %(message)s",
    level=logging.DEBUG,
)


try:
    app.config.from_envvar("PROD_APP_SETTINGS")
    api.logger.info("Production settings loaded")
except:
    app.logger.warning(
        "Do NOT use in production! Env variable PROD_APP_SETTINGS not set and defaults are used."
    )


"""
Handles the call of new push events.
Looks for the event and signature headers
and verifies the signature with the secret API token.

Returns always just an empty string.
"""


@app.route("/api/github/push", methods=["POST"])
def push_received():
    try:
        github_signature = request.headers.get("X-Hub-Signature-256")
        github_event = request.headers.get("X-Github-Event")

        if github_signature is None or github_event is None:
            # Defenitely not a github api call and I dont care
            # about good information for the sender.
            app.logger.info(
                f"Github event or signature not found.\nEvent: {github_event}\nSignature: {github_signature}"
            )
            return ""

        app.logger.info(f"Github signature: {github_signature}")
        app.logger.info(f"Github event: {github_event}")

        token = bytes(app.config["TOKEN"], "utf-8")
        app.logger.debug(f"Token: {app.config['TOKEN']}")

        signature = (
            "sha256=" + hmac.new(token, msg=request.data, digestmod=sha256).hexdigest()
        )

        # secure compare
        if hmac.compare_digest(github_signature, signature):
            app.logger.info("Signature validation successful")

            with open(app.config["BUILD_SCRIPT_LOG"], "w") as outputfile:
                # pipe stderr to stdout and capture this in the log file
                subprocess.run(
                    app.config["BUILD_SCRIPT"],
                    stdout=outputfile,
                    stderr=subprocess.STDOUT,
                )
                # TODO: Maybe send the logfile via email.

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
