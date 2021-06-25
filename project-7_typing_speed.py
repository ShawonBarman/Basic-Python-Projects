from time import time  #to record the time

#now to calculate the accuracy of imput prompt
def tperror(prompt):
    global inwords

    words = prompt.split()
    errors = 0

    for i in range(len(inwords)):
        if i in (0, len(inwords)-1):
            if inwords[i] == words[i]:
                continue
            else:
                errors += 1
        else:
            if inwords[i] == words[i]:
                if (inwords[i+1]==words[i+1]) & (inwords[i-1] == words[i-1]):
                    continue
                else:
                    errors += 1
            else:
                errors += 1
    return errors

#how to calculate the speed of typing words per minute
def speed(inprompt):
    global time
    global inwords

    inwords = inprompt.split()
    twords = len(inwords)
    speed = twords/time

    return speed

#calculate the total elapsed time
def elapsedtime(stime, etime):
    time = stime - etime
    return time

if __name__=="__main__":
    prompt = "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects. Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structure, object-oriented, and functional programming. Python is often described as a batteriesincluded language due to its comprehensive standard library."
    #this was the paragrao=ph which you have t type to check your speed
    print("Type this :- ",prompt)

    #checking to input enter basically it will see
    input("Press enter when you are ready to check your speed!!!")

    #recording time for imput
    stime = time()
    inprompt = input()
    etime = time()

    #collect all the information returned by the functions
    time = round(elapsedtime(stime,etime),2)
    speed = speed(inprompt)
    errors = tperror(prompt)

    #printing all the required data to see result
    print("Total time elapsed: ",abs(time), "seconds")
    print("Your average typing speed was ",abs(speed), "words per minutes")
    print("With the total of ",errors, "errors.")