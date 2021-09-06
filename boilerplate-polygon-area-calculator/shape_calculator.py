class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = (2 * self.width) + (2 * self.height)
        return perimeter

    def get_diagonal(self):
        diagonal = ((self.width ** 2) + (self.height ** 2)) ** .5
        return diagonal

    def get_picture(self):

        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        else:
            width_line = f"{'*' * self.width}\n"
            picture = self.height * width_line
            return picture

    def get_amount_inside(self, string):
        string = str(string)

        if "Square" in string:
            equal = string.find("=")
            s_width = string[equal + 1 : len(string) - 1]
            s_height = s_width

        elif "Rectangle" in string:
            list_string = string.split("(")
            list_data = list_string[1].split(",")

            equal1 = list_data[0].find("=")
            s_width = list_data[0][equal1 + 1 :]

            equal2 = list_data[1].find("=")
            s_height = list_data[1][equal2 + 1 : len(list_data[1]) - 1]

        s_area = int(s_width) * int(s_height)
        amount = int(self.get_area() / s_area)
        return amount

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.height = height
        self.width = height

    def __str__(self):
        return f"Square(side={self.width})"