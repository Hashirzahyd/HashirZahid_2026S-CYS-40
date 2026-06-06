# LAB TASK 02: Write a program that takes a sentence from user and counts vowels and consonants.
sentence = input("Enter sentence: ")
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
for letter in sentence:
    if letter.isalpha():
        if letter in vowels:
            vowel_count = vowel_count + 1
        else:
            consonant_count = consonant_count + 1
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
