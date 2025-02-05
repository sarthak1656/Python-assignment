'''l1=[1,2,3,4]
l2=[1,2,3,4]
if sorted(l1)==sorted(l2):
    print("true")
else:
    print("False")'''





'''mylist = [10,20,30,40,50]
print(mylist[10])'''





'''keys=["name","age","city"]
values=["sarthak",21,"bhubaneswar"]
mydist={}
for i in range(len(keys)):
                  mydist[keys[i]]=values[i]

print(mydist)'''






'''def cdist(ipdist):
    csum = 0
    result={}

    for key,value in ipdist.items():
        csum += value
        result[key]=csum
    return result

user_dict = {"a": 10, "b": 20, "c": 30, "d": 40}
print(cdist(user_dict))'''







def count(f1):
    try:
        with open(f1,"w") as outfile:
            outfile.write("hello world")
        with open(f1,"r") as infile:
            text=infile.read()
            words=text.split()
            num_word=len(words)

        print(f"number of words in {f1} is {num_word}")
    except Exception as e:
        print(e)

count("f1.txt")




'''def storeInput(f1):
    with open (f1,"w") as file:
        print("Enter the test to store in file press enter in a empty line to finsish")

        while True:
            userinput=input("Enter a text: ")
            if userinput.strip()=="":
                break
            file.write(userinput.upper()+"\n")
    with open(f1,"r") as infile:
        print(f"\nFile saved in {f1} is: \n")
        print(infile.read())

storeInput("f2.txt")'''
        

    



                
