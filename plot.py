#!/usr/bin/env python3

import sys, os
import subprocess as Subp

Delta = 1000
i = 0
FrameIdx = 0

def plotWithPoint(template, coord, output):
    Script = template.format(output=output, x=coord[0], y=coord[1])
    Proc = Subp.Popen(["gnuplot",], stdin=Subp.PIPE)
    Proc.communicate(Script.encode())
    if Proc.returncode != 0:
        raise RuntimeError("Gnuplot failed with code {}".format(Proc.returncode))

with open("plot-template.gnu", 'r') as TempFile:
    Template = TempFile.read()

if not os.path.exists("frames"):
    os.mkdir("frames")

with open("gly_rmsd_bb.dat", 'r') as File:
    for Line in File:
        if Line.strip().startswith("#"):
            continue

        if i % Delta == 0:
            Data = [float(x) for x in Line.split()]
            plotWithPoint(Template, Data, "frames/frame-{:08d}.png".format(FrameIdx))
            FrameIdx += 1

        i += 1
