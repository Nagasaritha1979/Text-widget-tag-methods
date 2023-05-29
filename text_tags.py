from tkinter import *
win=Tk()
text1=Text(win,height=8,wrap=WORD)
text1.pack()

text1.insert(1.0, "An apple a day keeps the doctor away is a common English-language proverb that appeared in the 19th century, advocating for the consumption of apples, and by extension, if one eats healthy foods, one will remain in good health and will not need to see the doctor often.")

text1.tag_add("first", 1.3,1.8)
text1.tag_add("second", 1.25,1.31)
text1.tag_add("second",1.11,1.14)

#text1.tag_remove("second",1.11,1.14)
#text1.tag_delete("second")
text1.tag_config("first",foreground='red')
text1.tag_config("second",foreground='blue')

win.mainloop() 
