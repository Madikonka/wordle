from wordlie_pixl_tutorial import Wordle

def main():
    print("helllo!!!!!!!!!!!!!!!!!!!!!!!")
    wordle = Wordle("ogogog")

    while wordle.can_attempt:
        word = input("Please inter the word ")
        wordle.adding_attempts(word)

    if wordle.is_solved: 
        print("You won!")
    else:
        print("Noooooooooooooooooo")




if __name__=="__main__":
    main()