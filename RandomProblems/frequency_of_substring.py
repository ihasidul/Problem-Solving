#!/usr/bin/python

#Write a program which will find all occurrences of a pattern in a text.
#Suppose there is a text “tadadattaetadadadafa” and a pattern “dada”, now you 
#have to find how many times “dada” appear in “tadadattaetadadadafa”.
#Here the pattern (dada) appears in text (tadadattaetadadadafa) 3 times.

def count_substring(string,sub_string):
    l=len(sub_string)
    count=0
    for i in range(len(string)-len(sub_string)+1):
        if(string[i:i+len(sub_string)] == sub_string ):      
            count+=1
    return count  

def main():
    string  = "tadadattaetadadadafa"
    sub_string = "dada"
    print("Number of occurrence: ", count_substring(string, sub_string))

if __name__ == "__main__":
    main()
