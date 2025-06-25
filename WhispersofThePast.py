import tkinter as tk
from tkinter import messagebox, simpledialog

class WhispersOfThePast:
    def __init__(self, root):
        self.root = root
        self.root.title("🌅 Whispers of the Past")
        self.root.geometry("700x500")
        self.inventory = []
        self.memories = []

        self.story_label = tk.Message(root, text="", width=650, font=("Arial", 14), bg="linen")
        self.story_label.pack(pady=20)

        self.button_frame = tk.Frame(root, bg="linen")
        self.button_frame.pack()

        self.display_intro()

    def display_intro(self):
        self.set_story("You sit on your porch as the evening sun glows warmly.\nIt's time to reflect on your past.")
        self.update_buttons([
            ("🌻 Visit the Old Garden", self.garden_scene),
            ("📚 Walk to the Forgotten Library", self.library_scene),
            ("🌊 Reflect at the Lake", self.lake_scene),
            ("🧠 View Memories", self.show_memories),
            ("🚪 Exit Game", self.root.quit)
        ])

    def set_story(self, text):
        self.story_label.config(text=text)

    def update_buttons(self, actions):
        for widget in self.button_frame.winfo_children():
            widget.destroy()
        for label, action in actions:
            tk.Button(self.button_frame, text=label, font=("Arial", 12), width=40,
                      bg="#6c757d", fg="white", command=action).pack(pady=5)

    def garden_scene(self):
        self.set_story("You kneel among blooming marigolds in the old garden.")
        if "garden_puzzle1" not in self.inventory:
            answer = simpledialog.askstring("Garden Puzzle", "Which day comes twice in every week?").lower()
            if answer == "e":
                self.inventory.append("garden_puzzle1")
                self.memories.append("📷 Found a photo of your young self holding a sunflower.")
                messagebox.showinfo("Memory Unlocked", "You found a photo in the garden.")
            else:
                messagebox.showinfo("Try Again", "That's not the right answer.")
                return
        if "garden_puzzle2" not in self.inventory:
            answer = simpledialog.askstring("Garden Puzzle 2", "I have roots but no branches, grow but never bloom. What am I?").lower()
            if "family" in answer or "tree" in answer:
                self.inventory.append("garden_puzzle2")
                self.memories.append("🌳 You recalled your family tree, drawn long ago.")
                messagebox.showinfo("Memory Unlocked", "You remembered your family roots.")
            else:
                messagebox.showinfo("Try Again", "That's not it.")
                return
        else:
            messagebox.showinfo("Garden", "You’ve uncovered all the memories in this garden.")
        self.display_intro()

    def library_scene(self):
        self.set_story("The forgotten library smells of dust and ink.")
        if "library_puzzle1" not in self.inventory:
            answer = simpledialog.askstring("Library Riddle", "What can fill a room but takes up no space?").lower()
            if answer == "light":
                self.inventory.append("library_puzzle1")
                self.memories.append("📖 Found a book of poems you once wrote.")
                messagebox.showinfo("Memory Unlocked", "A journal lights up your past.")
            else:
                messagebox.showinfo("Try Again", "Not quite.")
                return
        if "library_puzzle2" not in self.inventory:
            answer = simpledialog.askstring("Library Riddle 2", "The more you take, the more you leave behind. What am I?").lower()
            if answer == "footsteps":
                self.inventory.append("library_puzzle2")
                self.memories.append("👣 You remembered the footsteps echoing in that old hall.")
                messagebox.showinfo("Memory Unlocked", "You recalled a distant walk.")
            else:
                messagebox.showinfo("Try Again", "Still dusty... try again later.")
                return
        else:
            messagebox.showinfo("Library", "Every shelf has shared its secret.")
        self.display_intro()

    def lake_scene(self):
        self.set_story("You sit by the still lake, reflections flickering in the water.")
        if "lake_puzzle1" not in self.inventory:
            answer = simpledialog.askstring("Lake Riddle", "I speak without a mouth and hear without ears. What am I?").lower()
            if answer == "echo":
                self.inventory.append("lake_puzzle1")
                self.memories.append("🌊 Remembered a quiet talk with a loved one by the lake.")
                messagebox.showinfo("Memory Unlocked", "The lake echoed your memories.")
            else:
                messagebox.showinfo("Try Again", "The lake remains silent.")
                return
        if "lake_puzzle2" not in self.inventory:
            answer = simpledialog.askstring("Lake Riddle 2", "What has to be broken before you can use it?").lower()
            if answer == "egg":
                self.inventory.append("lake_puzzle2")
                self.memories.append("🥚 Remembered learning to cook breakfast at the lakeside cabin.")
                messagebox.showinfo("Memory Unlocked", "You remembered a small but cherished moment.")
            else:
                messagebox.showinfo("Try Again", "The ripples fade…")
                return
        else:
            messagebox.showinfo("Lake", "You have found peace in every ripple.")
        self.display_intro()

    def show_memories(self):
        if self.memories:
            memory_text = "\n".join(self.memories)
            messagebox.showinfo("🧠 Your Memories", memory_text)
        else:
            messagebox.showinfo("🧠 Your Memories", "You haven’t uncovered any memories yet.")

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="linen")
    app = WhispersOfThePast(root)
    root.mainloop()