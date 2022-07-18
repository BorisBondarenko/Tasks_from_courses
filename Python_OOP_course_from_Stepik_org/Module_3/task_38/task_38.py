class FileAcceptor:
    """This class describes the instances that can collect the file-extensions.
    Then this instances using as verifier of input file-extension.

    Allowed extensions are adding in the moment of creating new instance.
    And then we could merge instances collection by using "+" - operator."""

    def __init__(self, *args):
        self.extensions = args

    def __call__(self, filename):
        return True if filename.split('.')[-1] in self.extensions else False

    def __add__(self, other):
        if isinstance(other, FileAcceptor):
            ext = list(set(self.extensions + other.extensions))
            return FileAcceptor(*ext)
