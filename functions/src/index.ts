import * as functions from 'firebase-functions';
import { WebClient } from '@slack/web-api';
import { verifiySlackSignature } from './server';

const bot = new WebClient(functions.config().slack.token);

const { PubSub } = require('@google-cloud/pubsub');
const pubsubClient = new PubSub();


export const myBot = functions.https.onRequest ( async (req, res) =>  {
	// Validate signature 
	verifiySlackSignature(req);

	const data = JSON.stringify(req.body);

	const dataBuffer = Buffer.from(data);

	await pubsubClient
		.topic('slack-channel-join').publish(dataBuffer);

	res.sendStatus(200);
});


export const slackChannelJoin = functions.pubsub.topic('slack-channel-join')
.onPublish(async (message, context) => {

	const { event } = message.json;
	
	const { user, channel } = event;

	// IDs for the channel you plan on working with
	const generalChannel = 'C12345';
	const newChannel = '#aviation';

	// Throw error if not on the general channel

	if (channel !== generalChannel) {
		throw Error();
	}
	
	// Get the full Slack profile 

	const userResult = await bot.users.profile.get({ user });
	const { email, display_name } = userResult.profile as any;

	// Invite them to a new channel 

	const _invite = await bot.channels.invite( {
		channel: newChannel,
		user
	});

	// Send a Message 
	const _chatMessage = await bot.chat.postMessage({
		channel: newChannel,
		text: `Hey ${display_name}! howre u, welcome to slack`
	});
	
});
