# imports 
from tkinter import * 
from tkinter import ttk
from scraper import scraper

class gui:

    def __init__(self, root):

        root.title("Lyric Scraper")

        # setting up mainframe
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # labels and fields
        artist_label = ttk.Label(mainframe, text="Artist: ")
        artist_label.grid(column=2, row=2, sticky=E)

        self.artist_entry = StringVar()
        artist_field = ttk.Entry(mainframe, width=40, textvariable=self.artist_entry)
        artist_field.grid(column=3, row=2, sticky=W)

        title_label = ttk.Label(mainframe,text="Title: ")
        title_label.grid(column=2, row=3, sticky=E)

        self.title_entry = StringVar()
        title_field = ttk.Entry(mainframe, width=40, textvariable=self.title_entry)
        title_field.grid(column=3, row=3, sticky=W)

        # search button 
        search_button = ttk.Button(mainframe, text="Search Lyrics", command=self.fetch_lyrics)
        search_button.grid(column=3, row=4, sticky=W)
        

        # album cover 

        # lyrics page
        self.lyrics_box = Text(mainframe, width=60, height=30)
        self.lyrics_box.insert('1.0', "when you search for lyrics, lyrics will show up here.")
        self.lyrics_box.grid(column=3, row=7)
        

        # padding for widgets
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)


    def fetch_lyrics(self):
       lyrics_result = scraper(self.artist_entry.get(), self.title_entry.get())
       self.lyrics_box.replace('1.0', 'end', lyrics_result)

root = Tk()
gui(root)
root.mainloop()


