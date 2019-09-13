from PIL import Image
import os
from numpy import *
from matplotlib import pyplot as plt
import time
import filetype

import tensorflow.keras.models as models
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D

def process(img1_name, grid_dir, cell_dir):
    file_type = filetype.guess(img1_name).extension
    img1 = Image.open(img1_name)
    img2 = img1.resize((252,252))
    os.makedirs(grid_dir)
    os.makedirs(cell_dir)
    img2_name = grid_dir + 'sudokuGrid.' + file_type
    img2.save(img2_name)

    slice_image(img2, 9, 9, cell_dir, file_type)

 
def slice_image(img, rows, cols, new_path, file_type):
    width, height = img.size
    for i in range(rows):
        for j in range(cols):
            box = (j*int(width/rows),i*int(height/cols), j*int(width/rows)+int(width/rows), i*int(height/cols)+int(height/cols))
            cell = img.crop(box)
            cell = cell.crop((3,3,25,25))
            cell = cell.resize((28,28))
            cell.save(new_path + 'sudokuCell' + str(i) + str(j) + '.' + file_type)

def create_data(cell_dir):
    test = []
    for cell in os.listdir(cell_dir):
        cell = Image.open(cell_dir + cell).convert('L')
        test.append(array(cell).flatten())
    test = (255-reshape(test, (81, 28, 28, 1)).astype('float32'))/255
    return test

def remove(grid_dir, cell_dir):
    for x in os.listdir(cell_dir):
        os.unlink(cell_dir + x)
    os.rmdir(cell_dir)
    for x in os.listdir(grid_dir):
        os.unlink(grid_dir + x)
    os.rmdir(grid_dir)


def getInput(img1_name):
    grid_dir = img1_name + '/../grid_fromSudokuSolver/'
    cell_dir = grid_dir + 'cells_fromSudokuSolver/'
    process(img1_name, grid_dir, cell_dir)
    data = create_data(cell_dir)
    remove(grid_dir, cell_dir)
    model = models.load_model('digit_reader_for_sudoku.model')
    # plt.figure()
    j= 1
    inputb = ''
    for i in data:
        # plt.subplot(9,9, j)
        j += 1
        # plt.imshow(i.reshape(28, 28),cmap='Greys')
        pred = model.predict(i.reshape(1, 28, 28, 1))
        # plt.title(str(pred.argmax()))
        if (pred.argmax() == 10):
            inputb += '0'
        else:
            inputb += str(pred.argmax())
    plt.show()
    return inputb
