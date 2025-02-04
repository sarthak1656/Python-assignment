# Write a Python function that takes two file names, datafile1 and datafile2 as input. The function
# should read the contents of the file datafile1 line by line and should write them to another file
# datafile2 after adding a newline at the end of each line 


def copy(file1,file2):
    try:
        with open(file1,"r") as infile:
            with open(file2,"w") as outfile:
                for line in infile:
                    outfile.write(line.rstrip("/n"+"/n"))
        print(f"Content of {file1} is successfully copied to {file2}.")
    except FileNotFoundError:
        print(f"{file1} is not found")
    except Exception as e:
        print(e)

copy("input1.txt","output1.txt")








