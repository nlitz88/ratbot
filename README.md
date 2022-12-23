# ratbot
Rats! Ratbot is a simple, self-hosted Discord music bot.

## Self Hosting Ratbot
There are two main "pieces" to every Discord bot:
1. The "bot" you create on the Discord Developer Portal
2. The actual code that makes up the bot

I.e., you can think of the bot you create on the Discord Developer Portal as creating a new Discord user (where
that user is uniquely identified by some token), and the actual code that the bot runs with as what controls that
user.

Therefore, to use ratbot, you essentially have to (1) create your own "bot user" (if you will) on the Discord Developer
Portal, and then (2) run the bot code from this repository using your new "bot user's" token. It's like running
your own version of the bot, basically!

## 1. Creating a new bot on the Discord Developer Portal.
#### Starting with a YouTube Tutorial
I'll be honest: the best way to do this is to just follow along with the first part of [Computershort's
tutorial](https://www.youtube.com/watch?v=dRHUW_KnHLs).

### Getting Your Bot's Token
The most important part is **copying and storing
the token** of the bot you create. This is what you will specify when you go to spin up the bot as a container
later.

*Note: It's not like you have to guard the bot token with your life. Worst case, you have to regenerate it later.
You just don't want someone else to be able to host the same bot instance you created. The best idea is to probably
just stow away the token in a txt file somewhere on your computer or wherever you're hosting the bot, or just
regenerate it every time you forget :)*

#### Giving your bot access to [Privileged Gateway Intents](https://autocode.com/discord/threads/what-are-discord-privileged-intents-and-how-do-i-enable-them-tutorial-0c3f9977/).
In addition to the steps outlined in the above tutorial, you'll also need to give your bot access to all of the
different intents Discord has to offer. This basically just allows your bot to see everything that happens on your
server, like users sending messages, joining a channel, etc.
   1. In your Discord Developer Portal, head to the **bot** tab.
   2. Under the **Privileged Gateway Intents** section, give your bot access to all of these different types of
      intents (different kinds of Discord events) by enabling each intent type.

 > Why should I give my bot access to Priveleged Gateway Intents? Aren't they restricted for a reason?
 
 Yes, I hear you, but for ratbot, enabling them all will be fine. Why? Because ratbot is intended to be
 self-hosted. Therefore, because you're probably not publicly distributing the bot (although, there's nothing
 stopping you), you don't have to worry about the implications of giving **your own bot** access to these
 different intents.

 > What even are "intents?"

 Give [discordpy's page on these](https://discordpy.readthedocs.io/en/stable/intents.html) a read over, they
 offer a good explanation. In short, an intent is basically a group of different Discord events that you
 can have your bot subscribe/listen to.

## 2. Running the ratbot container with your unique bot token
Now that you have a token for your unique "bot user," you can spin up the ratbot code to power your unique bot!
Ratbot is currently run as a Docker Container. If you know what you're doing, you're more than welcome to execute
ratbot.py with python. For the average user, it'll probably be easier to just run everything as a container all
packaged up so you don't have to worry about any dependency or compatibility issues.

### Running the ratbot container using the ratbot image
To spin up the ratbot container using the latest image from Docker Hub, run the following command:

    docker run -e TOKEN=<bot_token_here> ratbot -d

### Environment Variables
Environment variables are used to control the bot's behavior. Below is a table of all possible environment
variables. **TOKEN is the only required environment variable.**

<table style="border-collapse:collapse;border-spacing:0" class="tg"><tbody><tr><td style="border-color:#333333;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:medium;font-weight:bold;overflow:hidden;padding:10px 5px;text-align:center;vertical-align:top;word-break:normal">Environment Variable</td><td style="border-color:#333333;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:medium;font-weight:bold;overflow:hidden;padding:10px 5px;text-align:center;vertical-align:top;word-break:normal">Description</td></tr><tr><td style="border-color:#333333;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:center;vertical-align:top;word-break:normal">TOKEN</td><td style="border-color:#333333;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">Your bot's unique token you got from your Discord Developer Portal</td></tr></tbody></table>

### Building ratbot image from source
To build the ratbot image from source, run the following command in your local copy of the repository to build the
ratbot image.

    docker build --tag ratbot .

<!-- # ratbot development environment
To start working on ratbot, use the following steps to set up a development environment.

1. Install python
2. Install all python requirements
   
        pip3 install -r requirements.txt

3. Install Docker -->

# Acknolwedgements
The core of ratbot originated from [this](https://www.youtube.com/watch?v=dRHUW_KnHLs) YouTube tutorial by
[Computershorts](https://www.youtube.com/channel/UC2clDLZK1wXYB5be4b240Hg). Ratbot has changed a fair bit since
that video, but that's where it started!