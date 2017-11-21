import tkinter as tk


window = tk.Tk()
window.title('WoW')
window.geometry('400x300')

#on_hit = False
# e = tk.Entry(window,show=None)
# e.pack()
def test():
    print('test')

t = tk.Text(window, height=5)
t.pack()

tk.Label(window, text='起始值：').place(x=10,y=100)
tk.Entry(window,show=None).place(x=60,y=95)

tk.Label(window, text='回數：').place(x=10,y=120)
tk.Entry(window,show=None).place(x=60,y=120)

tk.Label(window, text='倍數：').place(x=10,y=150)
tk.Entry(window,show=None).place(x=60,y=145)

b2 = tk.Button(window, text='測試', width=15, height=2, command=test)
b2.pack(side='left')

b = tk.Button(window, text='開網頁', width=15, height=2, command=test)
b.pack(side='left')

b3 = tk.Button(window, text='開始下注', width=15, height=2, command=test)
b3.pack(side='left')

window.mainloop()
