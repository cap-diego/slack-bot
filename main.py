import os
from slack import WebClient
from slack.errors import SlackApiError
from dotenv import load_dotenv
from flask import escape



def initialize_slack_client():
	client = WebClient(token=os.environ['SLACK_API_TOKEN'])

	try:
	    response = client.chat_postMessage(
	        channel='#general',
	        text="Hello world!")
	except SlackApiError as e:
	    # You will get a SlackApiError if "ok" is False
	    assert e.response["ok"] is False
	    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
	    print(f"Got an error: {e.response['error']}")


if __name__ == '__main__':

	load_dotenv(verbose=True)
	initialize_slack_client()


def callback_new_message(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    """
	try:
		import googleclouddebugger
		googleclouddebugger.enable(breakpoint_enable_canary=True)
	except ImportError:
  		pass
	request_json = request.get_json(silent=True)
    request_args = request.args
    challenge = ''
    if request_json and 'challenge' in request_json:
        return request_json['challenge']
    elif request_args and 'challenge' in request_args:
        return request_args['challenge']
    
    return '{} - {}'.format(type(request_json, request_json.keys()))
