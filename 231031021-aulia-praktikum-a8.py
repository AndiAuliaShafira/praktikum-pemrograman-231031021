import random
import string

def generasi_twitter_password():
    uppercase_letters = string.ascii_lowercase
    lowercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = '!@#$%^&*()_+-=[]{}|:;<>,.?/~'

    first_layer = lowercase_letters + uppercase_letters + digits + symbols
    first_layer = [random.choice(first_layer) for _ in range(4)]

    second_layer_password = random.choices(
        lowercase_letters + uppercase_letters + digits + symbols,
        k=8
        )

    password = first_layer_password + second_layer_password

    random.shuffle(password)
    final_password = ''.join(password)

    return final_password

def get_user_input():
    while True:
        password1 = input('Masukkan Password: ')
        password2 = input('Masukkan Password Kembali: ')

        if password1 == password2:
            return password1
        else:
            print('Password Tidak Cocok. Silakan Coba Lagi.')

user_password = get_user_input()
generated_password = generate_twitter_password()

print('Password Yang Anda Masukkan:', user_password)
print('Password Twitter Kembali:', generated_password)
