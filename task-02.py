import turtle


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    for _ in range(2):
        koch_curve(t, order, size)
        t.right(120)

    koch_curve(t, order, size)

    window.mainloop()


if __name__ == "__main__":
    try:
        level = int(
            input("Введіть рівень рекурсії для малювання сніжинки Коха, наприклад 3: "))
        if level < 0:
            raise ValueError("Рівень рекурсії повинен бути невід'ємним числом")

        draw_koch_curve(level)

    except ValueError as e:
        print(f"Помилка {e}")
