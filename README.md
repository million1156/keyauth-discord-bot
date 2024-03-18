# KeyAuth Discord bot

## What is KeyAuth?
KeyAuth is an "authentication" service designed as a sort of "license key" based system. You can create keys, track what HWID is tracked to which key, and way way more.
> [!NOTE]
> Because of how this bot works, you cannot track what HWID uses a specific key. They will all go back to the same HWID (that is, the one that is hosting the bot itself)
> 
> To disable requiring a valid HWID (in the event you change VPS providers), you can go to your [app's settings in KeyAuth](https://keyauth.cc/app/?page=app-settings) and set "HWID Lock" to "Disabled".
>
> (if you are not using this bot, HWID locking should still work)


## What does this do?
This bot takes advantage of KeyAuth's API in order to create a Discord bot. There are many useful advantages to using a dedicated key service rather than making your own, such as easy management.
You could use this bot, for example, to "sell" access to a Discord server (sell access on [Sellix](https://sellix.io) -> use KeyAuth's API to generate a key for the customer upon buying from Sellix (this is officially supported by them if you have the required paid plan) -> customer gets key from Sellix -> uses it with this bot -> access!)


## What can I do?
Anything! The sky is the limit :) In regards to the license, this uses GPL 3.0. In essence, you can do whatever you'd like, but you must make any modifications to the code (excluding changes in tokens/authentication keys) open-source aswell. 
> [!CAUTION]
> This is not legal advice! I'm not a lawyer. Please check the license for yourself to get a detailed understanding of what you may and may not do with regards to this source code.
