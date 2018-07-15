from PIL import Image
import numpy as np
import sys

pixel2char = np.array(list('WM@BN86GE5FV27L+1i|;:^",. '))
len = 256 / pixel2char.size

if __name__ == '__main__':
    file_in = sys.argv[1]
    file_out = sys.argv[2]
    image = Image.open(file_in).convert('L')
    data = np.array(image.getdata())
    data = np.reshape(data, (image.height, image.width))
    data = pixel2char[(data/len).astype(int)]
    np.savetxt(file_out, data, fmt='%c', delimiter='')
