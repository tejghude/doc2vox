from tkinter import*
from tkinter import ttk
from ttkthemes import ThemedStyle
import pyttsx3
import PyPDF2
from tkinter import filedialog

root = Tk()
root.title("AudioBook")
root.geometry("530x490")
main_frame=Frame(root)
main_frame.pack(fill=BOTH,expand=1)
mc=Canvas(main_frame)
mc.pack(side=LEFT,fill=BOTH,expand=1)
scrollbar =ttk.Scrollbar(main_frame,orient=VERTICAL,command=mc.yview)
scrollbar. pack(side=RIGHT, fill=Y)
mc.configure(yscrollcommand=scrollbar.set)
mc.bind('<Configure>',lambda e : mc.configure(scrollregio=mc.bbox("all")))
sframe=Frame(mc)
mc.create_window((0,0),window=sframe,anchor="nw")


style = ThemedStyle(root)
style.set_theme("plastik")


def display(text):
    my_text.insert(1.0, text)

global spd
spd=140

my_text = Text(sframe, height=15, width=65)
my_text.pack(pady=5)
my_text.config(state=NORMAL)



def clear (): 
     my_text.delete(1.0,END)  

def changepg():
    clear()
    pg=int(page_no.get('1.0', END))
    getpg(pg) 

l2=ttk.Label(sframe, text='Page number:', justify=LEFT)
l2.pack()
page_no =Text(sframe, height=1, width=10 )
page_no.pack(pady=10)

my_button1 =ttk.Button(sframe,text="Change Page", command=changepg,width = 30)
my_button1.pack(pady=5)

def getpg(pgno):
    page = pdf_file.getPage(pgno)
    global text
    text = page.extractText()   
    display(text)

def open_pdf():
    global open_file
    open_file = filedialog.askopenfilename(
        initialdir="C:/Users/Dell/Desktop/study/",
        title="Open PDF File",
        filetypes=(
            ("PDF Files", "*.pdf"),
            ("All Files", "*.*")))

    if open_file:
        global pdf_file
        pdf_file = PyPDF2.PdfFileReader(open_file ,"rb")
        global pg
        pg=0
        getpg(0)    
        
def mp():
    global spd
    spd=int(speed.get('1.0', END))
    engine =pyttsx3.init()
    engine.setProperty('rate',spd)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.save_to_file(text, 'speech.mp3')
    engine.say(text)
    engine.runAndWait()

my_button = ttk.Button(sframe,text="Play", command=mp,width = 30)
my_button.pack(pady=5)
l1 =ttk.Label(sframe, text='Speed :')
l1.pack()
speed =Text(sframe, height=1, width=10  )
speed.pack(pady=10)

my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open PDF", command=open_pdf)
file_menu.add_command(label="Close PDF", command=clear)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

root.mainloop()
