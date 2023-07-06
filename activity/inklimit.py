# Ink limit module
from PIL import Image
import numpy as np
import sys
import progressbar

class InkLimitBase:
    """
    Ink limiting base class
    Apply an ink-limiting algorithm to pixels of an image
    """

    def __init__(self, inkLimit: float):
        self.inkLimit = inkLimit * 255. / 100. # max value of uint8
        self._pixels_limited = 0
        self.name = None

    def apply(self, val: np.ndarray) -> np.ndarray:
        assert val.shape == (4,)
        assert val.dtype == np.uint8
        raise NotImplementedError()

    def pixels_limited(self) -> int:
        return self._pixels_limited

    def get_name(self) -> str:
        return self.name

#TODO:  Implement your Ink Limiter class here, derived from InkLimitBase
# You should mainly need to write an apply() function that goes through the pixels
# in the val array applying your ink limiting method

def help():
    print("command line: python <input_file> <output_file> [<ink_limit>]")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        help()
        exit(-1)
    limit = 240.
    if len(sys.argv) > 3:
        limit = float(sys.argv[3])
    #TODO:  construct an ink limiter class instance to replace the following line
    inklimiter = None
    infilename = sys.argv[1]
    outfilename = sys.argv[2]
    inimg = Image.open(infilename, "r")
    arr = np.asarray(inimg)
    outarr = np.copy(arr)
    for x in progressbar.progressbar(range(arr.shape[0])):
        for y in range(arr.shape[1]):
            if inklimiter:
                outarr[x][y] = inklimiter.apply(arr[x][y])
        sys.stdout.flush()
    print("done!")
    pixels_limited = inklimiter.pixels_limited() if inklimiter else 0
    total_pixels = arr.shape[0]*arr.shape[1]
    print(f"{pixels_limited / total_pixels * 100.:.2f}% of pixels were limited.")
    outimg = Image.fromarray(outarr, mode="CMYK")
    outimg.save(outfilename, compression="tiff_deflate")
