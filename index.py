import time
from telethon.sync import TelegramClient
from telethon.errors import FloodWaitError

# Substitua com seus próprios valores de API
api_ids = [1234567]  # Lista de API IDs como inteiros
api_hashes = ['your_api_hash_here']  # Lista de API Hashes como strings
phone_numbers = ["+5511912345678"]  # Lista de números de telefone como strings

# Adicione os destinatários, mensagens e caminhos das imagens
recipients = [
    {'username': 'username1', 'message': 'Sua mensagem aqui', 'image_path': '/caminho/para/imagem.jpg'},
    # Adicione mais destinatários conforme necessário
]

def send_image_with_caption(client, recipient, message, image_path):
    try:
        # Ajuste o texto da legenda conforme necessário
        caption_with_link = f"{message}\n\n[Texto do Link](URL)\n\n[Outro Texto do Link](URL)"
        # Correção: Adicionando a legenda na chamada de envio
        client.send_file(recipient, image_path, caption=caption_with_link, parse_mode='md')
        print(f"Imagem com legenda enviada para {recipient}.")
    except FloodWaitError as e:
        print(f"Aguardando {e.seconds} segundos devido à limitação de taxa.")
        time.sleep(e.seconds)
        send_image_with_caption(client, recipient, message, image_path)
    except Exception as e:
        print(f"Erro ao enviar imagem com legenda para {recipient}: {e}")

for i, recipient in enumerate(recipients):
    api_id = api_ids[i % len(api_ids)]
    api_hash = api_hashes[i % len(api_hashes)]
    phone_number = phone_numbers[i % len(phone_numbers)]

    with TelegramClient(phone_number, api_id, api_hash) as client:
        client.start()
        send_image_with_caption(client, recipient["username"], recipient["message"], recipient["image_path"])
        client.disconnect()

    # Ajuste o tempo de espera conforme necessário para evitar FloodWaitError
    time.sleep(10)  # Menor tempo de espera para demonstração

print("Todas as imagens com legendas foram enviadas.")
