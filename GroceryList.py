#Libaries importred
import ttkbootstrap as tb

#Window Properties
root = tb.Window(themename='darkly')
root.geometry('250x500')
root.title('Grocery List')

def new_Label(event=None):
    newLabel = tb.Label(root)
    newLabel.pack()
    newLabel.config(text=myInput.get())  
    myInput.delete(0, 'end') # 0 being start of the given string, 'end' being the end of the given string

#Window Addons
mylabel = tb.Label(text=('Grocery List'))
myInput = tb.Entry(root)
mySubmit = tb.Button(root, text='Submit!', command=new_Label)
new_Label()

#Window Hotkeys
root.bind('<Return>', new_Label)

#Pack Items within List
packedItems = [mylabel, myInput, mySubmit]
for items in packedItems:
    items.pack()


#Window Running Loop
root.mainloop()