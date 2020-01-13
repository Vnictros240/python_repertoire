#!/usr/bin/python3

# Program for adding data to a file
#  -- Takes input and prints it to screen.
#  -- Takes input and appends to file.

#     user = input("Enter Username: ")
#     if username == "pypy":
#         break
#     else:
#         continue
# start adding more code here for inputTxt_to_Screen
# -- while loop with list
# -- The more USER input is added then append to list
# for every item in the list, print it to screen.
def sentenceMaker(phrase):
    interrogatives = ('who', 'how', 'what', 'when', 'where', 'why')
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

def sentenceConvo():
    paragraph = []
    while True:
        print("To exit, type '/end' . ")
        userInput = input("Speak you mind: ")
        if userInput == "/end":
            break
        else:
            paragraph.append(sentenceMaker(userInput))
    return paragraph

def sentenceMaker(phrase):
    capitalized = phrase.capitalized()
    if phrase:


# <h2>Faith Pg. 7 of 37</h2>
# <br>
#
#
#
# Acts 11:24 (context: 19 - 26)<br>
# <br><br>
#
#   <span class="greek">&pi;&iota;&sigma;&tau;&epsilon;&omega;&#962;</span>
#     <br><code>gen. sing. fem. <br>
#
#   English: faith, believeth, believe </code><br>
#   <br>

def htmlContentHelper():
    with open("htmlhlpr.txt", "a+") as htmlhlpr:
        while True:
            scripture = input("What's the scripture? ")
            bible_context = input("What's the context? ")
            htmlhlpr.write("\n%s (context: %s)<br>\n<br><br>\n" % (scripture, context))
    print("To exit type '/end'.")
    # while True:
        # userInput = input("HTML input? ")
        # userInput = userInput.lower()
        # if userInput == "/end":
        #     break
        # else:
        #     para.append(userInput)
    pass


inputTxt_to_Screen()
