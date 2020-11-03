from tkinter import * 
from tkinter.ttk import *
from tkinter import messagebox
  
root = Tk()
root.geometry("900x900")

def helloCallBack():
   messagebox.showinfo( "alert", "you have been verified")



def ExitApplication():
    MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
    else:
        messagebox.showinfo('Return','You will now return to the application screen')




def ExitApplication1():
    MsgBox1 = messagebox.showerror('alert','you are not verified ',icon = 'warning')
    if MsgBox1 == 'ok':
       root.destroy()
   
       
           
  
Label(root, text = 'select any image without vehicals', font =( 
  'Verdana', 20)).pack(side = TOP, pady = 10) 
   
photo1= PhotoImage(file ="E:\\image based captcha\\resize-1604403443322666743building2.png")    
button1=Button(root, text = 'Click Me !', image = photo1,command=helloCallBack)
button1.place(x=25, y=50)

photo2= PhotoImage(file ="E:\\image based captcha\\road4.png")    
button2=Button(root, text = 'Click Me !', image = photo2,command=helloCallBack)
button2.place(x=265, y=50)


photo3= PhotoImage(file ="E:\\image based captcha\\resize-16044036431804167051road2.png")    
button3=Button(root, text = 'Click Me !', image = photo3,command=helloCallBack)
button3.place(x=505, y=50)

photo4= PhotoImage(file ="E:\\image based captcha\\resize-16044037431406635240road3.png")    
button4=Button(root, text = 'Click Me !', image = photo4,command=ExitApplication1)
button4.place(x=25, y=290)

photo5= PhotoImage(file ="E:\\image based captcha\\resize-1604403880741365805road5.png")    
button5=Button(root, text = 'Click Me !', image = photo5,command=ExitApplication1)
button5.place(x=265, y=290)    

photo6= PhotoImage(file ="E:\\image based captcha\\resize-16044039561391615741road6.png") 
button6=Button(root, text = 'Click Me !', image = photo6,command=helloCallBack)
button6.place(x=505, y=290)


photo7= PhotoImage(file ="E:\\image based captcha\\resize-1604404169248426620road7.png")    
button7=Button(root, text = 'Click Me !', image = photo7,command=ExitApplication1)
button7.place(x=25, y=530)


photo8= PhotoImage(file ="E:\\image based captcha\\resize-16044042151321610005road8.png")    
button8=Button(root, text = 'Click Me !', image = photo8,command=ExitApplication1)
button8.place(x=265, y=530)

photo9= PhotoImage(file ="E:\\image based captcha\\resize-16044042611144809408work.png")    
button9=Button(root, text = 'Click Me !', image = photo9,command=ExitApplication1)
button9.place(x=505, y=530)

button10=Button(root, text = 'close',command = ExitApplication)
button10.place(x=845, y=600)






  
root.mainloop() 

  

