import time
import random
import threading
from itertools import cycle

from .utils import clear, get_terminal_width, fclear
from .logo import watermark


class ZeroXWM:
    def __init__(self, watermark=watermark, speed=0.01, random_range=5, vertical_offset=5, author=None, version=None,
                 fast_clear=True):
        self.watermark = watermark
        self.speed = speed
        self.random_range = random_range
        self.fast_clear = fast_clear
        self.vertical_offset = vertical_offset
        self._width = len(max(self.watermark, key=len))

        self.metadata = self._gen_metadata_string(author, version)

        self._is_running = False
        self._thread = None

    def _gen_metadata_string(self, author: str = None, version: str = None) -> str | None:
        if author and version:
            return (version +
                    " " * (self._width - len(version) - len(author)) +
                    author)
        elif version:
            return version.rjust(self._width)
        elif author:
            return author.rjust(self._width)

        return None

    def _center_offset(self):
        return (get_terminal_width() - self._width) // 2

    def _animate(self, direction="in"):
        left_space = self._center_offset()
        clear()

        for i in range(self._width):
            print("\n" * self.vertical_offset, end="")
            for string in self.watermark:
                if direction == "in":
                    print(" " * left_space + string[:abs(i + random.randint(-self.random_range, self.random_range))])
                else:
                    r_size = min(abs(i + random.randint(-self.random_range, self.random_range)), len(string))
                    print(" " * left_space + " " * r_size + string[r_size:])

            if self.metadata:
                print("\n" + " " * left_space + self.metadata)

            time.sleep(self.speed)
            print()  # Хз как, но он повышает плавность // доп строка уменьшает мерцание
            if self.fast_clear:
                fclear()
            else:
                clear()

    def _animation_loop(self, min_once=True):
        cycle = 0
        while self._is_running or (min_once and cycle == 0):
            self._animation_cycle()
            cycle += 1

    def _animation_cycle(self):
        self._animate(direction="in")
        self._animate(direction="out")

    def animate_in(self):
        self._animate("in")

    def animate_out(self):
        self._animate("out")

    def run_animation_in_thread(self, min_once=True):
        if self._thread and self._thread.is_alive():
            return

        self._is_running = True
        self._thread = threading.Thread(target=self._animation_loop, args=(min_once,), daemon=True)
        self._thread.start()

    def stop_animation(self):
        self._is_running = False
        if self._thread:
            self._thread.join()
