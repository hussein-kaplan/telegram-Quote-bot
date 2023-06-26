# Daily Quote Bot for Telegram

This repository contains a Python script that generates and publishes daily quote images on a Telegram channel using the Telebot library.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Customization](#customization)
- [License](#license)

## Overview
The Daily Quote Bot script fetches a random quote using the Quotable API and creates an image with the quote and a custom logo. The image is then published on a Telegram channel at a specific interval, creating a daily quote feed.

The script uses the Telebot library to interact with the Telegram Bot API, requests library for making HTTP requests, PIL (Python Imaging Library) for image manipulation, and io library for working with byte streams.

## Installation
1. Clone the repository to your local machine:
   ```shell
   git clone https://github.com/your-username/daily-quote-bot.git
Install the required Python dependencies:
shell
Copy code
pip install -r requirements.txt
Usage
Obtain a Telegram bot token by creating a new bot using the BotFather on Telegram.

Set the token in the script:

TOKEN = 'YOUR_BOT_TOKEN'
Set the channel ID where you want to publish the images in the script:

channel_id = '@YOUR_CHANNEL_USERNAME'
Optionally, customize other configuration variables and parameters according to your requirements.

Start the bot by running the script:

python bot.py
The script will continuously fetch daily quotes and publish them on the specified Telegram channel at the specified interval.

Configuration
The script provides several configuration variables that you can modify to customize its behavior:

TOKEN: Your Telegram bot token obtained from BotFather.
channel_id: The username or ID of the Telegram channel where the quote images will be published.
quote_api_url: The API endpoint for fetching daily quotes. You can modify it if you want to use a different quote API.
font_path: The path to your custom font file (TTF format). Replace it with the actual font path.
image_width and image_height: The dimensions of the quote image in pixels.
background_color: The RGB color value for the image background.
text_color: The RGB color value for the quote text.
font_size: The font size for the quote text.
text_padding: The padding for the left and right edges of the quote text.
logo_text: The text to be used as the logo.
logo_font_size: The font size for the logo text.
logo_text_color: The RGB color value for the logo text.
Customization
You can customize the script further based on your requirements. Some possible customizations include:

Error handling: Add error handling to handle network failures, API errors, or other exceptions that may occur during script execution.
Additional features: Extend the script to support additional functionality, such as including images or graphics in the quote images, adding captions, or integrating with other APIs for fetching quotes.
UI improvements: Modify the appearance of the quote images, change the layout, add borders, or experiment with different fonts and colors.
License
This project is licensed under the MIT License.
