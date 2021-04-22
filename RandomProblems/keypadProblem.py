# Write a program that will print out the coordinates of input keypad string.
#Example for 7 the output should be (0,0)
#For 3 it is (2,2) and so on
def keyCordinate(key: str) -> str:
    keyDict = {
       "0" : "(1,-1)",
       "1" : "(0,2)",
       "2" : "(1,2)",
       "3" : "(2,2)",
       "4" : "(0,1)",
       "5" : "(1,1)",
       "6" : "(1,2)",
       "7" : "(0,0)",
       "8" : "(1,0)",
       "9" : "(2,0)" 
    }
    for _ in keyDict:
        if(_ == key):
            return keyDict[_]
    else:
        return "There is an error in your input"
def main():
    key = input("Input your key between 0 and 9 ")
    print("The coordinates of the input is ", keyCordinate(key))

if __name__ == "__main__":
    main()