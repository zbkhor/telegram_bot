import json
import os
from paragraph import *

# Separate Configuration Data
chat_ids = {
    'Boost': '-1001717957483',
    'Disposable': '-1001609338640',
    'sgvapezone': '-1001657320674',
    'VapehouseSG': '-1001308014353',
    'Vapehub': '-1001538107939',
    'VapePink': '-1001863158882',
    'VapeStation': '-1001685607433',
    'Bot': '-1001858159747',
    'Burning': '-1001566875450',
    'Karang': '-1001377220878',
    'LaunchingJuice': '-1001563439060',
    'SmokeDif': '-1001578412666',
    'SmokingFree': '-1001558933327',
    'ZooSingapore': '-1001519018057',
    'Merlion': '-1001858159747',
    'vapeparty': '-1001560725742',
    'happyvape': '-1001456831308',
    'pasarvape': '-1001693067994',
    'sgvape': '-1001793825702',
    'sgnightmarket': '-1001633391960',
    'vapestar': '-1001945472874',
    'realsgsupplier': '-1001781627788',
}

bot_tokens = {
    'Yuyuna': '5753903548:AAGzb92AMdhYEYMy_b0zMA0xUEEsX2qQaEk',
    'Chloe': '6703426544:AAHowvJhuVV4IkdguYT2iS7TuRQWX3UGSK0',
    'Seraphine': '6887431223:AAEJc4s3t_hA7DxrcO-k0NvqtgrkjPUMexU',
    'Celeste': '6787601158:AAE4N-FWjAyE3NHKGD35nVnHt-c-o6Ptedo',
    'Scarlett': '6371828828:AAErfPToRZwoyFTcZ1jnwGRUbbg5_rlKp9M',
    'Camila': '6763843999:AAGPRm9iB_GyyTKW7q6M3pY_BDA7YAUzJwU'
}
# Use Constants
SEND_INTERVAL_1 = 15

# Create Bot Configurations
chat_configs = []

for bot_name, token in bot_tokens.items():
    # Automatically insert all chat IDs into each bot's chat_ids list
    bot_config = {
        "token": token,
        "chat_ids": list(chat_ids.values()),  # Insert all chat IDs
        "strings": [paragraph1, paragraph10, paragraph11],
        "send_interval": SEND_INTERVAL_1
    }
    
    # Append the bot configuration to the list
    chat_configs.append(bot_config)

# Create a List of Bot Configurations
script_dir = os.path.dirname(__file__)
config_file_path = os.path.join(script_dir, 'bot_configs.json')

# Dump Configurations to a JSON File
try:
    with open(config_file_path, 'w') as json_file:
        json.dump(chat_configs, json_file, indent=4)
    print('Bot configurations have been saved to bot_configs.json')
except Exception as e:
    print(f'Error saving configurations: {e}')