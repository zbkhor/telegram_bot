import time
import threading
import json
from telebot_file import *
import logging

import time
import threading
import json
from telebot_file import TelegramBot
import logging

def create_and_run_bot(config):
    bot = TelegramBot(config['token'])
    thread = threading.Thread(target=bot.send_random_string, args=(config['chat_ids'], config['strings'], config['send_interval']))
    
    thread.daemon = True  # Set the thread as daemon
    thread.start()
    
    logging.info(f"Thread {thread.name} created and started for bot {config['token']}")
    
    return thread


def load_bot_configs(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# ... (previous code)

if __name__ == "__main__":
    bot_configs = load_bot_configs('./bot_configs.json')

    THREAD_START_INTERVAL = 3
    ADDITIONAL_SLEEP_INTERVAL = 3
    ITERATION_LIMIT = 20

    threads = []
    bots = []  # Create a list to hold instances of TelegramBot

    logging.basicConfig(level=logging.INFO)

    try:
        # Create instances of TelegramBot outside the loop
        for config in bot_configs:
            bot = TelegramBot(config['token'])
            bots.append(bot)

        # Start threads
        for bot, config in zip(bots, bot_configs):
            thread = threading.Thread(target=bot.send_random_string,
                                      args=(config['chat_ids'], config['strings'], config['send_interval']))
            thread.start()
            threads.append(thread)
            time.sleep(THREAD_START_INTERVAL)

        count = 0
        while True:
            count += 1
            print(f"Iteration Count: {count}")

            # Print bot stats after every iteration
            bot_stats = []
            with TelegramBot.counters_lock:
                for bot in bots:
                    bot_stats.append(bot.get_bot_stats())
                    # Debug: Print individual bot stats
                    print(f"Debug - Bot Stats for {bot.token}: {json.dumps(bot.get_bot_stats(), indent=2)}")

            print("Bot Stats:", json.dumps(bot_stats, indent=2))

            time.sleep(ADDITIONAL_SLEEP_INTERVAL)

    except KeyboardInterrupt:
        # Handle KeyboardInterrupt and stop threads
        try:
            print("KeyboardInterrupt: Stopping threads...")
            # Use the existing shared_counters dictionary
            bot_stats = [bot.get_bot_stats() for bot in bots]
            print("Bot Stats:", json.dumps(bot_stats, indent=2))
            with open('bot_stats.json', 'w') as json_file:
                json.dump(bot_stats, json_file, indent=2)
            for thread in threads:
                thread.join()

            # Collect bot stats after threads stop
            print("Threads stopped.")

            # Dump bot_stats to a new JSON file
            with open('bot_stats.json', 'w') as json_file:
                json.dump(bot_stats, json_file, indent=2)
            print("Bot stats saved to bot_stats.json")

        except KeyboardInterrupt:
            print("KeyboardInterrupt: Stopping threads...")
            for thread in threads:
                thread.join()
            print("Threads stopped. (No bot stats collected due to KeyboardInterrupt)")
