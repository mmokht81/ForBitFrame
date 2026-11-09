def word_counter():
    words = text.split()

    print("Total words:", len(words))

    word_count = {} # saving word in dict-> key: word + value: number of repetitions 

    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
    for word, count in word_count.items():
        print(word, ":", count)
    
while True:
    text = input("Enter text OR 0 for exit: ")
    
    if text == "0":
        break
    else:
        print("\nWord repetitions: ")
        word_counter()