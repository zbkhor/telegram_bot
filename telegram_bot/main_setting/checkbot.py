import requests

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
    'Camila': '6763843999:AAGPRm9iB_GyyTKW7q6M3pY_BDA7YAUzJwU',
    'Merlion': '6080654541:AAEa1upiGaQdcZJlLx4b4lRNJwAF7AOAzNs',
    'ElisePunPun': '5977569107:AAEtBZHFtkRUenVFztayXKvHf0pYC-371kU',
    'VapeSingapore': '6194098995:AAG4BMmq3YdxRw4nH9C9540r0Npw0I1kqQs'
}

def is_bot_in_chat(bot_token, chat_id):
    url = f'https://api.telegram.org/bot{bot_token}/getChat'
    params = {'chat_id': chat_id}
    response = requests.get(url, params=params)

    result = response.json()
    bot_name = next((name for name, token in bot_tokens.items() if token == bot_token), None)
    if result['ok'] and 'type' in result['result']:
        if 'title' in result['result']:
            print(f"Bot '{bot_name}' is in chat '{result['result']['title']}'")
        else:
            print(f"Bot '{bot_name}' is in chat (no group name)")
    else:
        chat_name = next((name for name, cid in chat_ids.items() if cid == chat_id), None)
        print(f"Bot '{bot_name}' is not in chat '{chat_name}'")

# Loop through every bot token
for bot_token in bot_tokens.values():
    for chat_id in chat_ids.values():
        is_bot_in_chat(bot_token, chat_id)
