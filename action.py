#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
__version__ =   "0.1"
__author__  =   "@lantip"
__date__    =   "2013/02/08"

an extend from Geovedi's Botgan
"""

import numpy, pylab
from PIL import Image, ImageDraw, ImageFont
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d
from botgan import ask_kaskus
import sys


def f(s, n):
    return ' '.join(s.split()[:n])

def draw_captcha(word):
    ln = len(word) * 23
    sz = (ln,50)
    img = Image.new('L', sz, 255)
    drw = ImageDraw.Draw(img)
    font = ImageFont.truetype("futura.TTF", 36)

    drw.text((10,5), word, font=font)
    #img.save('test.png')

    X , Y = numpy.meshgrid(range(sz[0]),range(sz[1]))
    Z = 1-numpy.asarray(img)/255

    fig = pylab.figure()
    ax = axes3d.Axes3D(fig)
    ax.plot_wireframe(X, -Y, Z, rstride=1, linewidths=.2)
    ax.view_init(45,-100)
    ax.set_zlim((-20,10))
    ax.set_axis_off()
    fig.savefig('captcha.png')
    return 'captcha saved!'
  
if __name__ == '__main__':
    question = raw_input('> ')
    while (question != 'quit'):
        try:
            print draw_captcha(f(ask_kaskus(question).lower(),2))
            question = raw_input('> ')
        except:
            sys.exit(1)
