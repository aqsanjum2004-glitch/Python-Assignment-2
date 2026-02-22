
# Step 1: Get input from user
sentence = input("Enter a sentence: ")

# Step 2: Display original sentence
print("\nOriginal:", sentence)

# Step 3: Count characters (with spaces)
print("Characters (with spaces):", len(sentence))

# Step 4: Count characters (without spaces)
characters_no_space = 0
for letter in sentence:
    if letter != " ":
        characters_no_space += 1
print("Characters (without spaces):", characters_no_space)

# Step 5: Count words
word_list = sentence.split()
print("Words:", len(word_list))

# Step 6: Case conversions
print("UPPERCASE:", sentence.upper())
print("lowercase:", sentence.lower())
print("Title Case:", sentence.title())

# Step 7: First and Last word
if len(word_list) > 0:
    print("First word:", word_list[0])
    print("Last word:", word_list[-1])
else:
    print("First word: N/A")
    print("Last word: N/A")

# Step 8: Reverse sentence
reverse_text = ""
for letter in sentence:
    reverse_text = letter + reverse_text

print("Reversed:", reverse_text)

# End of Program
