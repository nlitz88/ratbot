import discord
from discord.ext import commands

from youtube_dl import YoutubeDL

class music_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.is_playing = False
        self.is_paused = False

        self.music_queue = []
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

        # Instance variable to maintain the voice client returned once the bot successfully connects to the
        # channel.
        self.voice_client: discord.VoiceClient = None

    def search_yt(self, query):
        """Searches YouTube with the provided query. If successful, returns a dictionary containing the (source)
        url and title of the desired song."""
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try:
                info = ydl.extract_info("ytsearch:%s" % query, download=False)['entries'][0]
            except Exception:
                return False
        return {'source': info['formats'][0]['url'], 'title': info['title']}

    def play_next(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            m_url = self.music_queue[0][0]['source']
            
            self.music_queue.pop(0)

            self.voice_client.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    async def play_music(self, context: commands.Context):
        if len(self.music_queue) > 0:
            self.is_playing = True
            m_url = self.music_queue[0][0]['source']

            if self.voice_client == None or not self.voice_client.is_connected():
                self.voice_client = await self.music_queue[0][1].connect()

                if self.voice_client == None:
                    await context.send("Could not connect to the voice channel")
                    return
            else:
                await self.voice_client.move_to(self.music_queue[0][1])
            
            self.music_queue.pop(0)

            self.voice_client.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    @commands.command(name = "play", aliases = ["p", "playing"], help = "play the selected song from youtube")
    async def play(self, context: commands.Context, *args):

        # Grab the voice channel of the user that 
        voice_channel: discord.VoiceChannel = context.author.voice.channel

        # If the user invoked the bot but is not connected to a channel, tell them to connect first so the bot
        # knows what channel to connect to.
        if voice_channel is None:
            await context.send("Connect to a voice channel!")
        
        # Otherwise, if paused and the user sends a play command, just resume playback.
        elif self.is_paused:
            self.voice_client.resume()
            self.is_paused = False
            self.is_playing = True

        # If the user plays, is in a voice channel, and playback is not paused, then search for the song they
        # to play.
        # NOTE: I think this needs to be updated so that, if they provide a link, that it'll add that to the queue,
        # even if the bot is paused. That's the behavior many other bots use, so I'll request this as a feature.
        else:

            # Build the query from the arguments they provided with play.
            query = " ".join(args)
            # Attempt to get the song dictionary {source: url, title: title} from querying YouTube.
            song = self.search_yt(query)

            if type(song) == type(True):
                await context.send("Rats! I couldn't find the song you asked for. Maybe try a different search?")

            else:
                await context.send(f"{song['title']} added to the queue! ({song['source']})")
                # Add a new list containing the song dictionary {url, title} and the voice channel to connect to
                # and play that song in.
                self.music_queue.append([song, voice_channel])

                if self.is_playing == False:
                    await self.play_music(context)
            
    @commands.command(name = "pause", help = "Pauses the current song being played")
    async def pause(self, context, *args):
        if self.is_playing:
            self.voice_client.pause()
            self.is_playing = False
            self.is_paused = True
            
        elif self.is_paused:
            self.voice_client.resume()
            self.is_paused = False
            self.is_playing = True

    @commands.command(name = "resume", aliases=["r"], help = "Resumes playin gthe current song")
    async def resume(self, context, *args):
        if self.is_paused:
            self.is_playing = True
            self.is_paused = False
            self.voice_client.resume()

    @commands.command(anme = "skip", aliases = ["s"], help = "Skips the currently plaed song")
    async def skip(self, context, *args):
        if self.voice_client != None and self.voice_client:
            self.voice_client.stop()
            await self.play_music(context)
    
    @commands.command(name = "queue", aliases=["q"], help = "Displays all the songs currently in the queue")
    async def queue(self, context):
        retval = ""

        for i in range(0, len(self.music_queue)):
            if i > 4: break
            retval += self.music_queue[i][0]['title'] + '\n'
        
        if retval != "":
            await context.send(retval)
        else:
            await context.send("No music in the queue.")

    @commands.command(name = "clear", aliases = ["c", "bine"], help="stops the current song and clearas the queue")
    async def clear(self, context, *args):
        if self.voice_client != None and self.is_playing:
            self.voice_client.stop()
        self.music_queue = []
        await context.send("Music queue cleared")
    
    @commands.command(name = "leave", aliases = ["disconnect", "1", "d"], help = "Kick the bot from the voice channel")
    async def leave(self, context):
        self.is_playing = False
        self.is_paused = False
        await self.voice_client.disconnect()



    


