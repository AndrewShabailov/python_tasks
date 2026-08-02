import string


def is_pangram(st: str) -> bool:
    alphabet = set(string.ascii_lowercase)
    st_letters = set(st.lower())
    return alphabet.issubset(st_letters)
