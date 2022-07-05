class ImageFileAcceptor:
    """This class describes the objects for accepting the image-files by using file-extensions"""

    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, string, *args, **kwargs):
        return True if string.split('.')[-1] in self.extensions else False


acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]

image_filenames = filter(acceptor, filenames)
