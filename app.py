import logging
import os
import re
from slack_bolt import App, BoltContext
from strings import projects_starter, rutorrent, ideas_block
from typing import Callable

logging.basicConfig(level=logging.INFO)

# update ngrok/production links in slash commands and enable events page
# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
)


@app.middleware
def log_request(logger: logging.Logger, body: dict, next: Callable):
    logger.debug(body)
    return next()


def extract_subtype(body: dict, context: BoltContext, next: Callable):
    context["type"] = body.get("event", {}).get("type", None)
    next()


@app.message(
    re.compile(
        r"((?=.*(get|getting))(?=.*started))|(?=.*(find|found))(?=.*intresting)",
        flags=re.I | re.X | re.DOTALL,
    )
)  # ignore case and whitespace
def message_hello(body: dict, say):
    event = body["event"]
    thread_ts = event.get("thread_ts", None) or event["ts"]
    say(text=projects_starter, thread_ts=thread_ts)


@app.command("/rutorrent")
def rutorrent_command(body, respond, ack, logger):
    logger.info(body)
    respond(text=rutorrent)
    ack("All the best")


@app.command("/2020-ideas")
def rekognition_command(body, respond, ack, logger):
    logger.info(body)
    respond(blocks=ideas_block)
    ack("All the best")


# This listener handles all uncaught message events
# (The position in source code matters)
@app.event({"type": "message"}, middleware=[extract_subtype])
def just_ack(logger, context):
    event_type = context["type"]
    logger.info(f"{event_type} is ignored")


# # Start your app in debug
# if __name__ == "__main__":
#     app.start(port=int(os.environ.get("PORT", 3000)))

# for production

from flask import Flask, request
from slack_bolt.adapter.flask import SlackRequestHandler

flask_app = Flask(__name__)
handler = SlackRequestHandler(app)


@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)


@flask_app.route("/slack/install", methods=["GET"])
def install():
    return handler.handle(request)


@flask_app.route("/slack/oauth_redirect", methods=["GET"])
def oauth_redirect():
    return handler.handle(request)
