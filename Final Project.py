from tkinter import *

expression = "" 


#Calculator engine
def press(num): 
	
	global expression 

	expression = expression + str(num) 

	equation.set(expression) 



def equalpress(): 
	try: 

		global expression 

		total = str(eval(expression)) 

		equation.set(total) 

		expression = "" 

	except: 

		equation.set(" error ") 
		expression = "" 


def clear(): 
	global expression 
	expression = "" 
	equation.set("") 



if __name__ == "__main__": 

	#Resulation and app
	gui = Tk() 

	
	gui.configure(background="black") 

	
	gui.title("Calculator") 

	 
	gui.geometry("625x435")
	gui.resizable(False,False)

	#textbox and size
	equation = StringVar() 

	expression_field = Entry(font=("Arial", 20), textvariable=equation) 

	expression_field.grid(columnspan=4, ipadx=160, ipady=60)


        #all numbers,letters and buttons
	button1 = Button(gui, text=' 1 ', fg='white', bg='black', 
					command=lambda: press(1), height=3, width=21) 
	button1.grid(row=2, column=0) 

	button2 = Button(gui, text=' 2 ', fg='white', bg='black', 
					command=lambda: press(2), height=3, width=21) 
	button2.grid(row=2, column=1) 

	button3 = Button(gui, text=' 3 ', fg='white', bg='black', 
					command=lambda: press(3), height=3, width=21) 
	button3.grid(row=2, column=2) 

	button4 = Button(gui, text=' 4 ', fg='white', bg='black', 
					command=lambda: press(4), height=3, width=21) 
	button4.grid(row=3, column=0) 

	button5 = Button(gui, text=' 5 ', fg='white', bg='black', 
					command=lambda: press(5), height=3, width=21) 
	button5.grid(row=3, column=1) 

	button6 = Button(gui, text=' 6 ', fg='white', bg='black', 
					command=lambda: press(6), height=3, width=21) 
	button6.grid(row=3, column=2) 

	button7 = Button(gui, text=' 7 ', fg='white', bg='black', 
					command=lambda: press(7), height=3, width=21) 
	button7.grid(row=4, column=0) 

	button8 = Button(gui, text=' 8 ', fg='white', bg='black', 
					command=lambda: press(8), height=3, width=21) 
	button8.grid(row=4, column=1) 

	button9 = Button(gui, text=' 9 ', fg='white', bg='black', 
					command=lambda: press(9), height=3, width=21) 
	button9.grid(row=4, column=2) 

	button0 = Button(gui, text=' 0 ', fg='white', bg='black', 
					command=lambda: press(0), height=3, width=21) 
	button0.grid(row=5, column=0) 

	plus = Button(gui, text=' + ', fg='white', bg='black', 
				command=lambda: press("+"), height=3, width=21) 
	plus.grid(row=2, column=3) 

	minus = Button(gui, text=' - ', fg='white', bg='black', 
				command=lambda: press("-"), height=3, width=21) 
	minus.grid(row=3, column=3) 

	multiply = Button(gui, text=' x ', fg='white', bg='black', 
					command=lambda: press("*"), height=3, width=21) 
	multiply.grid(row=4, column=3) 

	divide = Button(gui, text=' / ', fg='white', bg='black', 
					command=lambda: press("/"), height=3, width=21) 
	divide.grid(row=5, column=3) 

	equal = Button(gui, text=' = ', fg='white', bg='green', 
				command=equalpress, height=3, width=21) 
	equal.grid(row=5, column=2) 

	clear = Button(gui, text='Clear', fg='white', bg='black', 
				command=clear, height=3, width=21) 
	clear.grid(row=5, column='1') 

	Decimal= Button(gui, text='.', fg='white', bg='black', 
					command=lambda: press('.'), height=3, width=21) 
	Decimal.grid(row=6, column=0) 
	
	gui.mainloop() 

