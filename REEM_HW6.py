# R12541218 ZHANG ZHIYANG 
# Source code available at github.com/KanzakiMoe

'''
This program will roughly simulate the concentration of four algae groups in a lake dynamically,
there will be low nitrogen and phosphorus input, and 20% loss due to other animals predation.
'''

# import GUI kit
from tkinter import *

# Basic model setting
def simulation():
    try:
        month = int(inp.get())
    except:
        print("invalid input")
    # initial setting
    diatom = 0
    green = 0
    bluegreen = 0
    crypto = 0
    nitrogen = 1000
    phosphorus = 100
    for i in range (0,month):
        # when nitrogen is high and phosphorus is high as well
        if nitrogen >= 100 and phosphorus >= 10:
            diatom += 2
            green += 1
            crypto += 1
            nitrogen -= 100
            phosphorus -= 50
        else:
            # when nitrogen is high and phosphorus is low
            if nitrogen >= 100 and phosphorus <= 10:
                green +=  1
                nitrogen -= 50
                
            # when nitrogen is low and phosphorus is high
            if nitrogen <= 100 and phosphorus >= 10:
                bluegreen += 1
                phosphorus -= 10
        
        # nitrogen and phosphorus source input every month
        nitrogen += 60
        phosphorus += 15
        
        # all algae will be eaten by 20% every month
        diatom = diatom * 0.2
        green = green * 0.2
        bluegreen = bluegreen * 0.2
        crypto = crypto * 0.2
    # output
    try:
        txt.delete("1.0",END)
    except:
        1
    txt.insert(END,"Result: \n")
    txt.insert(END,"green algae: "+str(green)[:4]+"\n")
    txt.insert(END,"bluegreen algae: "+str(bluegreen)[:4]+"\n")
    txt.insert(END,"diatom: "+str(diatom)[:4]+"\n")
    txt.insert(END,"cryptomonad: "+str(crypto)[:4]+"\n\n")
            

# window code
root = Tk()   
root.title("REEM HW6")       
root.geometry("300x200")           
label1=Label(root, text="How many months you want to simulation: ")
calculate_button=Button(root, text="press to simulate", command=simulation)
label1.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.1)
inp = Entry(root)
inp.place(relx=0.35, rely=0.2, relwidth=0.3, relheight=0.1)
txt = Text(root)
txt.place(rely=0.6, relheight=0.4)
label1.pack()
inp.pack()
calculate_button.pack()
root.mainloop()    