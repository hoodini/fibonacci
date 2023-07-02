import streamlit as st

english_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
hebrew_alphabet = 'אבגדהוזחטיכלמנסעפצקרשת'
fibonacci_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def encrypt(message, language):
    alphabet = english_alphabet if language == 'english' else hebrew_alphabet
    return ''.join(
        alphabet[(alphabet.index(char.upper()) + fibonacci_sequence[index + 1]) % len(alphabet)] if char.upper() in alphabet else char
        for index, char in enumerate(message)
    )

def decrypt(message, language):
    alphabet = english_alphabet if language == 'english' else hebrew_alphabet
    return ''.join(
        alphabet[(alphabet.index(char.upper()) - fibonacci_sequence[index + 1] + len(alphabet)) % len(alphabet)] if char.upper() in alphabet else char
        for index, char in enumerate(message)
    )

st.markdown("# Yuval's Fibonacci Cipher")

message = st.text_input('Enter your message here')
language = st.selectbox('Select language', ['hebrew', 'english'])

if st.button('Encrypt'):
    result = encrypt(message, language)
    st.text_input('Encrypted message:', result)

if st.button('Decrypt'):
    result = decrypt(message, language)
    st.text_input('Decrypted message:', result)
