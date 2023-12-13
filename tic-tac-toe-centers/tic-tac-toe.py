import cv2
import numpy as np


def get_centers_tic_tac_toe(image_path):
    image = cv2.imread(image_path)

    cv2.imshow('Original image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    edges = cv2.Canny(gray, 100, 200)

    cv2.imshow('Edges', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    lines = cv2.HoughLines(edges, 1, np.pi / 180, threshold = 200)

    vertical_lines = []
    horizontal_lines = []

    line_image = image.copy()
    
    for i in range(len(lines)):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))

        # 0.0 - theta для вертикальной линии, погрешность 0.10 радиан
        if abs(0.0 - theta) < 0.10:
            vertical_lines.append(lines[i])
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 2)
        
        # 1.57 радиан (90 градусов) - theta для горизонтальной линии, погрешность 0.10 радиан
        if abs(1.57 - theta) < 0.10:
            horizontal_lines.append(lines[i])
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 0, 255), 2)

    cv2.imshow('Image with lines', line_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Всего 8 линий - 4 вертикальные и 4 горизонтальные, составим массивы, состоящие из расстояний до них, и отсортируем
    vertical_lines_rhos = [vertical_lines[i][0][0] for i in range(len(vertical_lines))]
    vertical_lines_rhos.sort()
    horizontal_lines_rhos = [horizontal_lines[i][0][0] for i in range(len(horizontal_lines))]
    horizontal_lines_rhos.sort()


    center_points_image = image.copy()

    # Вычисляем координаты центров клеток
    vertical_half_distance_between_lines = (vertical_lines_rhos[2] - vertical_lines_rhos[1]) / 2
    horizontal_half_distance_between_lines = (horizontal_lines_rhos[2] - horizontal_lines_rhos[1]) / 2

    centers = []

    # Верхние клетки
    centers.append([(
        vertical_lines_rhos[0] - vertical_half_distance_between_lines,
        horizontal_lines_rhos[0] - horizontal_half_distance_between_lines
    ), (
        vertical_lines_rhos[1] + vertical_half_distance_between_lines,
        horizontal_lines_rhos[0] - horizontal_half_distance_between_lines
    ), (
        vertical_lines_rhos[3] + vertical_half_distance_between_lines,
        horizontal_lines_rhos[0] - horizontal_half_distance_between_lines
    )])

    # Средние клетки
    centers.append([(
        vertical_lines_rhos[0] - vertical_half_distance_between_lines,
        horizontal_lines_rhos[2] - horizontal_half_distance_between_lines
    ), (
        vertical_lines_rhos[1] + vertical_half_distance_between_lines,
        horizontal_lines_rhos[2] - horizontal_half_distance_between_lines
    ), (
        vertical_lines_rhos[3] + vertical_half_distance_between_lines,
        horizontal_lines_rhos[2] - horizontal_half_distance_between_lines
    )])

    # Нижние клетки
    centers.append([(
        vertical_lines_rhos[0] - vertical_half_distance_between_lines,
        horizontal_lines_rhos[3] + horizontal_half_distance_between_lines
    ), (
        vertical_lines_rhos[1] + vertical_half_distance_between_lines,
        horizontal_lines_rhos[3] + horizontal_half_distance_between_lines
    ), (
        vertical_lines_rhos[3] + vertical_half_distance_between_lines,
        horizontal_lines_rhos[3] + horizontal_half_distance_between_lines
    )])

    for arr in centers:
        for coords in arr:
            cv2.circle(center_points_image, (int(coords[0]), int(coords[1])), 5, (255,255,0), -1)

    cv2.imshow('Image with centers', center_points_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return centers

centers = get_centers_tic_tac_toe('image1.png')

for i in centers:
    print(i)
