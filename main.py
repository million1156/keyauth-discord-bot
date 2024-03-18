from keyauth import api
import sys
import hashlib
from interactions import Client, Intents, listen, slash_command, SlashContext, OptionType, slash_option, SlashCommandChoice, Embed
import requests
import random
import websockets
import yachalk
bot = Client(intents=Intents.DEFAULT)

@listen()
async def on_ready():
    print(f"[BOT]: Ready!")

def getchecksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest


keyauthapp = api(
    name = "",
    ownerid = "",
    secret = "",
    version = "1.0",
    hash_to_check = getchecksum()
)

# Authenticate token
async def auth(token: str):
    assert(type(token) == str)
    try:
        # Attempt to authenticate
        result = keyauthapp.license(token)

        # User input an invalid license
        if result == None or result == "Invalid license key":
            print(yachalk.chalk.red("[KeyAuth]: Failed auth"))
            return False
        
        elif result == False:
            # Uhoh.. this most likely means keyauth itself is having some issues :c
            print(yachalk.chalk.red("[KeyAuth]: Upstream failure"))
            return "Upstream failure"
        print(yachalk.chalk.green("[KeyAuth]: Auth Token: " + keyauthapp.user_data.username))
        return True
    except:
        return False

async def exampleCommand():
    try:
        return "Example"
    except:
        raise Exception("Error")
    
    
@slash_command(name = "examplecommand", description = "Example command that requires a valid KeyAuth license :)")
@slash_option(name= "token", description = "Your KeyAuth token", required = True, opt_type = OptionType.STRING)

async def examplecommand(ctx: SlashContext, token: str):
    await ctx.defer()
    authResult = await auth(token)
    
    # Handle any failures with auth
    if not authResult:
        embed = Embed(
            title="Error",
            description=f"<:error:1208885864424407141> Invalid token! Please try again with a valid token.",
            color=0xFF0000
        )
        await ctx.send(embed=embed)
        return
    if authResult == "Upstream failure":
        embed = Embed(
            title="Error",
            description=f"<:error:1208885864424407141> There was an upstream failure while trying to authenticate your token. Please try again later :c",
            color=0xFF0000
        )
        await ctx.send(embed=embed)
        return
    
    # Passed authentication
    print(yachalk.chalk.green("Passed auth"))
    
    exampleOutput = await exampleCommand()
    
    # Error with the command
    if exampleOutput == "Error":
        embed = Embed(
            title="Error",
            description=f"<:error:1208885864424407141> There was an error running your command. Please try again later :(",
            color=0xFF0000
        )
        await ctx.send(embed=embed)
        return
    embed = Embed(
        title="Success!",
        description=f"<:success:1208885438010359869> {exampleOutput}",
        color=0x00FF00
    )
    await ctx.send(embed=embed)
    return
    


bot.start("TOKEN")
   

