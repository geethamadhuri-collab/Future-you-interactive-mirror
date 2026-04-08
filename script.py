import tkinter as tk
from tkinter import ttk

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Future You Interactive Mirror")
root.geometry("500x650")

# ---------------- CANVAS (GRADIENT) ----------------
canvas = tk.Canvas(root, width=500, height=650)
canvas.pack(fill="both", expand=True)

def create_gradient(canvas, width, height):
    for i in range(height):
        r = int(30 + (i / height) * 50)
        g = int(30 + (i / height) * 50)
        b = int(60 + (i / height) * 120)
        color = f"#{r:02x}{g:02x}{b:02x}"
        canvas.create_line(0, i, width, i, fill=color)

create_gradient(canvas, 500, 650)

# ---------------- TITLE ----------------
canvas.create_text(250, 30, text="Future You Interactive Mirror",
                   fill="white", font=("Arial", 18, "bold"))

# ---------------- SLIDERS ----------------
study_slider = tk.Scale(root, from_=0, to=12, orient="horizontal",
                        label="Study Hours", bg="#2e2e3e", fg="white")
canvas.create_window(250, 100, window=study_slider)

screen_slider = tk.Scale(root, from_=0, to=10, orient="horizontal",
                         label="Screen Time", bg="#2e2e3e", fg="white")
canvas.create_window(250, 170, window=screen_slider)

sleep_slider = tk.Scale(root, from_=0, to=10, orient="horizontal",
                        label="Sleep Hours", bg="#2e2e3e", fg="white")
canvas.create_window(250, 240, window=sleep_slider)

# ---------------- CHECKBOXES ----------------
skill_var = tk.IntVar()
consistency_var = tk.IntVar()

skill_check = tk.Checkbutton(root, text="Learning New Skills",
                             variable=skill_var, bg="#2e2e3e", fg="white")
canvas.create_window(150, 300, window=skill_check)

consistency_check = tk.Checkbutton(root, text="Consistency",
                                   variable=consistency_var, bg="#2e2e3e", fg="white")
canvas.create_window(350, 300, window=consistency_check)

# ---------------- DROPDOWN ----------------
options = ["1 Year", "3 Years", "5 Years"]
selected = tk.StringVar()
selected.set(options[0])

dropdown = tk.OptionMenu(root, selected, *options)
canvas.create_window(250, 350, window=dropdown)

# ---------------- OUTPUT LABEL ----------------
result_label = tk.Label(root, text="", bg="#2e2e3e", fg="white", wraplength=400)
canvas.create_window(250, 420, window=result_label)

# ---------------- PROGRESS BARS ----------------
growth_bar = ttk.Progressbar(root, length=200, maximum=100)
canvas.create_window(250, 470, window=growth_bar)

skill_bar = ttk.Progressbar(root, length=200, maximum=100)
canvas.create_window(250, 510, window=skill_bar)

burnout_bar = ttk.Progressbar(root, length=200, maximum=100)
canvas.create_window(250, 550, window=burnout_bar)

# ---------------- LOGIC FUNCTION ----------------
def calculate():
    study = study_slider.get()
    screen = screen_slider.get()
    sleep = sleep_slider.get()
    skill = skill_var.get()
    consistency = consistency_var.get()

    growth = study * 8 + consistency * 20
    skill_score = skill * 40 + study * 5
    burnout = screen * 10 - sleep * 5

    # limit values
    growth = min(growth, 100)
    skill_score = min(skill_score, 100)
    burnout = max(0, min(burnout, 100))

    # update bars
    growth_bar['value'] = growth
    skill_bar['value'] = skill_score
    burnout_bar['value'] = burnout

    # message
    if growth > 70:
        msg = "🔥 Your future is bright! Keep going!"
    elif growth > 40:
        msg = "⚡ You are doing okay, but improve consistency."
    else:
        msg = "⚠️ You need to work harder for a better future."

    result_label.config(text=msg)

# ---------------- BUTTON ----------------
btn = tk.Button(root, text="Meet Future You", command=calculate,
                bg="#00adb5", fg="white", font=("Arial", 12, "bold"))
canvas.create_window(250, 390, window=btn)

# ---------------- RUN ----------------
root.mainloop()