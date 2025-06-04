import tkinter as tk
from Corona_ChatBot import predict_class, get_response  # or 'chatbot' based on your filename

def send():
    msg = entry_box.get("1.0", 'end-1c').strip()
    entry_box.delete("0.0", tk.END)

    if msg != '':
        chat_log.config(state=tk.NORMAL)
        chat_log.insert(tk.END, "You: " + msg + '\n\n')
        response = get_response(predict_class(msg))
        chat_log.insert(tk.END, "Bot: " + response + '\n\n')
        chat_log.config(state=tk.DISABLED)
        chat_log.yview(tk.END)

# Create GUI
base = tk.Tk()
base.title("Corona ChatBot")
base.geometry("400x500")
base.resizable(width=False, height=False)

chat_log = tk.Text(base, bd=0, bg="white", height="8", width="50", font="Arial", wrap=tk.WORD)
chat_log.config(state=tk.DISABLED)

scrollbar = tk.Scrollbar(base, command=chat_log.yview, cursor="heart")
chat_log['yscrollcommand'] = scrollbar.set

entry_box = tk.Text(base, bd=0, bg="white", width="29", height="5", font="Arial")

send_button = tk.Button(base, text="Send", width="12", height=2, bd=0, bg="#32de97", activebackground="#3c9d9b", fg='white', command=send)

scrollbar.place(x=376, y=6, height=386)
chat_log.place(x=6, y=6, height=386, width=370)
entry_box.place(x=6, y=401, height=90, width=265)
send_button.place(x=275, y=401, height=90)

base.mainloop()


def chat():
    msg = user_input.get()
    chat_log.insert(tk.END, "You: " + msg + "\n")
    user_input.delete(0, tk.END)

    if msg.lower() in ["quit", "exit"]:
        chat_log.insert(tk.END, "Bot: Goodbye! Stay safe.\n")
        return

    tag = predict_class(msg)
    reply = get_response(tag)
    chat_log.insert(tk.END, "Bot: " + reply + "\n")

app = tk.Tk()
app.title("Corona ChatBot")

chat_log = tk.Text(app, height=20, width=60)
chat_log.pack()

user_input = tk.Entry(app, width=50)
user_input.pack(side=tk.LEFT, padx=(10, 0))

send_btn = tk.Button(app, text="Send", command=chat)
send_btn.pack(side=tk.LEFT)

app.mainloop()
