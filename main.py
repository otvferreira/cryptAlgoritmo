from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    return private_key, public_key

def encrypt_message(public_key, message):
    ciphertext = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

def decrypt_message(private_key, ciphertext):
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode()

def save_keys_to_files(private_key, public_key):

    with open("private_key.pem", "wb") as private_file:
        private_file.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            )
        )

    with open("public_key.pem", "wb") as public_file:
        public_file.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )

def load_keys_from_files():

    with open("private_key.pem", "rb") as private_file:
        private_key = serialization.load_pem_private_key(
            private_file.read(),
            password=None,
        )

    with open("public_key.pem", "rb") as public_file:
        public_key = serialization.load_pem_public_key(
            public_file.read(),
        )
    return private_key, public_key

if __name__ == "__main__":
    print("Par de chaves...")
    private_key, public_key = generate_keys()
    save_keys_to_files(private_key, public_key)
    print("Chaves salvas")

    print("\nCarregando chaves")
    private_key, public_key = load_keys_from_files()

    mensagem = input("\nDigite a mensagem que deseja cifrar ")
    print(f"\nMensagem: {mensagem}")

    print("\nCifrando mensagem")
    mensagem_cifrada = encrypt_message(public_key, mensagem)
    print(f"Mensagem cifrada (em bytes): {mensagem_cifrada}")

    print("\nDecifrando mensagem")
    mensagem_decifrada = decrypt_message(private_key, mensagem_cifrada)
    print(f"Mensagem decifrada: {mensagem_decifrada}")
