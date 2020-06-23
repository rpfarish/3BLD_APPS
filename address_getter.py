import tkinter as tk


def remove_file(name):
    import os
    os.remove(name)


def return_address(address="index.txt"):
    f = open("sys_admin_X6hW%rD!pYM9h7%.txt", "w")

    # check if there is a sys_data file and if not create one
    # or a new file and then delete it ?!
    root = tk.Tk()
    if address != "index.txt":
        f.write(address)
        return 1
    canvas1 = tk.Canvas(root, width=400, height=300, relief='raised')
    canvas1.pack()

    label1 = tk.Label(root, text='Open Comm File')
    label1.config(font=('helvetica', 14))
    canvas1.create_window(200, 25, window=label1)

    label2 = tk.Label(root, text='Type the file Address')
    label2.config(font=('helvetica', 10))
    canvas1.create_window(200, 100, window=label2)

    entry1 = tk.Entry(root)
    entry1.insert(0, str(address))
    canvas1.create_window(200, 140, window=entry1)

    def get_address():
        x1 = entry1.get()
        f.write(x1)
        label3 = tk.Label(root, text=f'Opening {x1}... ', font=('helvetica', 10))
        canvas1.create_window(200, 210, window=label3)

        try:
            cool = open(x1, "r")
            cool.readline()
            if not cool.readable():
                raise FileNotFoundError
            if cool.readable():
                label4 = tk.Label(root, text='    Please close this window to continue.',
                                  font=('helvetica', 10, 'bold'))
                canvas1.create_window(200, 230, window=label4)

        except FileNotFoundError:
            print("ok")
            label4 = tk.Label(root, text='Please enter a valid file address.', font=('helvetica', 10, 'bold'),
                              fg=("red"))
            canvas1.create_window(200, 230, window=label4)

    button1 = tk.Button(text='Open', command=get_address, bg='brown', fg='white',
                        font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 180, window=button1)

    def get_edges():
        pass

    button2 = tk.Button(text='Edges', command=get_edges, bg='aqua', fg='white',
                        font=('helvetica', 9, 'bold'))
    canvas1.create_window(100, 180, window=button2)

    root.mainloop()



if __name__ == "__main__":
    return_address()
    import time

    # time.sleep(5)
    remove_file("sys_admin_X6hW%rD!pYM9h7%.txt")
