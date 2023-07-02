import streamlit as st

english_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
hebrew_alphabet = 'אבגדהוזחטיכלמנסעפצקרשת'

def generate_fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def encrypt(message, language):
    alphabet = english_alphabet if language == 'english' else hebrew_alphabet
    fibonacci_sequence = generate_fibonacci_sequence(len(message)+1)
    return ''.join(
        alphabet[(alphabet.index(char.upper()) + fibonacci_sequence[index + 1]) % len(alphabet)] if char.upper() in alphabet else char
        for index, char in enumerate(message)
    )

def decrypt(message, language):
    alphabet = english_alphabet if language == 'english' else hebrew_alphabet
    fibonacci_sequence = generate_fibonacci_sequence(len(message)+1)
    return ''.join(
        alphabet[(alphabet.index(char.upper()) - fibonacci_sequence[index + 1] + len(alphabet)) % len(alphabet)] if char.upper() in alphabet else char
        for index, char in enumerate(message)
    )

st.markdown("# Fibonacci Cipher by Yuval Avidani @hackit.co.il")

message = st.text_input('Enter your message here')
language = st.selectbox('Select language', ['hebrew', 'english'])

if st.button('Encrypt'):
    result = encrypt(message, language)
    st.text_input('Encrypted message:', result)

if st.button('Decrypt'):
    result = decrypt(message, language)
    st.text_input('Decrypted message:', result)
