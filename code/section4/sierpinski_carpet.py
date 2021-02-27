import Init
import numpy as np
import copy
FILE_DIR = "./img"
iteration_time = 8


def main():
    basic_block = [[0, 0, 0], [0, 255, 0], [0, 0, 0]]
    for kase in range(1, iteration_time+1):
        new_block = [[255 for n in range(pow(3, kase+1))]for n in range(pow(3, kase+1))]
        for p in range(0, 3):
            for q in range(0, 3):
                print(kase, iteration_time + 1, p, q ,end = "\r")
                if p == 1 and q == 1:
                    continue
                for i in range(0, len(basic_block)):
                    for j in range(0, len(basic_block[i])):
                        #print(p, q, i, j)
                        new_block[p * len(basic_block) + i][q * len(basic_block[0]) + j] = basic_block[i][j]
        #print(new_block)
        basic_block = new_block
    print()
    """
    for i in range(0, len(basic_block)):
        for j in range(0, len(basic_block[i])):
            if basic_block[i][j] == 0:
                basic_block[i][j] = [0, 0, 0]
            else:
                basic_block[i][j] = [255, 255, 255]
    
    """
    Filename = FILE_DIR + str(iteration_time+1) + ".png"
    Init.ImageIO(file_dir = Filename, img = np.float32(basic_block), io = "o", mode = "grey", backend = "opencv")


"""
def main():
    kase = iteration_time
    vals = [[[0]] for n in range(pow(pow(3, kase), 2))]
    for i in range(0, len(vals)):
        print(i, len(vals), end = "\r")
        have_five = False
        new_i = i
        while 1:
            code = new_i - 9 * int(new_i/9)
            if code == 4:
                have_five = True
                break
            if int(new_i/9) == 0:
                break
            new_i = int(new_i/9)

        if have_five:
            vals[i][0][0] = 255
    print()
    mark = 0
    while 1:
        print(mark, len(vals), end = "\r")
        if mark + 1 >= len(vals):
            break
        matrix = vals[mark: mark + 9]
        new_matrix = [[0 for n in range(len(vals[mark]) * 3)] for n in range(len(vals[mark]) * 3)]
        for p in range(0, 3):
            for q in range(0, 3):
                for i in range(0, len(vals[mark])):
                    for j in range(0, len(vals[mark])):
                        new_matrix[p * len(vals[mark]) + i][q * len(vals[mark]) + j] = matrix[p * 3 + q][i][j]
        mark += 9
        vals.append(new_matrix)
    print()
    Filename = FILE_DIR + str(kase) + ".png"
    img = vals[len(vals) - 1]
    for i in range(0, len(img)):
        for j in range(0, len(img[i])):
            if img[i][j] == 0:
                img[i][j] = [0, 0, 0]
            else:
                img[i][j] = [255, 255, 255]
    Init.ImageIO(file_dir = Filename, img = np.float32(img), io = "o", mode = "grey", backend = "Pillow")
    return
"""

if __name__ == '__main__':
    main()