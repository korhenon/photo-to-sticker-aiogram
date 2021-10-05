from PIL import Image

class Converter:
    def get_out_size(self, size):
        width = size[0]
        height =  size[1]
        if width <= 512 and height <= 512:
            return (width, height)
        elif width > height:
            return (512, round(height * (512 / width)))
        elif height > width:
            return (round(width * (512 / height)), 512)
        elif height == width:
            return (512, 512)
    def convert(self):
        image = Image.open('input.png')
        sticker = image.resize(self.get_out_size(image.size))
        sticker.save('output.png')