import telebot
import requests
from io import BytesIO
import time
from PIL import Image, ImageDraw, ImageFont, ImageOps
import textwrap

# Set your Telegram bot token
TOKEN = 'YOUR_BOT_TOKEN'

# Create a telebot instance
bot = telebot.TeleBot(TOKEN)

# Set your channel ID
channel_id = '@YOUR_CHANNEL_USERNAME'

# API endpoint for fetching daily quotes
quote_api_url = 'https://api.quotable.io/random'

# Font path
font_path = 'path_to_your_font_file.ttf'  # Replace with your font path

# Customization options for the image
image_width = 1080  # Instagram post width
image_height = 1080  # Instagram post height
background_color = (0, 0, 0)  # RGB value for black
text_color = (255, 255, 255)  # RGB value for white
font_size = 48
text_padding = 50  # Padding for left and right edges

# Logo customization
logo_text = "Your Logo"  # Replace with your logo text
logo_font_size = 64
logo_text_color = (255, 255, 255)  # RGB value for white

# Function to fetch a daily quote from the API
def get_daily_quote():
    response = requests.get(quote_api_url)
    if response.status_code == 200:
        quote_data = response.json()
        content = quote_data['content']
        author = quote_data['author']
        return f"{content}\n\n- {author}"
    return None

# Function to create an image with the quote and logo
def create_quote_image(quote):
    image = Image.new('RGB', (image_width, image_height), color=background_color)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, size=font_size)

    # Wrap the quote text based on the available width
    wrapped_lines = textwrap.wrap(quote, width=(image_width - 2 * text_padding) // font_size)
    text_height = 0
    for line in wrapped_lines:
        line_width, line_height = draw.textsize(line, font=font)
        text_height += line_height

    y = (image_height - text_height) // 2

    # Draw the wrapped lines of the quote text
    for line in wrapped_lines:
        line_width, line_height = draw.textsize(line, font=font)
        x = (image_width - line_width) // 2
        draw.text((x, y), line, font=font, fill=text_color, align='center')
        y += line_height

    # Add logo using text
    logo_font = ImageFont.truetype(font_path, size=logo_font_size)
    logo_width, logo_height = draw.textsize(logo_text, font=logo_font)
    logo_x = (image_width - logo_width) // 2
    logo_y = (image_height - logo_height) - (text_height // 2) - 50  # Adjust the logo position as needed
    draw.text((logo_x, logo_y), logo_text, font=logo_font, fill=logo_text_color, align='center')

    return image

# Function to publish the daily quote image in the channel
def publish_daily_quote():
    quote = get_daily_quote()
    if quote:
        image = create_quote_image(quote)
        image = image.resize((1080, 1080))  # Resize image for Instagram post
        with BytesIO() as bio:
            image.save(bio, format='JPEG')
            bio.seek(0)
            bot.send_photo(chat_id=channel_id, photo=bio)
    else:
        bot.send_message(chat_id=channel_id, text="Unable to fetch daily quote.")

# Call the publish_daily_quote function every day at a specific time
while True:
    publish_daily_quote()
    time.sleep(60)  # Delay for 60 seconds to avoid duplicate messages

# Start the bot
bot.polling()
