def read_input():

    word = input("Sentence: ")
    
    word = word.lower()

    return word


def splitterCount(word):

    count = 0
    split_by_space = word.split(" ")
    print(split_by_space)

    for i in range(split_by_space):
        split_by_stretch = split_by_space[i].split("z")

        for j in range(split_by_stretch):
            
            if is2count(split_by_stretch[j]):
                count += 1
                break

    return count

def isVowel(c):
    
    c = c.lower()
    
    return "aeiou".find(c) != -1


def is2count(word):
    
    count = 0
    for i in range(len(word)-1):
        
        if isVowel(word[i]):
            count += 1
    
    return count == 2

def main():
   
    word = read_input()
    
    while word != '*':

        count = splitterCount(word)

        print("Matching Words = " + str(count))

        word = read_input()

    print("Done")
    
if __name__ == '__main__':
    #Write your code here
    main()