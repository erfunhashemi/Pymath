def get_shape():
    shapes = {
        1: "Circle",
        2: "Square",
        3: "Rectangle",
        4: "Triangle"
    }
    print("Choose a shape:")
    for key, value in shapes.items():
        print(f"{key}: {value}")
    shape_choice = int(input("Enter the number corresponding to the shape: "))
    return shapes.get(shape_choice, None)

def calculate_circle():
    radius = float(input("Enter the radius of the circle in centimeters: "))
    perimeter = 2 * 3.14159 * radius
    area = 3.14159 * radius * radius
    return perimeter, area

def calculate_square():
    side = float(input("Enter the length of one side of the square in centimeters: "))
    perimeter = 4 * side
    area = side * side
    return perimeter, area

def calculate_rectangle():
    length = float(input("Enter the length of the rectangle in centimeters: "))
    width = float(input("Enter the width of the rectangle in centimeters: "))
    perimeter = 2 * (length + width)
    area = length * width
    return perimeter, area

def calculate_triangle():
    side1 = float(input("Enter the length of side 1 of the triangle in centimeters: "))
    side2 = float(input("Enter the length of side 2 of the triangle in centimeters: "))
    side3 = float(input("Enter the length of side 3 of the triangle in centimeters: "))
    perimeter = side1 + side2 + side3
    s = perimeter / 2
    area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
    return perimeter, area

def main():
    shape = get_shape()
    if shape == "Circle":
        perimeter, area = calculate_circle()
    elif shape == "Square":
        perimeter, area = calculate_square()
    elif shape == "Rectangle":
        perimeter, area = calculate_rectangle()
    elif shape == "Triangle":
        perimeter, area = calculate_triangle()
    else:
        print("Invalid shape choice.")
        return
    
    print(f"The perimeter of the {shape.lower()} is {perimeter:.2f} cm.")
    print(f"The area of the {shape.lower()} is {area:.2f} cm².")

if __name__ == "__main__":
    main()
