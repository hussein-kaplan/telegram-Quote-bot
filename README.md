# Daily Quote Bot

This is a Python script that creates and publishes daily quote images to a Telegram channel. The script fetches a random quote from an API and overlays it on a customizable background image along with a logo.

## Prerequisites

Before running the script, make sure you have the following:

- Python 3.x installed
- `telebot` library installed (`pip install pytelegrambotapi`)
- `requests` library installed (`pip install requests`)
- `Pillow` library installed (`pip install pillow`)

## Setup

1. Clone this repository or download the script file to your local machine.

2. Obtain a Telegram Bot token by creating a new bot using the [BotFather](https://core.telegram.org/bots#botfather) and note it down.

3. Replace the `'YOUR_BOT_TOKEN'` placeholder with your Telegram Bot token in the code.

4. Set your channel ID by replacing `'@YOUR_CHANNEL_USERNAME'` with the username of your Telegram channel.

5. Customize the script according to your preferences:
   - Adjust the `image_width` and `image_height` variables to set the size of the background image.
   - Modify the `background_color` and `text_color` variables to change the colors.
   - Replace `'path_to_your_font_file.ttf'` with the path to your desired font file.
   - Customize the logo text, font size, and color using the `logo_text`, `logo_font_size`, and `logo_text_color` variables.

6. Save the changes.

## Usage

1. Open a terminal or command prompt and navigate to the directory where the script is located.

2. Run the script using the following command:
python script.py



3. The script will continuously fetch a daily quote and publish it to the specified Telegram channel. Each quote will be accompanied by a generated image.

4. To stop the script, press `Ctrl + C` in the terminal or command prompt.

## Note

- Make sure your bot has permission to send messages and photos in the specified channel.

- Adjust the `time.sleep()` duration to control the frequency of quote publication. The provided script delays for 60 seconds between each iteration.

- Make sure the font file specified in `font_path` exists at the provided path.

- The script uses the `api.quotable.io` API to fetch random quotes. Ensure you have an internet connection for successful quote retrieval.

## License

This project is licensed under the [MIT License](LICENSE).
