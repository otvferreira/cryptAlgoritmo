```markdown
# Cifragem e Decifragem RSA

Este projeto demonstra como implementar cifragem e decifragem RSA em Python utilizando a biblioteca `cryptography`. Ele inclui funções para gerar pares de chaves RSA, cifrar e decifrar mensagens, além de salvar/carregar as chaves em arquivos.

## Funcionalidades

- **Geração de Chaves**: Gera um par de chaves RSA (privada e pública).
- **Cifragem de Mensagens**: Cifra mensagens utilizando a chave pública.
- **Decifragem de Mensagens**: Decifra mensagens utilizando a chave privada.
- **Armazenamento de Chaves**: Salva as chaves RSA em arquivos `.pem`.
- **Carregamento de Chaves**: Carrega as chaves RSA a partir de arquivos `.pem`.

## Requisitos

- Python 3.6 ou superior
- Biblioteca `cryptography`

Instale a biblioteca `cryptography` com o comando:

```bash
pip install cryptography
```

![image](https://github.com/user-attachments/assets/5ef9a14d-73d0-4cfd-9b17-f7298a3bfc28)

## Como Utilizar

### 1. Gerar o Par de Chaves RSA
A função `generate_keys()` cria um par de chaves RSA:
- **Chave Privada**: Usada para decifragem.
- **Chave Pública**: Usada para cifragem.

As chaves são salvas em arquivos utilizando a função `save_keys_to_files()`.

### 2. Cifrar uma Mensagem
Use a função `encrypt_message()` para cifrar uma mensagem em texto claro utilizando a chave pública.

### 3. Decifrar uma Mensagem
Use a função `decrypt_message()` para decifrar uma mensagem cifrada utilizando a chave privada.

### 4. Salvar e Carregar Chaves
- As chaves são salvas nos arquivos `private_key.pem` e `public_key.pem` usando a função `save_keys_to_files()`.
- As chaves podem ser carregadas a partir desses arquivos usando a função `load_keys_from_files()`.

## Execução

1. **Geração de Chaves**: Ao executar o script, um par de chaves será gerado e salvo em arquivos.
2. **Entrada de Mensagem**: O usuário será solicitado a inserir uma mensagem para cifrar.
3. **Cifragem e Decifragem**: A mensagem será cifrada com a chave pública e decifrada com a chave privada.

## Estrutura do Código

- `generate_keys()`: Gera o par de chaves RSA.
- `encrypt_message(public_key, message)`: Cifra uma mensagem usando a chave pública.
- `decrypt_message(private_key, ciphertext)`: Decifra uma mensagem cifrada usando a chave privada.
- `save_keys_to_files(private_key, public_key)`: Salva as chaves RSA em arquivos `.pem`.
- `load_keys_from_files()`: Carrega as chaves RSA de arquivos `.pem`.

## Exemplo de Uso

```bash
python rsa_encryption.py
```

### Exemplo de Saída

```plaintext
Par de chaves...
Chaves salvas

Carregando chaves

Digite a mensagem que deseja cifrar: Olá, mundo!

Mensagem: Olá, mundo!

Cifrando mensagem
Mensagem cifrada (em bytes): b'\x93\x85...\x1e'

Decifrando mensagem
Mensagem decifrada: Olá, mundo!
```
