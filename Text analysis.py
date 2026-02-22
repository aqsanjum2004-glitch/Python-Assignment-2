# Text Analysis Functions Program

def count_words(text):
    words = text.split()
    return len(words)

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def count_consonants(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char.isalpha() and char not in vowels)

def reverse_text(text):
    return text[::-1]

def is_palindrome(text):
    normalized = ''.join(char.lower() for char in text if char.isalnum())
    return normalized == normalized[::-1]

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in text if char not in vowels)

def word_frequency(text):
    freq = {}
    words = text.lower().split()
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

def longest_word(text):
    words = text.split()
    if not words:
        return "", 0
    longest = max(words, key=len)
    return longest, len(longest)

def analyze_text(text):
    print("\n=== TEXT ANALYSIS ===")
    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))
    print("Palindrome:", "Yes" if is_palindrome(text) else "No")
    print("Without vowels:", remove_vowels(text))
    longest, length = longest_word(text)
    print(f"Longest word: {longest} ({length} letters)")
    
    freq = word_frequency(text)
    freq_str = ', '.join(f"{word}: {count}" for word, count in freq.items())
    print("Word Frequency:", freq_str)

# ---------------------------
# Example Usage
# ---------------------------
user_text = input("Enter text: ")
analyze_text(user_text)


Enter text: Python is fun fun
=== TEXT ANALYSIS ===
Words: 4
Vowels: 3
Consonants: 10
Reversed: nuf nuf si nohtyP
Palindrome: No
Without vowels: Pythn s fn fn
Longest word: Python (6 letters)
Word Frequency: python: 1, is: 1, fun: 2
