from cryptography.fernet import Fernet

class Crypt:
    # Функция для шифрования текста
    def encrypt_message(self, key, message):
        try:
            fernet = Fernet(key)
            encrypted_message = fernet.encrypt(message.encode())
            return encrypted_message
        except Exception as e:
            return None

    # Функция для расшифровки текста
    def decrypt_message(self, key, encrypted_message):
        try:
            fernet = Fernet(key)
            decrypted_message = fernet.decrypt(encrypted_message).decode()
            return decrypted_message
        except Exception as e:
            return None
