def count(file1):
    try:
        with open(file1,"r") as infile:
            text = infile.read()
        words = text.split()
        num_words = len(words)
        vowels="aeiouAEIOU"
        num_vowels = 0
        for char in text:
            if char in vowels:
                num_vowels += 1
        print(f"Number of words in line {num_words}")
        print(f"Number of vowels in line {num_vowels}")

    except FileNotFoundError:
        print(f"{file1} is not found")
    except Exception as e:
        print(e)

count("file1.txt")