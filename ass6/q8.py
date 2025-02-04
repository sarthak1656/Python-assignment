# Write a function that takes a number as an input parameter and returns the corresponding text in
# words,for example, on input 452, the function should return ‘Four Five Two’. Use a dictionary for
# mappingdigits to their string representation.
def numWord(n):
    dict={"0":"zero","1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"}
    numstr = str(n)
    words=[dict[i] for i in numstr]
    return " ".join(words)


n = input("Enter a number: ")
print(f"{n} = {numWord(n)}")
