import base64

def encode_base64(input_text):
    """Mengenkripsi teks menggunakan Base64."""
    message_bytes = input_text.encode('utf-8')
    base64_bytes = base64.b64encode(message_bytes)
    return base64_bytes.decode('utf-8')

def decode_base64(encoded_text):
    """Mendekripsi teks yang di-encode menggunakan Base64."""
    base64_bytes = encoded_text.encode('utf-8')
    message_bytes = base64.b64decode(base64_bytes)
    return message_bytes.decode('utf-8')

if __name__ == "__main__":
    print("Pilih opsi:\n1. Encode Base64\n2. Decode Base64")
    choice = input("Masukkan pilihan (1/2): ")

    if choice == '1':
        text = input("Masukkan teks yang akan di-encode: ")
        encoded_text = encode_base64(text)
        print(f"Teks yang di-encode: {encoded_text}")
    elif choice == '2':
        encoded_text = input("Masukkan teks yang akan di-decode: ")
        decoded_text = decode_base64(encoded_text)
        print(f"Teks yang didecode: {decoded_text}")
    else:
        print("Pilihan tidak valid!")

