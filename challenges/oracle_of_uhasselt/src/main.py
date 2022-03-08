import os
from dotenv import load_dotenv
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import DES
from telnetserver import TelnetServer

load_dotenv()
flag = os.getenv('FLAG')
key = os.getenv('KEY')
iv = os.getenv('IV')

server = TelnetServer(port=23)
clients = []


def create_cypher():
    return DES.new(key.encode(), DES.MODE_CBC, iv.encode())


def encrypt(plain_text):
    cypher = create_cypher()
    padded_plain_text = pad(plain_text.encode(), DES.block_size)
    cypher_text = cypher.iv + cypher.encrypt(padded_plain_text)
    return cypher_text.hex()


def decrypt(cypher_text):
    cypher = create_cypher()
    padded_plain_text = cypher.decrypt(bytes.fromhex(cypher_text))
    plain_text = unpad(padded_plain_text, DES.block_size)
    return plain_text


if __name__ == '__main__':
    while True:
        server.update()

        # handle new clients
        for new_client in server.get_new_clients():
            clients.append(new_client)
            server.send_message(
                new_client, "Welcome to the oracle of Hasselt University!")
            server.send_message(new_client, "Speak your troubles, student.")
            server._attempt_send(new_client, ">>> ")

        # handle dead clients
        for disconnected_client in server.get_disconnected_clients():
            if disconnected_client not in clients:
                continue
            clients.remove(disconnected_client)

        # handle messages
        for sender_client, message in server.get_messages():
            if sender_client not in clients:
                continue

            server.send_message(new_client, "")
            try:
                _ = decrypt(message)
                server.send_message(
                    sender_client, "The oracle understands your struggles...")
            except Exception as error:
                server.send_message(
                    sender_client, f'The oracle has spoken: "{error}".')
                encrypted_flag = encrypt(flag)
                server.send_message(
                    sender_client, f"Maybe this will lead you? {encrypted_flag}")
            finally:
                server._clients[sender_client].socket.close()
                server._handle_disconnect(sender_client)
