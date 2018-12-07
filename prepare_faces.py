# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

import hashlib
import random
import shutil
from glob import glob
import os.path

from PIL import Image, ImageDraw

orig_path = os.path.join('datasets', 'faces', 'orig')
new_path = os.path.join('datasets', 'faces')

width = height = 286
green = (0, 255, 0)

for usage in ('train', 'test', 'val'):
    path = os.path.join(new_path, usage)
    shutil.rmtree(path, ignore_errors=True)
    os.mkdir(path)

filenames = list(glob(os.path.join(orig_path, '*', '*.jpg')))
for index, filename in enumerate(filenames):
    if index % 100 == 0:
        print('Processing {} ({}/{})'.format(filename, index, len(filenames)))
    # Split images 70%/20%/10% to train/test/val
    hash_byte = hashlib.sha1(filename.encode()).digest()[0]
    if hash_byte < 0.7 * 256:
        usage = 'train'
    elif hash_byte < 0.9 * 256:
        usage = 'test'
    else:
        usage = 'val'
    final_path = os.path.join(new_path, usage, os.path.splitext(os.path.basename(filename))[0] + '.png')

    orig = Image.open(filename, 'r')
    resize = orig.resize((width, height), resample=Image.BICUBIC)
    final = Image.new('RGB', (2*width, height), (0, 0, 0))
    final.paste(resize, (width, 0))

    for i in range(random.randint(1, 3)):
        draw = ImageDraw.Draw(final)
        r = random.randint(2, height // 10)
        th = 2*r + 1
        xs, ys = width + random.randint(th, width - th), random.randint(th, height - th)
        xe, ye = width + random.randint(th, width - th), random.randint(th, height - th)
        draw.line((xs, ys, xe, ye), fill=green, width=th)
        draw.ellipse((xs - r, ys - r, xs + r, ys + r), fill=green)
        draw.ellipse((xe - r, ye - r, xe + r, ye + r), fill=green)
        del draw

    final.paste(resize, (0, 0))

    final.save(final_path)
    final.close()
    orig.close()
