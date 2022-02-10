import numpy as np

class Arithmetics:

    def __init__(self):
        pass

    def value(self):
        data = np.array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ], dtype=np.int64)

        data3d = np.array([
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ],
            [
                [11, 12, 13],
                [14, 15, 16],
                [17, 18, 19]
            ],
            [
                [21, 22, 23],
                [24, 25, 26],
                [27, 28, 29]
            ],
            
        ], dtype=np.int64)

        # print("dimensi", data.ndim)
        # print("shape", data.shape)
        # print("size", data.size)
        # print("tipe data", data.dtype)

        # print("tipe data variable", type(data))

        return data, data3d

    def slicing(self):
        x = np.arange(15)
        x = x.reshape(5,3)
        return x

    def reshape(self):
        # x = np.arange(8)
        x = np.random.randint(10, size=(4, 4, 2))
        y = np.random.randint(10, size=(4, 4, 2))

        # x_reshaped = x.reshape(2, 2, 2)
        # y = np.random.randint(10, size=(3, 8))
        # x_reshape = x.reshape(2, 4)
        # x_t = x.reshape(8)

        print(x)
        print("="*50)
        print(y)
        print("="*50)
        concated = np.concatenate([x, y])
        
        print(concated)
        
    def concatenation(self):
        x = np.array([
                [1, 2, 3],
                [4, 5, 6],
            ])

        y_ver = np.array([7, 8, 9])
        y_hor = np.array([
                    [1],
                    [2]
                ])

        x_onedim = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        vertical_stack = np.vstack([x, y_ver])
        horizontal_stack = np.hstack([x, y_hor])
        print(vertical_stack)
        print("="*50)

        #  Bagi rata Split

        x = x_onedim.shape
        
        # angka 5 adalah jumlah group
        x_key = x[0] / 5

        slicer = []
        i = 0
        while i < x[0]:
            i += x_key
            slicer.append(int(i))
        print("sebelum", slicer)
        slicer = slicer[:-1]
        print("sesudah", slicer)
        split_data1d = np.split(x_onedim, slicer)
        # print(split_data1d)

    def twodim_split(self):
        x = np.array([
                [1, 2, 3],
                [4, 5, 6],
                [10, 11, 12],
            ])

        y_ver = np.array([7, 8, 9])
        vertical_stack = np.vstack([x, y_ver])
        vertical_splited = np.vsplit(vertical_stack, [2])
        horizontal_splited = np.hsplit(vertical_stack, [2])
        print(horizontal_splited)
        # print(vertical_stack)
        # print("="*50)
        # print(splited)
        # print(type(splited))
        # print(type(splited[0]))

    def multiplier(self):
        pass

if __name__ == '__main__':
    arithmatics = Arithmetics()
    # data, data3d = arithmatics.value()
    # print(data[1, 1])
    # print(data3d.shape)
    # print(data3d[2,1,1])
    # data3d[2, 1, 1] = 30
    # print(data3d)

    # data_slicing = arithmatics.slicing()
    arithmatics.concatenation()
    