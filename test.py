import time
import threading
import json
import telebot
import random
import logging

class TelegramBot:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)
        self.exit_flag = False  # Flag to signal thread termination

    def send_random_string(self, chat_ids, strings, send_interval):
        try:
            while not self.exit_flag:
                self.bot.send_message(random.choice(chat_ids), random.choice(strings))
                time.sleep(send_interval)
        except KeyboardInterrupt:
            logging.info("Thread interrupted. Exiting gracefully.")

    def stop_thread(self):
        self.exit_flag = True

def initialize_bot(config):
    token = config['token']
    return TelegramBot(token)

def create_and_run_bot(config):
    bot = initialize_bot(config)
    thread = threading.Thread(target=bot.send_random_string, args=(config['chat_ids'], config['strings'], config['send_interval']))
    thread.daemon = True
    thread.start()
    return thread

def load_bot_configs(filename):
    with open(filename, 'r') as file:
        return json.load(file)

if __name__ == "__main__":
    bot_configs = load_bot_configs('./bot_configs.json')

    THREAD_START_INTERVAL = 3
    ADDITIONAL_SLEEP_INTERVAL = 3
    ITERATION_LIMIT = 20

    threads = []

    try:
        for config in bot_configs:
            thread = create_and_run_bot(config)
            threads.append(thread)
            time.sleep(THREAD_START_INTERVAL)

        count = 0
        while True:
            count += 1
            if count == ITERATION_LIMIT:
                count = 0
                time.sleep(ADDITIONAL_SLEEP_INTERVAL)

    except KeyboardInterrupt:
        print("KeyboardInterrupt: Stopping threads...")

        for thread in threads:
            thread.join()

        print("Threads stopped.")
