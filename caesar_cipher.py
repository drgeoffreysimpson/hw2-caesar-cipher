from pathlib import Path

class CaesarCipher:
    def __init__(self, key=3):
        pass


    def encrypt(self, plaintext):
        ''' 
        Task 1: encrypt plaintext using caesar cipher
        '''

        return True


    def decrypt(self, ciphertext):
        ''' 
        Task 2: decrypt ciphertext using caesar cipher
        '''

        return True
    

    def encrypt_file(self, input_filename, output_filename):
        '''
        Task 3: encrypt the content in a file (input_filename) using caesar cipher 
                and store the ciphertext in another file (output_filename)
        '''

        pass


    def decrypt_file(self, input_filename, output_filename):
        '''
        Task 4: decrypt the content in a file (input_filename) using caesar cipher 
                and store the decrypted text in another file (output_filename)
        '''

        pass


if __name__ == "__main__":
    caesar_cipher = CaesarCipher()
    print(caesar_cipher.encrypt('This is a secret message! My password is XYZ.'))
    print(caesar_cipher.decrypt('Hello ABC!'))
    caesar_cipher.encrypt_file('secret_message.txt', 'encrypted_secret_message.txt')
    caesar_cipher.decrypt_file('encrypted_secret_message.txt', 'decrypted_text.txt')

