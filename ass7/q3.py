# Write a Python function that takes data to be stored in the file file1 as interactive input from the user
# until he responds with nothing as input. Each line (or paragraph) taken as input from the user should
# be capitalized, and stored in the file file1

def storeInput(file):
    try:
        with open(file,"w") as outfile:
            print("Enter the text to store in the file. Press Enter on an empty line to finish.")

            while True:
                s = input("Enter the text: ")
                if s.strip()=="":
                    break

                outfile.write(s.upper()+"\n")
        print("All the files saved in file.")
    except FileNotFoundError:
        print(f"{file} is not found.")
    except Exception as e:
        print(e)

storeInput("example.txt")

