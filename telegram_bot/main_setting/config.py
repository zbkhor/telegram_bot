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
    'test': '-856941379',
    'test2':'-4117172640'
}

bot_tokens = {
    'Yuyuna': '5753903548:AAGzb92AMdhYEYMy_b0zMA0xUEEsX2qQaEk',
    'Chloe': '6703426544:AAHowvJhuVV4IkdguYT2iS7TuRQWX3UGSK0',
    'Seraphine': '6887431223:AAEJc4s3t_hA7DxrcO-k0NvqtgrkjPUMexU',
    'Celeste': '6787601158:AAE4N-FWjAyE3NHKGD35nVnHt-c-o6Ptedo',
    'Scarlett': '6371828828:AAErfPToRZwoyFTcZ1jnwGRUbbg5_rlKp9M',
    'Camila': '6763843999:AAGPRm9iB_GyyTKW7q6M3pY_BDA7YAUzJwU',
}

# Use Constants
SEND_INTERVAL_1 = 1
SEND_INTERVAL_2 = 1

# Define Bot Configurations
Yuyuna = {
    "token": bot_tokens['Yuyuna'],
    "chat_ids": [chat_ids['test'],chat_ids['test2']],
    "strings": [paragraph1],    
    "send_interval": SEND_INTERVAL_1
}

Chloe = {
    "token": bot_tokens['Chloe'],
    "chat_ids": [chat_ids['test'],chat_ids['test2']],
    "strings": [paragraph1],
    "send_interval": SEND_INTERVAL_2
}

Seraphine = {
    "token": bot_tokens['Seraphine'],
    "chat_ids": [chat_ids['test'],chat_ids['test2']],
    "strings": [paragraph1],
    "send_interval": SEND_INTERVAL_1  # Adjust as needed
}

Celeste = {
    "token": bot_tokens['Celeste'],
    "chat_ids": [chat_ids['test'],chat_ids['test2']],
    "strings": [paragraph1],
    "send_interval": SEND_INTERVAL_2  # Adjust as needed
}

Scarlett = {
    "token": bot_tokens['Scarlett'],
    "chat_ids": [chat_ids['test'],chat_ids['test2']],
    "strings": [paragraph1],
    "send_interval": SEND_INTERVAL_1  # Adjust as needed
}
Camila = {
    "token": bot_tokens['Camila'],
    "chat_ids": [chat_ids['test'],chat_ids['test2']],
    "strings": [paragraph1],
    "send_interval": SEND_INTERVAL_1  # Adjust as needed
}

# Create a List of Bot Configurations
chat_configs = [Yuyuna, Chloe, Seraphine , Celeste, Scarlett, Camila]
# chat_configs = [Yuyuna, Chloe]
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
