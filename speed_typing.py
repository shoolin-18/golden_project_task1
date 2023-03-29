from tkinter import *
from tkinter import messagebox
from timeit import default_timer as timer
import random

root = Tk()
root.minsize(500, 500)
root.configure(bg="sky blue")

window = Tk()
window.minsize(550, 500)
window.withdraw()

hs_file = open("highest.txt", "r+")
m = 0


def game():
    global m
    if m == 0:
        root.withdraw()
        m = m + 1
    window.deiconify()

    def check_result():
        j = error = 0
        answer = entry.get("1.0", 'end-1c')
        end = timer()
        time_taken = end - start

        if len(words[word]) >= len(answer):
            error = len(words[word]) - len(answer)
            for i in answer:
                if i == words[word][j]:
                    pass
                else:
                    error += 1
                j += 1
        elif len(words[word]) <= len(answer):
            error = len(answer) - len(words[word])

            for i in words[word]:
                if i == answer[j]:
                    pass
                else:
                    error += 1
                j += 1
        wpm = len(answer) / 5
        wpm = wpm - error
        wpm = int(wpm / (time_taken / 60))
        hs_file.seek(0)
        line = int(hs_file.readline())

        if wpm > line:
            hs_file.seek(0)
            hs_file.write(str(wpm))
            result = "Amazing Your new high score is: " + str(wpm) + "WPM"
            messagebox.showinfo("Score", result)
        else:
            result = "Your score is: " + str(wpm) + " WPM\nBetter luck next time"
            messagebox.showinfo("Score", result)

        

    def finish():
        hs.file.close()
        window.destroy()
        root.destroy()

    words = ["The greatest glory in living lies not in never falling, but in rising every time we fall.",
                     "The way to get started is to quit talking and begin doing.",
                     "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking.",
                     "If life were predictable it would cease to be life, and be without flavor.",
                     "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough.",
                     "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success.",
                     "Life is what happens when you're busy making other plans.",
                     "One day the people that don’t even believe in you will tell everyone how they met you.",
                     "The true meaning of life is to plant trees, under whose shade you do not expect to sit.",
                     "The quick brown fox jumps over the lazy dog."]

    word = random.randint(0, len(words) - 1)

    x2 = Label(window, text=words[word], bg="black", fg="white", height=8, width=121, font="times 15")
    x2.place(x=15, y=15)

    x3 = Button(window, text="Submit!", font="times 20", bg="#fc2828", command=check_result, width=12)
    x3.place(x=1100, y=660)

    entry = Text(window)
    entry.place(x=400, y=450, height=150, width=550)

    b2 = Button(window, text="Done", font="times 13", bg="#fc2828", width=12, command=finish)
    b2.place(x=150, y=660)

    b3 = Button(window, text="Another one", font="times 13", bg="#fc2828", width=12, command=game)
    b3.place(x=265, y=660)

    start = timer()

    window.mainloop()


x1 = Label(root, text="Lets test the typing skill", bg="light blue", fg="white", font="times 20")
x1.place(x=520, y=50)

b1 = Button(root, text="Go!", width=12, bg="light blue", font="times 20", command=game)
b1.place(x=565, y=120)

hs_text = Label(root, text="Highest", width=12, bg="blue", font="times 35")
hs_text.place(x=270, y=240)

hs = int(hs_file.readline())
hs_val = Label(root, text=str(hs) + "WPM", width=12, fg="#03fcf8", bg="black", font="times 35")
hs_val.place(x=720, y=240)

root.mainloop()
