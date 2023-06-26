from tkinter import *
from math import sqrt, factorial

root = Tk()

class Calculator:
    def __init__(self, master):
        self.master = master
        self.memory = 0
        self.total = 0
        self.current = ""
        self.new_num = True
        self.operator = 0
        self.last_key = None
        self.last_num = None

        self.entry = Entry(master, width=15, font=('Helvetica', 34), bg='#333333', fg='#D3D3D3', insertbackground='white', justify='right')
        self.entry.grid(row=0, column=0, columnspan=6, pady=24, padx=19)

        buttons = [
            "MC", "M+", "M-", "MR", "AC",
            "\u221A", "7", "8", "9", "/",
            "!", "4", "5", "6", "*",
            "+/-", "1", "2", "3", "-",
            "CE", ".", "0", "=", "+"
        ]

        row = 1
        col = 0
        
        for button in buttons: 
            button_frame = Frame(master, bg='#0d0d0d')
            button_frame.grid(row=row, column=col)
            Button(button_frame, text=button, width=5, height=2, font=('Helvetica', 19), bg='#0d0d0d', fg='#D3D3D3', command=lambda button=button: self.click(button)).pack()
            col += 1
            if col > 4:
                col = 0
                row+=1
            
    def click(self, key):
        if key in ['MC', 'M+', 'M-', 'MR']:
            self.memory_operations(key)
        elif key in ['0', '1', '2', '3', '4', '5' ,'6', '7', '8', '9']:
            self.num(key)
        elif key in ['/','*','+']:
            self.calc(key)
        elif key == '-':
            current_entry = self.entry.get()
            if current_entry == "":               
                self.entry.insert(0, '-')
            elif current_entry == '-':
                pass
            else:
                self.calc(key)
        elif key == '=':
            self.equals()
        elif key == '\u221A':
            self.sqrt()
        elif key == '!':
            self.factorial()
        elif key == 'CE':
            self.clear_entry()
        elif key == 'AC':
            self.all_clear()
        elif key == '+/-':
            self.sign_change()
        elif key == '.':
            self.point()

    def memory_operations(self, key):
        if key == 'MC':
            self.memory = 0
        elif key == 'M+':
            self.memory += float(self.entry.get())
        elif key == 'M-':
            self.memory -= float(self.entry.get())
        elif key == 'MR':
            self.entry.delete(0, END)
            if self.memory == int(self.memory):
                self.memory = int(self.memory)
            self.entry.insert(0, self.memory)

    def num(self, key):
        current_entry = self.entry.get()
        if self.new_num and current_entry != "-":
            self.entry.delete(0, END)
            self.new_num = False
            self.last_key = None
            self.last_num = None
        self.entry.insert(END, key)
        
    def calc(self, key):
        if self.current and self.operator:
            self.equals()
        self.current = float(self.entry.get())
        self.operator = key
        self.new_num = True

    def equals(self):
        num = float(self.entry.get())
        if self.operator:
            try:
                if self.operator == '+':
                    self.total = round(self.current + num, 10)
                elif self.operator == '-':
                    self.total = round(self.current - num, 10)
                elif self.operator == '*':
                    self.total = round(self.current * num, 10)
                elif self.operator == '/': 
                    self.total = round(self.current / num, 10)
            except ZeroDivisionError:
                self.entry.delete(0, END)
                self.entry.insert(0, "Error")
                return
            self.last_key = self.operator
            self.last_num = num
            self.current = self.total
        else:  
            if self.last_key and self.last_num is not None:
                if self.last_key == '+':
                    self.total = round(self.current + self.last_num, 10)
                elif self.last_key == '-':
                    self.total = round(self.current - self.last_num, 10)
                elif self.last_key == '*':
                    self.total = round(self.current * self.last_num, 10)
                elif self.last_key == '/':
                    if self.last_num != 0:
                        self.total = round(self.current / self.last_num, 10)
                    else:
                        self.entry.delete(0, END)
                        self.entry.insert(0, "Error")
                        return
                self.current = self.total
            else:
                self.total = num  
        if self.total == int(self.total):
                self.total = int(self.total)
        self.entry.delete(0, END)
        self.entry.insert(0, self.total)
        self.new_num = True
        self.operator = None

    def sqrt(self):
        if self.current and self.operator:
            self.equals()
        num = sqrt(float(self.entry.get()))
        if num.is_integer():
            num = int(num)
        self.entry.delete(0, END)
        self.entry.insert(END, num)
        self.new_num = True

    def factorial(self):
        if self.current and self.operator:
            self.equals()
        try:
            num = int(self.entry.get())
            if num < 0:
                self.entry.delete(0, END)
                self.entry.insert(0, "Error")
            else:        
                self.entry.delete(0, END)
                self.entry.insert(0, factorial(num))
        except ValueError:
            self.entry.delete(0, END)
            self.entry.insert(0, "Error")
        self.new_num=True

    def clear_entry(self): 
        self.entry.delete(0, END)
        self.last_key = None
        self.last_num = None

    def all_clear(self):
        self.clear_entry()
        self.current = 0

    def sign_change(self):
        num = float(self.entry.get())
        self.entry.delete(0, END)
        num = -num
        if num == int(num):
            num = int(num)
        self.entry.insert(0, num)

    def point(self):
        if self.new_num:
            self.entry.delete(0, END)
            self.new_num = False
            self.last_key = None
            self.last_num = None
        current_number = self.entry.get()
        if "." not in current_number:
            if current_number =='':
                self.entry.insert(END, '0.')
            else:
                self.entry.insert(END, '.')

root.configure(bg='#0d0d0d')
root.title("GW Calc")
app = Calculator(root)
root.mainloop()

