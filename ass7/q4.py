def alternate(file1,file2):
    try:
        with open(file1,"r") as source:
            with open(file2,"w")as destination:
                line_number = 1
                for line in source:
                    if line_number % 2 != 0:
                        destination.write(line)
                    line_number+=1
        print("Alternate line copied successfully.")  
    except FileNotFoundError:
        print(f"{file1} is not found.")
    except Exception as e:
        print(e)
     
alternate("text1.txt","text2.txt")
        
        