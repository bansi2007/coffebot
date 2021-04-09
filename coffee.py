import re
import logging
import constants as CONST
#from config_loader import get_config
from flask import Flask, request
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from create_modalhandler import create_modalhandler

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s %(asctime)s %(message)s")

# Initializes your app with your bot token and signing secret
app = App(
    token= "\\your slack_bot_token",
    #get_config("slack_bot_token"),
    signing_secret= "\\your slack_signing_secret"
    #get_config("slack_signing_secret")
)

# holding slack user data
users_data = {}
notification_channel="C01T7PQJ881"

# The echo command simply echoes on command
@app.command(f"/{CONST.BOT_NAME}")
def bot_command(ack, body, client,say):
    try:
        # Acknowledge command request
        ack()
        text = body.get("text", "")
        channel_id = body.get("channel_id")
        print("----  channeld id : ", channel_id)
        channel_name = body.get("channel_name")
        print("----  channeld name : ", channel_name)
        user_id = body["user_id"]
        match = re.match(f"^make(\s*)", text)
        if match:
          create_modalhandler(ack, body, client,say,channel_id,user_id)
            #break
        #handler(ack, body, client, channel_id=channel_id)
    except Exception as e:
        #notify_error_to_slack(app, "An error Occured!!! Could not complete the request!!! Please try afetr some time", channel_id)
        # notify_error_to_slack(app)
        raise e



@app.message(re.compile("^hi$|^hello$|^hey$"))
def say_hello(message, say):
    try:
        user = message["user"]
        say(f"Hello there, <@{user}>!")
    except Exception as e:
        #notify_error_to_slack(app)
        print(e)
        
@app.message(re.compile("^how are you$|^hw r u$|^how r uh$"))
def ask(message, say):
    try:
        user = message["user"]
        say(f"i am fine, <@{user}>!")
    except Exception as e:
        #notify_error_to_slack(app)
        print(e)

@app.view("make_coffee")
def view_submission(ack, body, client, view, say):
    try:
        print(f"Welcome to Starbucks!")
        ack()
        
        name = view["state"]["values"]["Name"]["Name"]["value"]
        msg = view["state"]["values"]["Message"]["Message"]["value"]
        sugar = view["state"]["values"]["Sugar_packs"]["Sugar_packs"]["selected_option"]["value"]
        #project = view["state"]["values"]["project"]["project"]["selected_option"]["value"]
        drink = view["state"]["values"]["Drink"]["Drink"]["selected_option"]["value"]
        user_id = body["user"]["id"]
        from pprint import pprint
        pprint(body)
        #user_data = get_slack_user_data(user_id)
        msg = f"Hey,<@{user_id}>!\nWelcome to 'STARBUCKS'.\nYour {drink} with {sugar} of sugar packets is been recieved.\n The cup is named as {name} , and will send your message {msg} . Thankyou!:smile:"
        #msg, channel_id = create_ops_ticket(user_id, user_data, app, title, desc, estimate, priority, project, say, epic_link=None)
        say(msg, channel = notification_channel)
        say(msg, user = user_id)
    except Exception as e:
      print(e)
    
    

flask_app = Flask(__name__)
handler = SlackRequestHandler(app)


@flask_app.route("/health-check", methods=["GET"])
def health_check():
    return "Ok"


@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)


# Start your app
if __name__ == "__main__":
    try:
        if True:
            flask_app.run()
            logging.info("app started")

    except Exception as e:
        #notify_error_to_slack(app)
        raise e


   

