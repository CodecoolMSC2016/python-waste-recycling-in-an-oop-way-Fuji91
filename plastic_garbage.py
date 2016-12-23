from garbage import Garbage


class PlasticGarbage(Garbage):

    def __init__(self, name, clean):
        super(PlasticGarbage, self).__init__(name)
        self.is_clean = clean

    def clean(self):
        if self.is_clean is False:
            self.is_clean = True
            return self.is_clean