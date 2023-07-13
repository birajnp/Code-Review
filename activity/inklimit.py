# Ink limit module
import sys
import progressbar
import numpy as np
from PIL import Image


class InkLimitBase:
    """
    Ink limiting base class
    Apply an ink-limiting algorithm to pixels of an image
    """

    def __init__(self, inkLimit: float):
        self.ink_limit = inkLimit * 255.0 / 100.0  # max value of uint8
        self._pixels_limited = 0
        self.name = "(None)"

    def apply(self, val: np.ndarray) -> np.ndarray:
        """
        Apply the actual ink limiting algorithm to each pixel of val
        (Needs to be implemented in the derived class)
        """
        assert val.shape == (4,)
        assert val.dtype == np.uint8
        assert self.ink_limit > 255.0
        raise NotImplementedError()

    def pixels_limited(self) -> int:
        """
        Return the number of pixels that were altered by the
        ink limiting algorithm
        """
        return self._pixels_limited

    def get_name(self) -> str:
        """
        Return the name of this ink limiting algorithm
        """
        return self.name


# TODO:  Implement your Ink Limiter class here, derived from InkLimitBase
# You should mainly need to write an apply() function that goes through the
# pixels in the val array applying your ink limiting method. It should
# also update self._pixels_limited if it makes a change.


def print_help():
    print("command line: python <input_file> <output_file> [<ink_limit>]")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()
        sys.exit(-1)
    limit = 240.0
    if len(sys.argv) > 3:
        limit = float(sys.argv[3])
    # TODO:  construct an ink limiter class instance to replace the None
    ink_limiter = None
    infilename = sys.argv[1]
    outfilename = sys.argv[2]
    inimg = Image.open(infilename, "r")
    arr = np.asarray(inimg)
    outarr = np.copy(arr)
    for x in progressbar.progressbar(range(arr.shape[0])):
        for y in range(arr.shape[1]):
            if ink_limiter:
                outarr[x][y] = ink_limiter.apply(arr[x][y])
        sys.stdout.flush()
    print("done!")
    pixels_limited = ink_limiter.pixels_limited() if ink_limiter else 0
    ink_limiter_name = ink_limiter.get_name() if ink_limiter else "(none)"
    total_pixels = arr.shape[0] * arr.shape[1]
    print(f"{pixels_limited / total_pixels * 100.:.2f}"
          f"% of pixels were limited using {ink_limiter_name}.")
    outimg = Image.fromarray(outarr, mode="CMYK")
    outimg.save(outfilename, compression="tiff_deflate")
