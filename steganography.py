from tkinter import *
from tkinter.filedialog import *
from PIL import ImageTk,Image
from stegano import exifHeader as stg
from tkinter import messagebox
  

class EDPD(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.pded = master        
        font = ['Courier', '13', 'normal']
        self.fontcmd = ['Consolas', '10', 'normal']
        self.sw = self.pded.winfo_screenwidth()      #### screen width
        self.sh = self.pded.winfo_screenheight()     #### screen height
        self.w = self.sw - (self.sw/2)
        self.w = (self.w - (self.sw/8))/2                #### calculation for window
        self.h = (self.sh - (self.w/2))/2                
        self.xpos =(self.sw/2) - (self.w/2)          #### calculation for centre
        self.ypos =(self.sh/2) - (self.h/2)
        self.pded.geometry('%dx%d+%d+%d' % (self.w, self.h, self.xpos, self.ypos))

        EncodeButton = Button(text="Encode",command = self.Encode)
        EncodeButton.place(relx=0.3,rely=0.4)

        DecodeButton = Button(text="Decode",command=self.Decode)
        DecodeButton.place(relx=0.6,rely=0.4)

        
        

    def Encode(self):
        self.pded.destroy()
        EncScreen = Tk()
        EncScreen.title("Encode- Antra")
        EncScreen.geometry('%dx%d+%d+%d' % (self.w, self.h, self.xpos, self.ypos))
        EncScreen.config(bg="yellow")
        label = Label(text="Confidential Message")
        label.place(relx=0.1,rely=0.2)
        self.entry=Entry()
        self.entry.place(relx=0.5,rely=0.2)
        label1 = Label(text="Name of the File")
        label1.place(relx=0.1,rely=0.3)
        self.SaveEntry = Entry()
        self.SaveEntry.place(relx=0.5,rely=0.3)
        self.SelectButton = Button(text="Select the file",command= self.OpenFile)
        self.SelectButton.place(relx=0.1,rely=0.4)
        self.EncodeButton=Button(text="Encode",command = self.Encoder)
        self.EncodeButton.place(relx=0.4,rely=0.5)
        

    def OpenFile(self):
        global FileOpen
        FileOpen=StringVar()
        FileOpen = askopenfilename(initialdir = "/Desktop" , title = "SelectFile",filetypes=(("jpeg files","*jpg"),("all files","*.*")))

        label2 = Label(text=FileOpen)
        label2.place(relx=0.3,rely=0.3)
 
    def Encoder(self):
        Response= messagebox.askyesno("PopUp","Do you want to encode the image")
        if Response == 1:
            stg.hide(FileOpen,self.SaveEntry.get()+"enc.jpg",self.entry.get())
            messagebox.showinfo("Pop Up","Successfully Encoded the image")
        else:
            messagebox.showwarning("Pop Up","Unsuccessful,please try again")
            
    def Decode(self):
        self.pded.destroy()
        DecScreen = Tk()
        DecScreen.title("Decode- Akshita")
        DecScreen.geometry('%dx%d+%d+%d' % (self.w, self.h, self.xpos, self.ypos))
        DecScreen.config(bg="pink")
        SelectButton = Button(text="Select the file",command= self.OpenFile)
        SelectButton.place(relx=0.1,rely=0.4)
        EncodeButton=Button(text="Decode",command= self.Decoder)
        EncodeButton.place(relx=0.4,rely=0.5)

    def OpenFile(self):
        global FileOpen
        FileOpen=StringVar()
        FileOpen = askopenfilename(initialdir="/Desktop",title="Select the File",filetypes=(("only jpeg files","*jpg"),("all type of files","*.*")))
        self.label2 = Label(text=FileOpen)
        self.label2.place(relx=0.3,rely=0.3)
        
    def Decoder(self):
        try:
            Message=stg.reveal(FileOpen)
            self.label2.config(text = Message)
        except:
            messagebox.showinfo("Pop Up","No message Found")
        
    

        
def main():
    root = Tk()
    root.title("Steganography")
    root.config(bg= "cyan")
    EDPD(root)
    root.mainloop()

if __name__ == "__main__":
    main()
