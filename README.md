### Bomb Party Word Game Bot

This Python program is a bot designed to play the word game on JKML.FUN, where players have to quickly type words containing specific letters. The bot automatically generates and types words based on the given letters.

### Installation

To use this bot, make sure you have Python installed on your system. Then, install the required Python packages by running:

pip install -r requirements.txt


### Usage

1. **Clone Repository**: Clone this repository to your local machine.

2. **Install Dependencies**: Install the required Python packages using the command mentioned in the Installation section.

3. **Run the Bot**: Run the bot by executing the `word_game_bot.py` script using Python:

4. **Save the position**: Place your mouse over the syllable in the bomb and press F4 to save this position

5. **Write the word**: Press F2 when it is your turn

**Keybinds**:
   - **F9**: Exit the bot.
   - **Shift**: Toggle instant typing mode.
   - **Space**: Reset used letters.
   - **F8**: Reset used words.
   - **F4**: Set mouse position.
   - **F2**: Process the given letters and type the word.
   - **Caps Lock**: Toggle long words mode.

### Customization

You can change the language of the game by modifying the word list file. This bot currently supports English and Portuguese, but you can create or use a different word list file to play in other languages.


You can customize the bot's behavior by modifying the settings and methods in the `WordGame` class within the `word_game_bot.py` file. You can adjust parameters such as delay times, word length preferences, and more.

