import time
import random
from .utils import clear, get_terminal_width, fclear
from .logo import watermark


class ZeroXWM:
    def __init__(self, watermark=watermark, speed=0.01, random_range=5, vertical_offset=5, author=None, version=None, fast_clear=True):
        self.watermark = watermark
        self.speed = speed
        self.random_range = random_range
        self.fast_clear = fast_clear
        self.metadata = self._gen_metadata_string(author, version)
        self.vertical_offset = vertical_offset

    def _gen_metadata_string(self, author: str = None, version: str = None) -> str | None:
        if author and version:
            return (version +
                    " " * (len(max(self.watermark, key=len)) - len(version) - len(author)) +
                    author)
        elif author:
            return " " * (len(max(self.watermark, key=len)) - len(author)) + author
        elif version:
            return " " * (len(max(self.watermark, key=len)) - len(version)) + version

        return None

    def _center_offset(self):
        return (get_terminal_width() - len(max(self.watermark, key=len))) // 2

    def _animate(self, direction="in"):
        left_space = self._center_offset()
        clear()

        for i in range(len(max(self.watermark, key=len))):
            print("\n" * self.vertical_offset)
            for string in self.watermark:
                if direction == "in":
                    print(" " * left_space + string[:abs(i + random.randint(-self.random_range, self.random_range))])
                else:
                    r_size = abs(i + random.randint(-self.random_range, self.random_range))
                    print(" " * left_space + " " * r_size + string[r_size:])

            if self.metadata:
                print("\n" + " " * left_space + self.metadata)

            time.sleep(self.speed)
            print()  # Хз как, но он повышает плавность
            if self.fast_clear:
                fclear()
            else:
                clear()

    def animate_in(self):
        self._animate("in")

    def animate_out(self):
        self._animate("out")
