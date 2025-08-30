from ZeroXWM import ZeroXWM, watermark
import time

"""Пример работы"""
if __name__ == "__main__":
    watermark = ZeroXWM(author="ZeroX", version="Build 0.47b")

    # Просто анимация
    while True:
        watermark.animate_in()
        watermark.animate_out()


    # Пример работы в потоке

    watermark.run_animation_in_thread()
    time.sleep(44)  # <- Имитация работы
    watermark.stop_animation()



