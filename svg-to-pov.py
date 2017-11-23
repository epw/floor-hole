#! /usr/bin/env python

import re
import sys

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
        print line
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
                    point_list.append(points[0])
                    break
                pair = pair.split(",")
                point_list.append((float(pair[0]), float(pair[1])))
            points.append(point_list)
            adjust_extremes(points[-1][2][0], points[-1][2][1])
            if close:
                break
        sys.stderr.write("Not handling anything after first Close operation\n")
    print len(points)
    print extremes

def main():
    print svg_to_pov()

if __name__ == "__main__":
    main()
