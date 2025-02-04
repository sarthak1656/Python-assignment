# Write a program that takes a sentence as input from the user and computes the frequency of each
# letter. Use a variable of dictionary type to maintain the count


def freq(s):
    f = {}      # Initialize an empty dictionary to store letter counts
    for i in s:      # Iterate through each character in the input string
        if i.isalpha():       # Check if the character is a letter (ignores spaces, digits, punctuation)
            i = i.lower()          # Convert the letter to lowercase to avoid case sensitivity
            if i in f:       # If letter already exists in dictionary
                f[i] += 1      # Increment its count
            else:      # If letter appears for the first time
                f[i] = 1       # Initialize count to 1
    return f  # Return the dictionary with letter frequencies

s = input("Enter a sentence: ")
frequency = freq(s)
print("Letter frequency is: ")
for l,c in sorted(frequency.items()):
    print(f"{l}:{c}")