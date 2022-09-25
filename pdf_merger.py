#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import tkinter as tk
import PyPDF2
from tkinter import filedialog


def files() -> tuple:
    root = tk.Tk()
    root.withdraw()
    file = filedialog.askopenfilenames()
    return file

def order(file: tuple, count: int = 0) -> list:
    file_1 = []
    for i in file:
        count += 1
        for data in i.split('/'):
            i = data
        print(f"{count} -> {i}")
    orders = list(input())
    for i in range(len(orders)):
        file_1.append(file[int(orders[i])-1])
    return file_1

def merge(file: list) -> str:
    name = str(input('Please write the name for your PDF data: '))
    mergeFile = PyPDF2.PdfFileMerger()
    for pdf in file:
        mergeFile.append(PyPDF2.PdfFileReader(pdf, 'rb'))
    mergeFile.write(name)
    return 'Your PDF is merged now!'


if __name__ == '__main__':
    print(merge(order(files())))
