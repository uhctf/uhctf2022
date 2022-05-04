# Solution
This is a cryptography challenge. The oracle is a network service. It asks you for your "question", thinks about it, and responds appropriately. If we play around with possible inputs, we discover several different possible responses.

## Error responses
When your input is "incorrect", the oracle will first respond with an error. It also always gives you a long hexadecimal string.

The possible errors are:
- `Data must be hex encoded.`: this implies that your input is expected to be in hexadecimal format.
- `Padding is incorrect.`: encryption functions only work on a fixed amount of bytes called a block. To support arbitrary length inputs, i.e. multiple blocks, a block chaining algorithm/mode of operation is used. Blocks are usually 8 or 16 bytes long. If the data to be encrypted does not align with these boundaries, padding must be added. PKCS-5 and PKCS-7 are simple yet popular padding schemes. This error indicates that the padding scheme was not followed correctly.

## Correct response
When your input is "correct", the oracle responds with `The oracle understands your struggles...`. An example of "correct" input is the long hexadecimal string given to us by the oracle.

## Padding oracle attack
Based on the errors we discovered, we can deduce that we are supposed to provide the oracle with a hexadecimal string. The oracle then converts this to bytes and tries to decrypt it. It responds verbosely based on how far it gets in the decryption process. Applications performing CBC mode symmetric decryption and share whether or not a padding error occurred are vulnerable to the [padding oracle attack](https://book.hacktricks.xyz/cryptography/padding-oracle-priv). This allows attackers to decrypt a cypher text without knowing the password.

The simple explanation requires you to know that encrypted messages can be split up into blocks of bytes. In CBC mode, the encryption/decryption of each block is influenced by the block before it. Broadly speaking, the padding oracle attack is a brute-force attack. For each block in the original cypher text to be decrypted, all blocks up to and including the target block are copied. The block before the target is then replaced with a forged block. This whole forged cypher text is then sent to the application for decryption. We will know that the forged block messed something up if the application, i.e. our oracle, replies with the message "incorrect padding". In this case, the forged block must be tweaked and re-sent. If the oracle accepts the forged cypher text, a different byte is tweaked. The correct value for each byte in each block must be found this way. In the end, some simple XOR operations can reveal the encrypted message.

## Exploit
The most popular script to attack oracles is [PadBuster](https://github.com/AonCyberLabs/PadBuster). However, it is slow and only supports web URIs. A modern version is [rustpad](https://github.com/Kibouo/rustpad). It supports any service with the `script` mode.

The following script allows `rustpad` to talk with the Telnet oracle and parse its response:
```sh
#! /bin/bash

echo ${1} | telnet <IP> | grep 'The oracle understands your struggles...'
```

Decryption of the oracle's message with `rustpad` can be done with the following command:
```sh
rustpad script --oracle ./rustpad_script.sh --block-size 8 --decrypt 4b735e3b6573297482b1c427abf022d6f7d71907bd7ef27fe5490f42c5c00ddcd02939137b5c04b7e1c1835449ba68786ddb928dfe6064d8
```