import pytest
from pathlib import Path
from caesar_cipher import CaesarCipher

def test_caesar_cipher_1():
    cipher = CaesarCipher()
    assert cipher.encrypt('Hi, my name is Weiping.') == 'KL, PB QDPH LV ZHLSLQJ.' 
    assert cipher.decrypt('WKLV LV D VHFUHW PHVVDJH! PB SDVVZRUG LV ABC.') == 'THIS IS A SECRET MESSAGE! MY PASSWORD IS XYZ.' 


def test_caesar_cipher_2():
    cipher = CaesarCipher()
    cipher.encrypt_file('secret_message.txt', 'encrypted_secret_message.txt')
    path = Path('encrypted_secret_message.txt')
    assert path.read_text() == 'KHOOR, WKLV LV D VHFUHW PHVVDJH!\nBRXU SDVVZRUG LV QGVFVA&V091WVAVD^\n'      
    cipher.decrypt_file('encrypted_secret_message.txt', 'decrypted_secret_message.txt')
    path = Path('decrypted_secret_message.txt')
    assert path.read_text() == 'HELLO, THIS IS A SECRET MESSAGE!\nYOUR PASSWORD IS NDSCSX&S091TSXSA^\n'  
