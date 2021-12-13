from time import *
import threading
import sys
if len(sys.argv) != 3:
    print("You must write two arguments for this program")
    sys.exit()

file1 = sys.argv[1]
file2 = sys.argv[2]

format = "utf-8"

f1 = open(file1, 'r', encoding=format)
f2 = open(file2, 'r', encoding=format)

dictionary = {}
letter_dic = {}
keys_list = []
value_list = []
guessed_words = []

for line in f1:
  (key1, value1) = line.rstrip().split(":")
  dictionary[key1] = value1
for line in f2:
  (key1, value1) = line.rstrip().split(":")
  letter_dic[key1] = int(value1)

for key in dictionary:
    keys_list.append(key)

x = 0
y = 0
s = "-"
score = 0
score1 = 0
b = dictionary[keys_list[x]]

while x < len(keys_list):
    b = dictionary[keys_list[x]]
    print("Shuffled letters are: " + str(keys_list[x]).replace("İ","i").lower() + " Please guess words for these letters with minimum three letters")
    def countdown():
        global my_timer
        my_timer = 30
        for j in range(30):
            my_timer = my_timer - 1
            sleep(1)
    countdown_thread = threading.Thread(target = countdown)
    countdown_thread.start()
    while y < int(len(b.split(","))):
        a = str(input("Guessed Word: ")).upper().replace("I","İ")

        for i in guessed_words:
            if a == i and my_timer != 0:
                print("This word is guessed before")
        if my_timer == 0:
            y = int(len(b.split(",")))
        elif len(a) < 4:
            print("Your guessed word is not a valid word")
        elif a in str(dictionary[keys_list[x]]) and a not in guessed_words:
            guessed_words.append(a)
            y += 1
        elif a not in dictionary[keys_list[x]]:
            print("Your guessed word is not a valid word")
        print("You have " + str(my_timer) + " time")

    for i in guessed_words:
        for j in i:
            j = letter_dic[j]
            score1 += j
        score1 *= len(i)
        score = score + score1
        score1 = 0

    if score == 0:
        print("Score for " + str(keys_list[x]).replace("İ","i").lower() + " is " + str(score) +" and no words were guessed(correctly)")
    else:
        print("Score for " + str(keys_list[x]).replace("İ","i").lower() + " is " + str(score) +" and guessed words are: " + s.join(guessed_words).replace("İ","i").lower())
    guessed_words = []
    score = 0
    y = 0
    x += 1
    my_timer = 30
sys.exit()
