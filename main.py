from ZeroXWM import ZeroXWM



"""Пример работы"""
if __name__ == "__main__":
    watermark = ZeroXWM(author="ZeroX", version="Build 42e")
    while True:
        watermark.animate_in()
        watermark.animate_out()