import random
import json
import tkinter as tk

quotes = [
    {"text": "Stay hungry, stay foolish.", "author": "Steve Jobs", "topic": "Motivation"},
    {"text": "To be or not to be.", "author": "William Shakespeare", "topic": "Philosophy"},
    {"text": "Knowledge is power.", "author": "Francis Bacon", "topic": "Education"}
]

history = []

def load_history():
    global history
    try:
        with open("history.json", "r", encoding="utf-8") as f:
            history = json.load(f)
    except:
        history = []

def save_history():
    with open("history.json", "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=4)

def generate_quote():
    quote = random.choice(quotes)
    text = f'{quote["text"]}\n— {quote["author"]} ({quote["topic"]})'
    label.config(text=text)
    history.append(quote)
    listbox.insert(tk.END, text)
    save_history()

def filter_quotes():
    keyword = entry.get().lower()
    listbox.delete(0, tk.END)
    for q in history:
        if keyword in q["author"].lower() or keyword in q["topic"].lower():
            text = f'{q["text"]} — {q["author"]} ({q["topic"]})'
            listbox.insert(tk.END, text)

root = tk.Tk()
root.title("Random Quote Generator")

label = tk.Label(root, text="Нажми кнопку", wraplength=300)
label.pack(pady=10)

btn = tk.Button(root, text="Сгенерировать цитату", command=generate_quote)
btn.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

filter_btn = tk.Button(root, text="Фильтр (автор/тема)", command=filter_quotes)
filter_btn.pack(pady=5)

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

load_history()

root.mainloop()