from pynput.keyboard import Listener, Key
from time import sleep
import pyautogui
import pyperclip
import random

class WordGame:
    def __init__(self):
        self.x = ""
        self.y = ""
        self.delays = [0.03, 0.04, 0.05, 0.06, 0.07]
        self.long_words = True
        self.instant_typing = False
        pyautogui.PAUSE = 0
        self.used_words = set()
        self.used_letters = set()

        with open('wordlist-br.txt', encoding="utf8") as word_file:
            self.valid_words = word_file.read().split()

    def search_best_word(self, word_list):
        best_word = ''
        max_length = 0
        max_unused_letters = 0
        
        for word in word_list:
            unused_letters_count = sum(1 for letter in word if letter not in self.used_letters)
            if word not in self.used_words:
                if unused_letters_count > max_unused_letters or (unused_letters_count == max_unused_letters and len(word) > max_length):
                    max_unused_letters = unused_letters_count
                    max_length = len(word)
                    best_word = word
        
        return best_word

    def handle_f9(self):
        print("Exiting...")
        exit(1)

    def toggle_instant_typing(self):
        self.instant_typing = not self.instant_typing
        print("Instant typing set to: " + str(self.instant_typing))

    def set_long_words(self):
        self.long_words = not self.long_words
        print("Long words set to: " + str(self.long_words))

    def reset_used_letters(self):
        self.used_letters.clear()
        print("Resetting used letters.")

    def reset_used_words(self):
        self.used_words.clear()
        print("Resetting used words.")

    def set_mouse_position(self):
        try:
            self.x, self.y = pyautogui.position()
            print("Mouse position set to: " + str(self.x) + ", " + str(self.y))
        except Exception as e:
            print(f"Error setting mouse position: {e}")

    def process_f2(self):
        try:
            pyautogui.click(x=self.x, y=self.y, clicks=2)
            with pyautogui.hold('ctrl'):
                pyautogui.press('c')
            pyautogui.click(x=self.x - 100, y=self.y)
            sleep(0.1)
            syllable = pyperclip.paste().lower().strip()
            pyperclip.copy('')
            found_words = [word for word in self.valid_words if syllable in word]
            
            if not found_words:
                print("No words were found.")
                return

            if len(self.used_letters) >= 26:
                print("All letters have been used.")
                self.used_letters.clear()

            if self.long_words:
                final_word = self.search_best_word(found_words)
            else:
                final_word = random.choice(found_words)
                while final_word in self.used_words:
                    if len(self.used_words) == len(found_words):
                        print("All words have been used.")
                        return
                    final_word = random.choice(found_words)
            
            self.used_words.add(final_word)
            for char in final_word:
                self.used_letters.add(char)
            
            if self.instant_typing:
                pyperclip.copy(final_word)
                with pyautogui.hold('ctrl'):
                    pyautogui.press('v')
            else:
                for char in final_word:
                    delay = random.choice(self.delays)
                    pyautogui.write(char, delay)
            pyautogui.press('enter')
        except Exception as e:
            print(f"Error processing F2: {e}")

    def release(self, key):
        actions = {
            Key.f9: self.handle_f9,
            Key.shift: self.toggle_instant_typing,
            Key.space: self.reset_used_letters,
            Key.f8: self.reset_used_words,
            Key.f4: self.set_mouse_position,
            Key.f2: self.process_f2,
            Key.caps_lock: self.set_long_words
        }

        action = actions.get(key)
        if action:
            action()

    def start_game(self):
        with Listener(on_release=self.release) as listener:
            listener.join()

if __name__ == "__main__":
    game = WordGame()
    game.start_game()