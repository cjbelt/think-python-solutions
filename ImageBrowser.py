from swampy.Gui import *
from tkinter import PhotoImage
import PIL.Image as PIL
from PIL import ImageTk
import os

class PhotoView(object):
    def __init__(self, im_path=os.getcwd()):
        self.g = Gui()
        self.dir_entry = self.g.en(text=im_path)
        self.dir_entry.bind('<Return>', self.update_viewer)
        self.load_photos()
        self.curr_photo = ImageTk.PhotoImage(self.images[0])
        self.load_btn = self.g.bu(text="Load Photos", command=self.update_viewer)
        self.canvas = self.g.ca(width=300, height=300)
        self.im = self.canvas.image([0, 0], image=self.curr_photo)
        self.update_viewer()
        self.canvas.bind('<ButtonPress-1>', self.next_photo)

    def load_photos(self, event=None):
        self.ind = 0
        self.images = []
        dir_path = self.dir_entry.get()

        for file in os.listdir(dir_path):
            try:
                file_path = os.path.join(dir_path, file)
                image = PIL.open(file_path)
                self.images.append(image)
            except (PIL.UnidentifiedImageError, IsADirectoryError):
                continue

    def update_viewer(self, event=None):
        self.load_photos()
        self.curr_photo = ImageTk.PhotoImage(self.images[self.ind])
        self.im.config(image=self.curr_photo)


    def next_photo(self, event):
        self.ind += 1

        if self.ind == len(self.images):
            self.ind = 0

        self.curr_photo = ImageTk.PhotoImage(self.images[self.ind])
        self.im.config(image=self.curr_photo)

if __name__ == '__main__':
    p = PhotoView()
    p.g.mainloop()
