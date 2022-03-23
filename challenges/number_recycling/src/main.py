from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from asn1crypto import pem
from asn1crypto.keys import PublicKeyInfo
from math import gcd, ceil
import sys

FLAG = 'uhctf{sharing-is-not-always-caring-cc324c}'
EXPONENT1 = 65537
EXPONENT2 = 42337
PEM_1_FILENAME = 'key1.pem'
PEM_2_FILENAME = 'key2.pem'
CYPHER_1_FILENAME = 'cypher1.hex'
CYPHER_2_FILENAME = 'cypher2.hex'

KEY_SIZE = 2048
output_dir = ''


def der_to_pem(der_bytes):
    return pem.armor('PUBLIC KEY', der_bytes)


def generate_public_key():
    private_key = rsa.generate_private_key(
        public_exponent=EXPONENT1,
        key_size=KEY_SIZE
    )
    return private_key.public_key().public_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )


def tweak_exponent(der_bytes):
    parsed_keyinfo = PublicKeyInfo.load(der_bytes)
    parsed_pubkey = parsed_keyinfo['public_key'].parsed
    parsed_pubkey['public_exponent'] = EXPONENT2

    parsed_keyinfo['public_key'].set(parsed_pubkey.contents)
    # `force=True` prevents usage of cache
    return parsed_keyinfo.dump(force=True)


def create_similar_keys():
    try:
        assert(gcd(EXPONENT1, EXPONENT2) == 1)
    except:
        print('Exponents must be coprime for common modulo attack to work')
        exit(1)

    key1 = generate_public_key()
    key2 = tweak_exponent(key1)

    global output_dir
    with open(output_dir + PEM_1_FILENAME, 'w') as f:
        f.write(der_to_pem(key1).decode('utf-8'))
    with open(output_dir + PEM_2_FILENAME, 'w') as f:
        f.write(der_to_pem(key2).decode('utf-8'))


def encrypt(message, key):
    # The simplest form of common modulo attack only works without padding. However, the `cryptography` library's API does not support encrypting without padding as it's insecure. We need to re-implement encryption. This is sadly slow but w/e.
    message_int = int.from_bytes(message.encode(), byteorder='big')
    cypher_text_int = pow(
        message_int, key.public_numbers().e, key.public_numbers().n)
    return cypher_text_int.to_bytes(ceil(cypher_text_int.bit_length() / 8), byteorder='big')


def write_cyphertext(file_name, cyphertext):
    global output_dir
    with open(output_dir + file_name, 'w') as f:
        f.write(cyphertext.hex())


def create_encrypted_messages():
    global output_dir
    with open(output_dir + PEM_1_FILENAME, 'rb') as f:
        key = load_pem_public_key(f.read())
        write_cyphertext(CYPHER_1_FILENAME, encrypt(FLAG, key))
    with open(output_dir + PEM_2_FILENAME, 'rb') as f:
        key = load_pem_public_key(f.read())
        write_cyphertext(CYPHER_2_FILENAME, encrypt(FLAG, key))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: ./main.py <output_dir>')
        exit(1)
    output_dir = sys.argv[1] if sys.argv[1][-1] == '/' else sys.argv[1] + '/'

    create_similar_keys()
    create_encrypted_messages()
