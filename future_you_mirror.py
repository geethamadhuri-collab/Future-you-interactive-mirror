import tkinter as tk
from tkinter import ttk

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Future You Interactive Mirror")
root.geometry("520x750")
root.configure(bg="#0f172a")

# ---------------- TITLE ----------------
title = tk.Label(root,
                 text="Future You Interactive Mirror",
                 font=("Segoe UI", 18, "bold"),
                 bg="#0f172a",
                 fg="#38bdf8")
title.pack(pady=15)

subtitle = tk.Label(root,
                    text="Analyze your habits. Shape your future.",
                    font=("Segoe UI", 10),
                    bg="#0f172a",
                    fg="#94a3b8")
subtitle.pack()

# ---------------- MAIN FRAME ----------------
frame = tk.Frame(root, bg="#1e293b")
frame.pack(pady=20, padx=20, fill="both", expand=True)

# ---------------- SLIDER FUNCTION ----------------
def styled_scale(parent, text):
    lbl = tk.Label(parent, text=text,
                   bg="#1e293b", fg="white",
                   font=("Segoe UI", 10))
    lbl.pack(anchor="w", pady=(10, 0))

    scale = tk.Scale(parent,
                     from_=0, to=10,
                     orient="horizontal",
                     bg="#1e293b",
                     fg="white",
                     highlightthickness=0,
                     troughcolor="#334155",
                     activebackground="#38bdf8")
    scale.pack(fill="x", pady=5)
    return scale

study_slider = styled_scale(frame, "Study Hours")
screen_slider = styled_scale(frame, "Screen Time")
sleep_slider = styled_scale(frame, "Sleep Hours")

# ---------------- CHECKBOXES ----------------
skill_var = tk.IntVar()
consistency_var = tk.IntVar()

style = ttk.Style()
style.configure("Custom.TCheckbutton",
                background="#1e293b",
                foreground="white")

check_frame = tk.Frame(frame, bg="#1e293b")
check_frame.pack(pady=15)

skill_check = ttk.Checkbutton(check_frame,
                              text=" Learning Skills",
                              variable=skill_var,
                              style="Custom.TCheckbutton")
skill_check.pack(side="left", padx=20)

consistency_check = ttk.Checkbutton(check_frame,
                                    text=" Consistency",
                                    variable=consistency_var,
                                    style="Custom.TCheckbutton")
consistency_check.pack(side="left", padx=20)

# ---------------- BUTTON ----------------
def calculate():
    study = study_slider.get()
    screen = screen_slider.get()
    sleep = sleep_slider.get()
    skill = skill_var.get()
    consistency = consistency_var.get()

    # IMPROVED LOGIC
    growth = (study * 6) + (consistency * 30)
    skill_score = (skill * 50) + (study * 4)
    burnout = (screen * 10) - (sleep * 6)

    # LIMIT VALUES
    growth = min(max(growth, 0), 100)
    skill_score = min(max(skill_score, 0), 100)
    burnout = min(max(burnout, 0), 100)

    # UPDATE BARS
    growth_bar['value'] = growth
    skill_bar['value'] = skill_score
    burnout_bar['value'] = burnout

    # MESSAGE
    if consistency and skill and study > 6:
        msg = "🚀 You are unstoppable. This version of you wins."
    elif growth > 70:
        msg = "🔥 Strong path. Keep pushing."
    elif growth > 40:
        msg = "⚡ Decent progress. Stay consistent."
    else:
        msg = "⚠️ You're underperforming. Fix habits NOW."

    result_label.config(text=msg)

btn = tk.Button(frame,
                text="Analyze Future",
                command=calculate,
                bg="#38bdf8",
                fg="black",
                font=("Segoe UI", 11, "bold"),
                relief="flat",
                padx=10, pady=6)
btn.pack(pady=10)

# ---------------- RESULT LABEL ----------------
result_label = tk.Label(frame,
                        text="",
                        bg="#1e293b",
                        fg="white",
                        font=("Segoe UI", 11),
                        wraplength=400)
result_label.pack(pady=10)

# ---------------- PROGRESS BAR STYLE ----------------
style.theme_use('default')

style.configure("green.Horizontal.TProgressbar",
                troughcolor="#334155",
                background="#22c55e",
                thickness=12)

# ---------------- BARS ----------------
def styled_bar(parent, text):
    lbl = tk.Label(parent, text=text,
                   bg="#1e293b",
                   fg="#94a3b8",
                   font=("Segoe UI", 9))
    lbl.pack(anchor="w", pady=(10, 0))

    bar = ttk.Progressbar(parent,
                          length=300,
                          maximum=100,
                          style="green.Horizontal.TProgressbar")
    bar.pack(pady=5)
    return bar

# spacing
tk.Label(frame, text="", bg="#1e293b").pack(pady=5)

growth_bar = styled_bar(frame, "Career Growth")
skill_bar = styled_bar(frame, "Skill Strength")
burnout_bar = styled_bar(frame, "Burnout Risk")

# ---------------- RUN ----------------
root.mainloop()