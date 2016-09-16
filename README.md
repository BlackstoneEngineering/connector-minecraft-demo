# What is this?
Demo that uses the mbed client / connector. When you press the button on an embedded device it triggers an action in the minecraft game. The basic demo is press a button and get some diamond ore.

# Why do I care?
It demonstrates how to use mbed client on the embedded side and the python REST API wrapper library on the other side to hook up any script or server to mbed connector. Its super simple.

# Pre-requisites
1. Python 2.7.9+ installed on your computer
2. Raspberry Pi with Raspbian (has minecraft installed by default), or windows machine with minecraft and [appropriate mods and python extensions installed](http://www.instructables.com/id/Python-coding-for-Minecraft/) (Forge + RaspberryJam mod)

# How do I use this?
You have to run 2 pieces of code: 

1. *Embedded code*: runs on an embedded device that can use an IP connection  (Ethernet / Wifi / Cellular) and relays when a button is pressed to connector.
2. *Python Script*: This runs on the computer that is running the minecraft game server. It talks to both the minecraft server and to connector via the [mbed-connector-api-python](https://github.com/armmbed/mbed-connector-api-python). This script interprets the button presses and generates the items in minecraft. Run `python demo-for-pi.py` on Raspberry Pi or `python demo-for-windows.py` on windows machines to use the scripts. 

### Embedded Code
The embedded code is the [mbed-client-quickstart](https://github.com/armmbed/mbed-client-quickstart). You can either compile this online using the [mbed compiler](developer.mbed.org/compiler) or using [mbed cli](https://github.com/armmbed/mbed-cli). Make sure to populate the `source/security.h` file with security credentials from [mbed connector](https://connector.mbed.com/#credentials). Take special note of your devices name in the `#define MBED_ENDPOINT_NAME "your-devices-uuid-name"` string as you need it for the embedded script. 

### Python Script
The Python script requires two pieces of information. 
1. The embedded devices endpoint name, the `MBED_ENDPOINT_NAME` from the security.h fle. In `demo-for-*.py` replace `ep = "YOUR ENDPOINT NAME"` with the value from `MBED_ENDPOINT_NAME`.
2. A [mbed connector API key](https://connector.mbed.com/#accesskeys) registered to your account. In `demo-for-*.py` replace `x = mdc.connector("YOUR API KEY")` with your API key. 

Once you have both the embedded code running, turn on the minecraft server (run `minecraft.exe`), then run the python script. Now when you press a button on the board it should cause a piece of diamond ore to show up in front of your avatar in game. 

# Liscense
Apache 2.0

