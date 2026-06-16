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
        self.curr_img = self.images[0]
        self.curr_photo_im = ImageTk.PhotoImage(self.curr_img)
        self.load_btn = self.g.bu(text="Load Photos", command=self.update_viewer)
        self.canvas = self.g.ca(width=300, height=300)
        self.im = self.canvas.image([0, 0], image=self.curr_photo_im)
        self.update_viewer()
        self.canvas.bind('<ButtonPress-1>', self.next_photo)
        self.g.row()
        self.rotate_btn = self.g.bu(text="Rotate", command=self.rotate_photo)
        self.zoom_btn = self.g.bu(text="Zoom in", command=self.zoom_in)
        self.restore_btn = self.g.bu(text="Restore", command=self.restore)

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
        self.curr_photo_im = ImageTk.PhotoImage(self.curr_img)
        self.im.config(image=self.curr_photo_im)

    def load_and_update(self, event=None):
        self.load_photos()
        self.curr_img = self.images[self.ind]
        self.update_viewer()

    def next_photo(self, event):
        self.ind += 1

        if self.ind == len(self.images):
            self.ind = 0

        self.curr_img = self.images[self.ind]
        self.update_viewer()

    def rotate_photo(self):
        self.curr_img = self.curr_img.rotate(90, expand=True)
        self.update_viewer()

    def zoom_in(self):
        width, height = self.curr_img.size
        self.curr_img = self.curr_img.crop((width/2 - 30, height/2 - 30, width/2 + 30, height/2 + 30)).resize(
            (width, height), PIL.LANCZOS
        )

        self.update_viewer()

    def restore(self):
        self.curr_img = self.images[self.ind]
        self.update_viewer()

if __name__ == '__main__':
    p = PhotoView()
    p.g.mainloop()
