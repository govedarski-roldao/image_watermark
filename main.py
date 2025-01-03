from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk

current_image = None


def choose_image():
    global current_image
    aplication = filedialog.askopenfilename(title="Choose an Image", filetypes=[("Images", "*.jpg;*.png;*.gif"), ("All files", "*.*")])
    if aplication:
        field_url.config(text=f"File chosen: {aplication}")
        try:
            img = Image.open(aplication)
            img = img.resize((300, 300))
            current_image = img
            tk_img = ImageTk.PhotoImage(img)
            image_area.image = tk_img
            image_area.create_image(150, 150, image=tk_img)
        except Exception as e:
            field_url.config(text=f"Error loading image: {e}")

    else:
        field_url.config(text="No application chosen")


def add_watermark():
    global current_image
    max_characters = 10
    text = watermark_text_field.get()
    if text:
        if len(text) > max_characters:
            messagebox.showinfo(title="Watermark Error", message=f"The watermark needs to have max. {max_characters} characters")
        else:
            if current_image:
                try:
                    txt = Image.new("RGBA", current_image.size, (255, 255, 255, 0))
                    d = ImageDraw.Draw(txt)
                    font = ImageFont.truetype("arial.ttf", 26)

                    d.text((100, 100), text=text, font=font, fill=(255, 255, 255, 128))

                    watermarked_image = Image.alpha_composite(current_image.convert("RGBA"), txt)

                    tk_img = ImageTk.PhotoImage(watermarked_image.resize((300, 300)))
                    image_area.image = tk_img
                    image_area.create_image(150, 150, image=tk_img)
                except Exception as e:
                    messagebox.showerror(title="Watermark Error", message=f"An error occurred: {e}")
    else:
        messagebox.showinfo(title="Watermark Error", message="You need to insert some text on the watermark field")


# region UI
# ---------------------------------    window
root = Tk()
root.title("Add a watermark to your images")
root.minsize(width=600, height=500)
root.config(padx=50, pady=50)

# ---------------------------------    Labels

# image area
image_area = Canvas(width=300, height=300, bg="white", highlightthickness=5)
image_area.grid(column=0, row=0, columnspan=2, rowspan=7)

# search title
insert_url_input = Label(text="Please choose an image", padx=20)
insert_url_input.grid(column=2, row=0, sticky="W")
# watermark title
watermark_title = Label(text="Please insert the text for the watermark (10 characters):", padx=20)
watermark_title.grid(column=2, row=4)
# search url field
field_url = Label(width=50)
field_url.grid(column=2, row=1)

# ---------------------------------    Entries
# watermark text field
watermark_text_field = Entry(width=50)
watermark_text_field.grid(column=2, row=5)

# ---------------------------------    Button
add_image = Button(text="Upload Image", padx=20, command=choose_image)
add_image.grid(column=2, row=3)

apply_button = Button(text="Create Watermark", padx=20, command=add_watermark)
apply_button.grid(column=2, row=6)

root.mainloop()
## endregion
