"""
Generate an RSA keypair with an exponent of 65537 in PEM format
param: bits The key length in bits
Return private key and public key

IMPORTANT! INSTALL PyCryptodome
---->  pip3 install -U PyCryptodome  <----

Bits length of the RSA key is the first argument e.g.
---->  python3 rsa.py 1024  <----
"""

import sys
from os import path
from Crypto.PublicKey import RSA


def generate_rsa(bits_length: int) -> tuple:
    """Generates the RSA key."""
    new_key: RSA.RsaKey = RSA.generate(bits_length, e=65537)
    public_key: bytes = new_key.publickey().exportKey(format='PEM')
    private_key: bytes = new_key.exportKey(format='PEM')
    return private_key, public_key


if __name__ == "__main__":
    try:
        bits_len: int = int(sys.argv[1])
    except ValueError:
        print(f'Use: {path.basename(__file__)} <int>')
        sys.exit(1)

    with open(file='RSA_KEY.txt', mode='w', encoding='utf-8') as rsa_key:
        rsa_key.write(str(generate_rsa(bits_length=bits_len)))
