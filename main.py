INSIDE = 0  # 0000
LEFT = 1  # 0001
RIGHT = 2  # 0010
BOTTOM = 4  # 0100
TOP = 8  # 1000


def compute_out_code(point, rect_min, rect_max):
    """Compute the bit code for a point (x, y) using the clip rectangle
     bounded diagonally by rect_min (x, y), and rect_max (x, y)"""

    code = INSIDE
    if point[0] < rect_min[0]:
        code = code | LEFT
    elif point[0] > rect_max[0]:
        code = code | RIGHT
    if point[1] < rect_min[1]:
        code = code | BOTTOM
    elif point[1] > rect_max[1]:
        code = code | TOP
    return code


def cohen_sutherland_line_clip(line_first, line_second, rect_min, rect_max):
    """Cohen–Sutherland clipping algorithm clips a line from
    line_first (x, y) to line_second (x, y) against a rectangle with
    diagonal from rect_min (x, y) to rect_max (x, y)
    returns True if line were clipped, or it were inside rectangle with coordinates of clipped line
    and False if line doesn't cross rectangle and coordinates of given line"""

    line_first = list(line_first)
    line_second = list(line_second)
    out_code0 = compute_out_code(line_first, rect_min, rect_max)
    out_code1 = compute_out_code(line_second, rect_min, rect_max)
    collision = False

    while True:
        if not (out_code0 | out_code1):
            collision = True
            break
        elif out_code0 & out_code1:
            break
        else:
            if out_code1 > out_code0:
                outcode_out = out_code1
            else:
                outcode_out = out_code0
            if outcode_out & TOP:
                x = line_first[0] + (line_second[0] - line_first[0]) * (rect_max[1] - line_first[1]) / (
                        line_second[1] - line_first[1])
                y = rect_max[1]
            if outcode_out & BOTTOM:
                x = line_first[0] + (line_second[0] - line_first[0]) * (rect_min[1] - line_first[1]) / (
                        line_second[1] - line_first[1])
                y = rect_min[1]
            if outcode_out & RIGHT:
                y = line_first[1] + (line_second[1] - line_first[1]) * (rect_max[0] - line_first[0]) / (
                        line_second[0] - line_first[0])
                x = rect_max[0]
            if outcode_out & LEFT:
                y = line_first[1] + (line_second[1] - line_first[1]) * (rect_min[0] - line_first[0]) / (
                        line_second[0] - line_first[0])
                x = rect_min[0]
            if outcode_out == out_code0:
                line_first[0] = x
                line_first[1] = y
                out_code0 = compute_out_code(line_first, rect_min, rect_max)
            else:
                line_second[0] = x
                line_second[1] = y
                out_code1 = compute_out_code(line_second, rect_min, rect_max)
    return collision, tuple(line_first), tuple(line_second)
