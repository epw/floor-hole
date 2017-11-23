#! /usr/bin/env python

import re
import sys

def out_pair(pair):
    return "<%g,%g>" % (pair[0], pair[1])

def declaration(points):
    print "#declare POINTS = array[%d] {" % ((len(points)-1) * 3)
    maybe_comma = ","
    for i in range(len(points[:-1])):
        if i == len(points) - 2:
            maybe_comma = ""
        print "%s, %s, %s%s" % (out_pair(points[i+1][0]),
                                out_pair(points[i+1][1]),
                                out_pair(points[i][-1]), maybe_comma)
    print "};"

def avg(x, y):
    return (x + y) / 2

def svg_to_pov():
    started = False
    extremes = {}
    def adjust_extremes(x, y):
        if x < extremes["min_x"]:
            extremes["min_x"] = x
        if x > extremes["max_x"]:
            extremes["max_x"] = x
        if y < extremes["min_y"]:
            extremes["min_y"] = y
        if y > extremes["max_y"]:
            extremes["max_y"] = y
    points = []
    with open("edge.svg") as f:
        while not started:
            line = f.readline()
            if line.find("<path") != -1:
                started = True
        assert(f.readline().find("fill=\"none\" stroke=\"black\"") != -1)
        regex = re.search(r"M ([0-9.]+),([0-9.]+)", f.readline())
        assert(regex)
        points.append([(float(regex.group(1)), float(regex.group(2)))])
        extremes["min_x"] = extremes["max_x"] = points[0][0][0]
        extremes["min_y"] = extremes["max_y"] = points[0][0][1]
        line = f.readline()
        regex = re.search(r"C ([0-9.]+),([0-9.]+) ([0-9.]+),([0-9.]+) ([0-9.]+),([0-9.]+)", line)
        assert(regex)
        points.append([(float(regex.group(1)), float(regex.group(2))),
                       (float(regex.group(3)), float(regex.group(4))),
                       (float(regex.group(5)), float(regex.group(6)))])
        adjust_extremes(points[-1][2][0], points[-1][2][1])
        close = False
        for line in f:
            pairs = line.strip().split(" ")
            point_list = []
            for pair in pairs:
                if pair.strip() == "Z":
                    close = True
                    points.append(point_list)
                    adjust_extremes(points[-1][2][0], points[-1][2][1])
#                    points.append(points[0])
                    break
                pair = pair.split(",")
                point_list.append((float(pair[0]), float(pair[1])))
            if not close:
                points.append(point_list)
                adjust_extremes(points[-1][2][0], points[-1][2][1])
            else:
                break
        sys.stderr.write("Not handling anything after first Close operation\n")
    middle_x = avg(extremes["min_x"], extremes["max_x"])
    middle_y = avg(extremes["min_y"], extremes["max_y"])
    
    normalized_points = [[(pair[0] - middle_x, pair[1] - middle_y) for pair in pairs] for pairs in points]
    print "#declare POINTS = array[%d] {" % len(points)
    print ",\n".join(["<%g, %g>" % (p[0], p[1]) for p in [pair[-1] for pair in normalized_points]])
    print "};"

def main():
    svg_to_pov()

if __name__ == "__main__":
    main()
