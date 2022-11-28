from tkinter import *
import main
root=Tk()
root.title(" quizzer ")
root.geometry("1000x1000")
main_frame=Frame(root,width=1000,height=400,bg="black")
main_frame.pack(fill="both",expand=1)
l1=Label(main_frame,text="Computer Vision Quiz Through Hand Gestures Movements",bg="black",fg="white",font=("time new roman",20,"bold"))
l1.grid(row=0,column=0,padx=100,pady=100)
e=Entry(main_frame,width=90)
e.grid(row=1,column=0,padx=90)

def fun():
    entry=e.get()
    main.fun(entry)

b=Button(main_frame,text=" START QUIZ ",command=fun,width=15,bg="green",fg="white",font=("time new roman",20,"bold"))
b.grid(row=2,padx=90,pady=75)


b=Button(main_frame,text=" EXIT ",command=root.quit,width=15,bg="green",fg="white",font=("time new roman",20,"bold"))
b.grid(row=3,padx=90)

root.mainloop()