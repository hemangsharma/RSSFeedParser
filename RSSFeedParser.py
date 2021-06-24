import feedparser
import tkinter as tk
import tkinter.scrolledtext as sb_text
from tkinter import *

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    rssfeedsLabel = Label(root, text="RSS FEED URL : ", bg="#d5d9e0")
    rssfeedsLabel.grid(row=0, column=0, padx=10, pady=5)

    rssfeedsEntry = Entry(root, width=39, bg='white', textvariable=feedentryurl)
    rssfeedsEntry.grid(row=0, column=1, padx=10, pady=5)

    addButton = Button(root, text="ADD FEED", command=addRssFeedEntry)
    addButton.grid(row=2, column=0, padx=10, pady=5, columnspan=2)

    rssfeedsListLabel = Label(root, text="RSS FEED LIST", bg="#d5d9e0")
    rssfeedsListLabel.grid(row=3, column=0, padx=10, pady=5)

    root.rssfeedsListBox = Listbox(root, width=55, height=19, bg='white')
    root.rssfeedsListBox.grid(row=4, column=0, rowspan=12, columnspan=3, padx=10, pady=5)
    # Binding onRssFeedSelect() event to the ListBox Widget
    root.rssfeedsListBox.bind('<<ListboxSelect>>', onRssFeedSelect)

    findButton = Button(root, text="FIND DETAILS", command=findRssFeedDetails)
    findButton.grid(row=17, column=0, padx=10, pady=15, columnspan=2)

    selectedFeedLabel = Label(root, text="SELECTED FEED : ", bg="#d5d9e0")
    selectedFeedLabel.grid(row=0, column=3, padx=10, pady=5)
    root.selectedFeedEntry = Entry(root, width=38, bg='white', textvariable=selectedfeed)
    root.selectedFeedEntry.grid(row=0, column=4, padx=10, pady=5)

    root.rssfeedsDetails = sb_text.ScrolledText(root, width=47, height=23, bg='white',
                                                font = "Calibri 16", wrap="word")
    root.rssfeedsDetails.grid(row=1, column=3, rowspan=17, columnspan=3, padx=10, pady=5)
    # Making the Text Widget uneditable by setting state parameter of config() to DISABLED
    root.rssfeedsDetails.config(state=DISABLED)

# Defining onRssFeedSelect() to display the ListBox Cursor Selection in the Entry widget
def onRssFeedSelect(evt):
    # Fetching the ListBox cursor selection
    rssfeed = root.rssfeedsListBox.get(root.rssfeedsListBox.curselection())
    # Displaying the selected text from ListBox in the widget using selectedfeed variable
    selectedfeed.set(rssfeed)

# Defining addRssFeedEntry() function to fetch user-input text and add it to the ListBox
def addRssFeedEntry():
    # Fetching the user-input text from the widget using get() of the tkinter variable
    rssFeedUrl = feedentryurl.get()
    # Adding the user-input text to the ListBox method using the insert() method
    root.rssfeedsListBox.insert("end", rssFeedUrl)

# Defining the findRssFeedDetails() to fetch the RSS Feed from the user-input Feed URL
def findRssFeedDetails():
    # Fetching the user-selected URL from ListBox displayed in Entry Widget using get()
    userSelectedFeed = selectedfeed.get()
    # Parsing the feed from the RSS Feed URL using the parse() method of feedparser URL
    NewsFeed = feedparser.parse(userSelectedFeed)
    # Enabling the Text Widget by setting state parameter of config() to NORMAL
    root.rssfeedsDetails.config(state=NORMAL)
    root.rssfeedsDetails.delete('1.0', END)
    # Looping through each item of the NewsFeed.entries dictionary
    for entryD in range(len(NewsFeed.entries)):
        # Storing each item of the NewsFeed.entries dictionary in the entry variable
        entry = NewsFeed.entries[entryD]
        # Fetch each feed details (Title, Summary, Date) and store in displayFeedDetails
        displayFeedDetails = "No. " + str(entryD+1) + "\n\nTITLE : " + entry.title + \
                             "\n\nDATE : " + entry.published + "\n\nSUMMARY: " \
                             + entry.summary + "\n\nLINK : " + entry.link +"\n\n"
        # Displaying the Feed Details in the Text Widget
        root.rssfeedsDetails.insert("end", displayFeedDetails)

    # Making Text Widget uneditable again after the displaying list of news from feed
    root.rssfeedsDetails.config(state=DISABLED)

# Creating object of tk class
root = tk.Tk()

# Setting the title, background color, windowsize & disabling the resizing property
root.title("Hemang-RSSFeedParser")
root.config(background="#d5d9e0")
root.resizable(False, False)

# Creating the tkinter variables
feedentryurl = StringVar()
selectedfeed = StringVar()

# Calling the CreateWidgets() function
CreateWidgets()

# Defining infinite loop to run application
root.mainloop()
