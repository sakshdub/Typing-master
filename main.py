from tkinter import *
import random
import time
def start_game():
    result_label.config(text="")
    sentences = [
        "Self-confidence is a tricky subject for many people. For some, it's impossible to feel good about themselves without outside validation. When you're in a situation where the people in your life aren't helping you to feel better about yourself, this can become a problem in your day to day life. Most insecurity stems from feelings of not being attractive or feelings of loneliness. If your insecurity doesn't necessarily stem from a lack of interaction, but more a lack of feeling attractive, there are other options that will help you online. Sometimes the best way to put your insecurities to rest can simply be to get an honest opinion. There are multiple support groups online where you can share a picture of yourself with other members and they will give honest feedback on your appearance. In most cases, they will point out good qualities that you may have missed in yourself. But you can trust them to be honest and many members give very valuable style and posture advice to increase your attractiveness. These practical tips and unbiased opinions from supportive strangers will immediately help you feel better about yourself, and if the tips are implemented it will also improve your self-esteem in the long-run.",
        "In the hustle and bustle of daily life, it's easy to neglect our own well-being. But remember, you can't pour from an empty cup. Taking care of your physical and mental health is crucial for maintaining high self-confidence, motivation, and overall productivity. Make time for activities that nourish your mind, body, and spirit. Prioritize sleep, exercise, and a balanced diet. Engage in hobbies that bring you joy and relaxation. Remember, self-care isn't selfish; it's an investment in your long-term happiness and success.",
        "Engineers, as practitioners of engineering, are people who invent, design, analyze, build, and test machines, systems, structures and materials to fulfill objectives and requirements while considering the limitations imposed by practicality, regulation, safety, and cost. The work of engineers forms the link between scientific discoveries and their subsequent applications to human and business needs and quality of life."
    ]
    global text_to_type
    global total_words
    text_to_type=random.choice(sentences)
    total_words=len(text_to_type.split())
    text_widget.delete(1.0,END)
    text_widget.insert(END,text_to_type)
    typing_area.delete(0, END)

    # //timer
    timer_label.config(text="60")
    countdown(60)

    # for secs in range(60, 0, -1):
    #     time.sleep(1)
    #     timer_label.config(secs)

    typing_area.focus()

    # Bind the entry box to check the input
    typing_area.bind("<KeyRelease>", check_typing)
def countdown(secs):
    if secs>0:
        timer_label.config(text=str(secs))
        window.after(1000,countdown,secs-1)  # Call countdown again after 1 second
    else:
        calculate_wpm()
def check_typing(event):
    typed_text = typing_area.get()
    typed_words=typed_text.split()
    original_words=text_to_type.split()
    correct_words=0
    for i in range(min(len(typed_words),len(original_words))):

        if typed_words[i]==original_words[i]:
            correct_words+=1
        else:
            break
    result_label.config(text=f"Correct Words: {correct_words}/{len(original_words)}", fg="blue")

def calculate_wpm():
    typed_text=typing_area.get()
    correct_words = sum(1 for word in typed_text.split() if word in text_to_type.split())
    total_words=len(text_to_type.split())
    minutes=1   #for 60sec
    wpm=(correct_words/minutes)
    accuracy=(correct_words/total_words)*100 if total_words>0 else 0
    result_label.config(text=f"Time's up! You typed {correct_words} out of {total_words} words correctly. WPM: {wpm:.2f} and  Accuracy:{accuracy:2f}%", fg="blue")
window=Tk()
window.minsize(width=800,height=700)
window.title("Test your speed")
window.configure(bg="#AEEEEE")  # Light gray background




# starting headings...
label1=Label(text="TEST YOUR SKILLS IN TYPING",font=("Thorletto Regular", 24, "bold"),fg="red")
label_2=Label(text="You will never stub your toe standing still, but the faster you go, the more chance you have of getting somewhere.",font=("Aerial", 10, "bold"))
label1.pack()
label_2.pack()

timer_label=Label(text="60",font=("Aerial",14))
timer_label.pack()
text_widget=Text(width=50,height=10,font=("Arial", 16),wrap=WORD)
text_widget.pack(pady=20)
text_to_type = "The quick brown fox jumps over the lazy dog."
typing_area = Entry(window, font=("Arial", 14), width=50)
typing_area.pack(pady=20)
start_button=Button(text="START",command=start_game)
start_button.pack()
restart_button=Button(text="Restart",command=start_game)
restart_button.pack()
# Result label
result_label = Label(window, text="", font=("Arial", 14))
result_label.pack(pady=20)
window.mainloop()