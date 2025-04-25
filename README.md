# #not Discord Bot - Documentation

Hey, Thanks for using our bot 😄 `#not` is the official bot for the Dream it possible Discord server, designed to enhance your server's functionalities and provide an enjoyable experience for your community.

## Introduction

Welcome to the documentation for the `#not` Discord bot! This document provides a comprehensive guide on how to use and interact with our bot in your Discord server. The bot is designed to perform various tasks, enhance your server's functionalities, and provide an enjoyable experience for your community.

## Table of Contents

* [Getting Started](#getting-started)
    * [Invite the Bot to Your Server](#invite-the-bot-to-your-server)
    * [Bot Commands Prefix](#bot-commands-prefix)
* [Hello & Bye Reply](#hello--bye-reply)
* [Edit Message Response](#edit-message-response)
* [Calculator Support](#calculator-support)
    * [clc](#clc)
    * [sum](#sum)
    * [avg](#avg)
* [Media Support](#media-support)
    * [ytdl](#ytdl)
* [Channel Support](#channel-support)
    * [ctd](#ctd)
* [Auto Reaction](#auto-reaction)
    * [hhreact](#hhreact)
* [Wiki Searching](#wiki-searching)
    * [src](#src)
* [Others](#others)
    * [flip](#flip)
    * [mog](#mog)
* [Support and Contributions](#support-and-contributions)

## Getting Started

### Invite the Bot to Your Server

[Add to my server](YOUR_BOT_INVITE_LINK_HERE)

* *Replace `YOUR_BOT_INVITE_LINK_HERE` with the actual invite link for the `#not` bot.*

### Bot Commands Prefix

All `#not` bot commands are prefixed with `hh`.

## Core Functionality

### Hello & Bye Reply

`#not` bot automatically replies when a member sends "Hello" or "Bye" messages in the channel.  This provides a simple, automated greeting and farewell.

### Edit Message Response

`#not` will respond when a user edits a message. It will send a message showing what the author's message was before and what it is now.  This can be useful for moderation or tracking changes.

## Calculator Support

`#not` bot supports calculations using specific commands within your messages.

### `clc`

Performs a basic two-number calculation.

**Note:** You must use specific operators:

* `+` use `pl`
* `-` use `mi`
* `*` use `mu`
* `/` use `di`

**Command:** `hh clc {digit} {First number} {operator} {Last value}`

* `{digit}`: Specifies the number of digits to display in the result.
* `{First number}`: The first number in the calculation.
* `{operator}`: The operator to use (`pl`, `mi`, `mu`, `di`).
* `{Last value}`: The second number in the calculation.

**Example:** `hh clc 2 12 pl 13`
**`#not` bot will return:** `25`

### `sum`

Calculates the sum of multiple numbers.

**Command:** `hh sum {numbers by space}`

* `{numbers by space}`: A series of numbers separated by spaces.

**Example:** `hh sum 12 345 435`
**`#not` bot will return:** The sum of the numbers (e.g., `∫(12 345 435) = 792`).

### `avg`

Calculates the average of multiple numbers.

**Command:** `hh avg {numbers by space}`

* `{numbers by space}`: A series of numbers separated by spaces.

**`#not` bot will return:** The average of the provided numbers (e.g., `∫((numbers)/count)`).  The bot handles floating-point numbers.

## Media Support

### `ytdl`

Provides a download link for a YouTube video.

**Command:** `hh ytdl {youtube video link}`

* `{youtube video link}`: The URL of the YouTube video.

**Example:** `hh ytdl https://www.youtube.com/watch?v=f5F7fxrU1lc`
**`#not` bot will return:** A download link for the video.

## Channel Support

### `ctd`

Creates a new thread within the current channel.

**Command:** `hh ctd {Thread Name}`

* `{Thread Name}`: The name for the new thread.

When you use this command, the bot will:

1.  Create a new thread with the specified name.
2.  Mention the user who created the thread in the new thread.

## Auto Reaction

`#not` bot can automatically add reactions to messages containing images.

### `hhreact`

Adds reactions to image messages.

**How it works:**

When you send an image with the `hhreact` command in the message caption, the bot adds reactions.

* If `hhreact` is the *only* text in the caption, the bot adds 5 default reactions.
* If the caption contains `hhreact` *plus* other text, the bot adds 6 reactions.

**Example (5 reactions):** Image sent with caption: `hhreact`
**Example (6 reactions):** Image sent with caption: `hhreact This is my image`

## Wiki Searching

### `src`

Searches for information on a wiki (likely Wikipedia).

**Command:** `hh src {parameter}`

* `{parameter}`: The term you want to search for.

**Example:** `hh src Discord`
**`#not` bot will return:** Search results or a summary.

## Other Functions

### `flip`

Flips the characters in a message.

**Command:** `hh flip {message}`

* `{message}`: The text to flip.

**Example:** `hh flip Hello`
**`#not` bot will return:** `oןןǝH`

### `mog`

Creates groups of members from a provided list.

**Command:** `hh mog {sets of name of member} {group size}`

* `{sets of name of member}`: A space-separated list of member names.
* `{group size}`: The desired size of each group.

**Example:** `hh mog User1 User2 User3 User4 User5 2`
**`#not` bot will return:** A list of groups (e.g., `Group 1: User1, User3; Group 2: User2, User4`).  If the group size equals the member count, the bot returns "none".

## Support and Contributions

Thank you for using the `#not` bot! We hope this documentation is helpful.  For support, questions, or to contribute, please reach out in the Dream it possible Discord server.  We appreciate your feedback!
