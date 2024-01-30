import json
import os
from paragraph import *

# Separate Configuration Data
chat_ids = {
    'sgvapezone': '-1001657320674',
    'Merlion': '-1001858159747',
    'realsgsupplier': '-1001781627788',
    'Disposable': '-1001609338640',
    'VapeStation': '-1001685607433',
    'Burning': '-1001566875450',
    'Vapehub': '-1001538107939',
    'vapestar': '-1001945472874',
    'VapePink': '-1001863158882'
}

bot_tokens = {
    'Yuyuna': '5753903548:AAGzb92AMdhYEYMy_b0zMA0xUEEsX2qQaEk',
    'Chloe': '6703426544:AAHowvJhuVV4IkdguYT2iS7TuRQWX3UGSK0',
    'Seraphine': '6887431223:AAEJc4s3t_hA7DxrcO-k0NvqtgrkjPUMexU',
    'Celeste': '6787601158:AAE4N-FWjAyE3NHKGD35nVnHt-c-o6Ptedo',
    'Scarlett': '6371828828:AAErfPToRZwoyFTcZ1jnwGRUbbg5_rlKp9M',
    'Camila': '6763843999:AAGPRm9iB_GyyTKW7q6M3pY_BDA7YAUzJwU',
    'Merlion': '6080654541:AAEa1upiGaQdcZJlLx4b4lRNJwAF7AOAzNs',
    'ElisePunPun': '5977569107:AAEtBZHFtkRUenVFztayXKvHf0pYC-371kU',
    'VapeSingapore': '6194098995:AAG4BMmq3YdxRw4nH9C9540r0Npw0I1kqQs'
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