import tkinter as tk

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Future You Simulator")
root.geometry("500x600")
root.configure(bg="#0f0f1a")

# ---------------- TITLE ----------------
title = tk.Label(root, text="FUTURE YOU SIMULATOR",
                 font=("Arial", 20, "bold"),
                 bg="#0f0f1a", fg="#00f5ff")
title.pack(pady=20)

# ---------------- SLIDERS ----------------
study = tk.Scale(root, from_=0, to=12, orient="horizontal",
                 label="Study Hours",
                 bg="#0f0f1a", fg="white", highlightthickness=0)
study.pack(pady=10)

screen = tk.Scale(root, from_=0, to=10, orient="horizontal",
                  label="Screen Time",
                  bg="#0f0f1a", fg="white", highlightthickness=0)
screen.pack(pady=10)

# ---------------- CHECKBOX ----------------
consistency_var = tk.IntVar()

consistency = tk.Checkbutton(root, text="Consistency",
                             variable=consistency_var,
                             bg="#0f0f1a", fg="white",
                             activebackground="#0f0f1a")
consistency.pack(pady=10)

# ---------------- RESULT TEXT ----------------
result = tk.Label(root, text="",
                  font=("Arial", 16, "bold"),
                  wraplength=400,
                  bg="#0f0f1a", fg="white")
result.pack(pady=40)


# ---------------- LOGIC ----------------
def reveal_future():
    result.config(text="Analyzing your future...", fg="yellow")

    root.after(1500, show_result)  # delay for dramatic effect


def show_result():
    s = study.get()
    sc = screen.get()
    c = consistency_var.get()

    # --------- 3 DESTINIES ----------
    if s > 7 and c == 1 and sc < 5:
        root.configure(bg="#0a0a23")
        result.config(
            text="🌟 THE LEGEND VERSION 🌟\n\n"
                 "You didn’t just succeed...\n"
                 "You became unstoppable.\n\n"
                 "People study your journey now.",
            fg="#00f5ff", bg="#0a0a23"
        )

    elif s > 4:
        root.configure(bg="#1a1a1a")
        result.config(
            text="⚖️ THE AVERAGE LOOP ⚖️\n\n"
                 "You survived...\n"
                 "but never reached your true potential.\n\n"
                 "You always wondered... what if?",
            fg="white", bg="#1a1a1a"
        )

    else:
        root.configure(bg="#2a0000")
        result.config(
            text="⚠️ THE REGRET VERSION ⚠️\n\n"
                 "You had time...\n"
                 "but you chose comfort over growth.\n\n"
                 "Now, you wish you could go back.",
            fg="#ff4d4d", bg="#2a0000"
        )


# ---------------- BUTTON ----------------
btn = tk.Button(root, text="⚡ Reveal My Future ⚡",
                command=reveal_future,
                font=("Arial", 14, "bold"),
                bg="#00adb5", fg="black",
                padx=10, pady=5)
btn.pack(pady=20)

# ---------------- RUN ----------------
root.mainloop()