# Random secret generator

import os
import binascii

def add_secret(app):
    # Generates a random 24 bit string 
    secret_key_value = os.urandom(24)
    # Create the hex-encoded string value.
    secret_key_value_hex_encoded = binascii.hexlify(secret_key_value)
    # Set the SECRET_KEY value in Flask application configuration settings.
    app.config['SECRET_KEY'] = secret_key_value_hex_encoded
