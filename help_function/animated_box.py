import datetime
import time

import flet as ft
import requests
import base64
import io
from functools import lru_cache
import asyncio


class AnimatedBox(ft.Container):
    def __init__(self, STILE_MODE: str, **kwargs):
        ft.Container.__init__(self, **kwargs)
        self.instruments_light = [
            self.get_image("drum_light", "LIGHT", "png"),
            self.get_image("electro_light", "LIGHT", "png"),
            self.get_image("fleit_light", "LIGHT", "png"),
            self.get_image("guitar_light", "LIGHT", "png"),
            self.get_image("piano_light", "LIGHT", "png"),
            self.get_image("pick_light", "LIGHT", "png"),
        ]
        self.instruments_dark = [
            self.get_image(r"drum_dark", "DARK", "png"),
            self.get_image(r"electro_dark", "DARK", "png"),
            self.get_image(r"fleit_dark", "DARK", "png"),
            self.get_image(r"guitar_dark", "DARK", "png"),
            self.get_image(r"piano_dark", "DARK", "png"),
            self.get_image(r"pick_dark", "DARK", "png"),
        ]
        if STILE_MODE == "dark":
            self.instruments = self.instruments_dark
        else:
            self.instruments = self.instruments_light
        self.current_index = 0

    @lru_cache
    def get_image(self, name, style, val):
        # Загружаем изображение через API
        request = requests.get(f" http://localhost:30000/images/{style}/{name}.{val}")
        base_64_image = base64.b64encode(io.BytesIO(request.content).read()).decode()
        return f"data:image/{val};base64,{base_64_image}"

    def did_mount(self):
        self.page.run_task(self.startAnimatedBox)

    async def startAnimatedBox(self, timeout: float = None):
        if timeout is None:
            timeout = 9999999

        time_now = time.time()
        while (time.time() - time_now) < timeout:
            # Устанавливаем быстрое вращение до 270 градусов
            self.rotate = ft.transform.Rotate(3.14 * 3 / 4, alignment=ft.alignment.center)
            self.update()
            await asyncio.sleep(0.3)  # Время на быструю часть вращения

            # Устанавливаем полное вращение с замедлением
            self.rotate = ft.transform.Rotate(3.14 * 2, alignment=ft.alignment.center)
            self.update()
            await asyncio.sleep(0.7)  # Время на замедленное вращение

            # Смена изображения
            self.current_index = (self.current_index + 1) % len(self.instruments)
            self.content = ft.Image(
                src=self.instruments[self.current_index],
                width=300,
                height=200,
            )
            self.rotate = ft.transform.Rotate(0, alignment=ft.alignment.center)  # Сброс вращения
            self.update()

            # Пауза перед следующим циклом
            await asyncio.sleep(2)


class SendData(AnimatedBox):
    def __init__(self, PTH: str, **kwargs):
        self.PTH = PTH
        super().__init__(**kwargs)

    def did_mount(self):
        self.page.run_task(self.whileStartAnimatedBox)

    async def whileStartAnimatedBox(self):
        await self.startAnimatedBox(timeout=0.1)
        self.update()
        self.page.go(f"{str(self.PTH)}")
