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

    def send_messages_to_chat(self, chat_id, messages, send_interval):
        try:
            for message in messages:
                # Log the bot, chat_id, and message before sending
                logging.info(f"Bot {self.token} sending message to chat_id {chat_id}")
                logging.info(f"Bot sending {message}")

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

    def send_random_strings(self, chat_ids, strings, send_interval, bot_index):
        try:
            strings_cycle = itertools.cycle(strings)  # Create an iterator for round-robin

            # Skip to the message corresponding to the bot_index
            for _ in range(bot_index):
                next(strings_cycle)

            chat_id_message_pairs = list(zip(chat_ids, strings_cycle))

            while True:
                threads = []
                for chat_id, message in chat_id_message_pairs:
                    thread = threading.Thread(target=self.send_messages_to_chat, args=(chat_id, [message], send_interval))
                    thread.start()
                    threads.append(thread)

                # Wait for all threads to finish
                for thread in threads:
                    thread.join()

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
