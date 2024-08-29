from PIL import Image, ImageDraw
import os

# Define the size and background color
size = (50, 50)
background_color = (255, 255, 255, 0)  # Transparent background
fill_color = (0, 0, 0)  # Black color


# Function to draw and save an image
def create_shape_image(draw_func, filename):
    image = Image.new("RGBA", size, background_color)
    draw = ImageDraw.Draw(image)
    draw_func(draw)
    image.save(os.path.join("png2", f"{filename}.png"))


# 1. Square
def draw_square(draw):
    draw.rectangle([(10, 10), (40, 40)], fill=fill_color)


# 2. Ellipse
def draw_ellipse(draw):
    draw.ellipse([(10, 15), (40, 35)], fill=fill_color)


# 3. Right Triangle
def draw_right_triangle(draw):
    draw.polygon([(10, 40), (40, 40), (10, 10)], fill=fill_color)


# 4. Rotated Square (Diamond Shape)
def draw_rotated_square(draw):
    draw.polygon([(25, 10), (40, 25), (25, 40), (10, 25)], fill=fill_color)


# 5. Circle
def draw_circle(draw):
    draw.ellipse([(15, 15), (35, 35)], fill=fill_color)


# 6. Equilateral Triangle
def draw_equilateral_triangle(draw):
    draw.polygon([(25, 10), (40, 35), (10, 35)], fill=fill_color)


# 7. Vertical Rectangle
def draw_vertical_rectangle(draw):
    draw.rectangle([(20, 10), (30, 40)], fill=fill_color)


# 8. Hexagon
def draw_hexagon(draw):
    draw.polygon([(25, 10), (35, 20), (35, 30), (25, 40), (15, 30), (15, 20)], fill=fill_color)


# 9. Acute Angled Triangle
def draw_acute_triangle(draw):
    draw.polygon([(10, 40), (40, 40), (30, 20)], fill=fill_color)


# 10. Horizontal Rectangle
def draw_horizontal_rectangle(draw):
    draw.rectangle([(10, 20), (40, 30)], fill=fill_color)


# 11. Five-pointed Star
def draw_star(draw):
    draw.polygon([(25, 10), (30, 20), (40, 20), (32, 28), (35, 40), (25, 32), (15, 40), (18, 28), (10, 20), (20, 20)], fill=fill_color)


# 12. Trapezoid
def draw_trapezoid(draw):
    draw.polygon([(15, 40), (35, 40), (30, 20), (20, 20)], fill=fill_color)


# Create and save all images
shapes = [
    (draw_square, "square"),
    (draw_ellipse, "ellipse"),
    (draw_right_triangle, "right_triangle"),
    (draw_rotated_square, "rotated_square"),
    (draw_circle, "circle"),
    (draw_equilateral_triangle, "equilateral_triangle"),
    (draw_vertical_rectangle, "vertical_rectangle"),
    (draw_hexagon, "hexagon"),
    (draw_acute_triangle, "acute_triangle"),
    (draw_horizontal_rectangle, "horizontal_rectangle"),
    (draw_star, "star"),
    (draw_trapezoid, "trapezoid"),
]

for draw_func, filename in shapes:
    create_shape_image(draw_func, filename)
