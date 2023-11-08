class Cow:
    def __init__(self, name):
        self.name = name # set self.name to be name
        self.image = None # set self.image to be None

    def get_name(self):
        return self.name

    def get_image(self):
        return self.image # retrieve attribute self.image

    def set_image(self, image):
        self.image = image # set self.image to be image, how you can update the attribute