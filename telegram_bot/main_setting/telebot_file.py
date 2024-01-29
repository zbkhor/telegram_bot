import telebot
import random
import time
import logging
import threading
import itertools

class TelegramBot:
    counters_lock = threading.Lock()
    global_counters = {}

    def __init__(self, token):
        self.bot = telebot.TeleBot(token)
        self.token = token
        self.message_count = 0
        self.chat_id_occurrences = {}

    def send_random_string(self, chat_ids, strings, send_interval):
        try:
            chat_ids_cycle = itertools.cycle(chat_ids)  # Create an iterator for round-robin
            strings_cycle = itertools.cycle(strings)  # Create an iterator for round-robin

            while True:
                chat_id = next(chat_ids_cycle)  # Get the next chat_id in the round-robin sequence
                message = next(strings_cycle)  # Get the next message in the round-robin sequence

                # Log the bot, chat_id, and message before sending
                logging.info(f"Bot {self.token} sending message to chat_id {chat_id}")

                # Update counters
                with self.counters_lock:
                    self.increment_counter(chat_id)

                self.bot.send_message(chat_id, message)

                logging.info(f"Interval: {send_interval}")
                time.sleep(send_interval)

        except telebot.apihelper.ApiException as api_error:
            logging.error(f"Telegram API error: {api_error}")
        except KeyboardInterrupt:
            logging.info("Thread interrupted. Exiting gracefully.")

    def increment_counter(self, chat_id):
        if chat_id not in self.chat_id_occurrences:
            self.chat_id_occurrences[chat_id] = 0
        self.chat_id_occurrences[chat_id] += 1
        self.message_count += 1

    def get_bot_stats(self):
        return {
            'token': self.token,
            'message_count': self.message_count,
            'chat_id_occurrences': self.chat_id_occurrences
        }
