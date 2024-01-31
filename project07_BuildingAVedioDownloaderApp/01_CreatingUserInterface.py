from tkinter import *
root = Tk()
root.title('Video Downloader')
canvas = Canvas(root,width=400,height=300)
canvas.pack()

#app label
app_label = Label(root,text="Video Downloader",fg='blue',font=('Arial',30))
canvas.create_window(200,20,window=app_label)

#entry to accept video URL
url_label = Label(root,text="Enter video URL")
url_entry = Entry(root)
canvas.create_window(200,80,window=url_label)
canvas.create_window(200,100,window=url_entry)

root.mainloop()