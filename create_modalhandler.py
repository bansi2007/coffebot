import constants as CONST

def create_modalhandler(ack, body, client,say,channel_id,user_id):
  if channel_id not in CONST.supported_channels:
    print("Not supported")
    message = f"Hey <@{user_id}>,This slash command is not supported to our channel.\n Thankyou!:smile:"
    say(message, channel = channel_id)
  else:
    res = client.views_open(
            # Pass a valid trigger_id within 3 seconds of receiving it
            trigger_id=body["trigger_id"],
            channel_id = channel_id,
      
          
            # View payload
            view={
                
                "type": "modal",
                # View identifier
                "callback_id": "make_coffee",
                "title": {"type": "plain_text", "text": "Starbucks"},
                "submit": {"type": "plain_text", "text": "ok!Done"},
                "blocks": [
                    {
                        "type": "section",
                        "text": {"type": "mrkdwn", "text": "Please select your preferences\n "
                                                           "*are mandatory fields"},
                    },
                    {
                        "type": "input",
                        "block_id": "Name",
                        "label": {"type": "plain_text", "text": "Name *"},
                        "element": {
                            "type": "plain_text_input",
                            "action_id": "Name",
                            "multiline": False
                        }
                    },
                    {
                        "type": "input",
                        "block_id": "Message",
                        "label": {"type": "plain_text", "text": "Message for loved ones *"},
                        "element": {
                            "type": "plain_text_input",
                            "action_id": "Message",
                            "multiline": True
                        }
                    },
                    {
                        "type": "input",
                        "label": {"type": "plain_text", "text": "Sugar_packs  *"},
                        "block_id": "Sugar_packs",
                        "element": {
                            "type": "static_select",
                            "placeholder": {
                                "type": "plain_text",
                                "text": "Select no. of sugar packets ",
                                "emoji": True
                            },
                            "options": [
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": _,
                                    },
                                    "value": _ 
                                } for _ in ["1", "2", "3", "4"]
                            ],
                            "action_id": "Sugar_packs"
                        },
                        "optional": True,
                    },
                    {
                        "type": "input",
                        "label": {"type": "plain_text", "text": "Drink  *"},
                        "block_id": "Drink",
                        "element": {
                            "type": "static_select",
                            "placeholder": {
                                "type": "plain_text",
                                "text": "Select a drink ",
                                "emoji": True
                            },
                            "options": [
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": _,
                                    },
                                    "value": _ 
                                } for _ in ["Latte", "Cappuccino", "Cold_brew", "Frappuccino"]
                            ],
                            "action_id": "Drink"
                        }
                    },
                    
                ]
            }
        )



