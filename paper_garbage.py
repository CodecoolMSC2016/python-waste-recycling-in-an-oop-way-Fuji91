from garbage import Garbage


class PaperGarbage(Garbage):

    def __init__(self, name, squeeze):
        super(PaperGarbage, self).__init__(name)
        self.is_squeezed = squeeze

    def squeeze(self):
        if self.is_squeezed is False:
            self.is_squeezed = True
            return self.is_squeezed