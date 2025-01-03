from tkinter import *
from tkinter import filedialog

from sqlalchemy import column


def choose_image():
    aplication = filedialog.askopenfilename(title="Choose an Image", filetypes=[("Images", "*.jpg"), ("Todos os arquivos", "*.*")])
    if aplication:



# region UI
# ---------------------------------    Window
root = Tk()
root.title("Add a watermark to your images")
root.minsize(width=600, height=500)
root.config(padx=50, pady=50)

# ---------------------------------    Labels

# image area
image_area = Canvas(width=200, height=200, bg="white", highlightthickness=5)
image_area.grid(column=0, row=0, columnspan=2, rowspan=7)

# search title
insert_url_input = Label(text="Please choose an image", padx=20)
insert_url_input.grid(column=2, row=0, sticky="W")
# watermark title
watermark_title = Label(text="Please insert the text for the watermark (10 characters):", padx=20)
watermark_title.grid(column=2, row=4)

# ---------------------------------    Entries
# search url field
field_url = Entry(width=50)
field_url.grid(column=2, row=1)
# watermark text field
watermark_text_field = Entry(width=50)
watermark_text_field.grid(column=2, row=5)

# ---------------------------------    Button
add_image = Button(text="Upload Image", padx=20)
add_image.grid(column=2, row=3)

apply_button = Button(text="Create Watermark", padx=20)
apply_button.grid(column=2, row=6)

root.mainloop()
# end Region
