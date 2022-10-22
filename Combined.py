from pynput.mouse import Listener

import os
import asyncio
from threading import Timer
from pywizlight import wizlight, PilotBuilder, discovery
import time

def on_move(x, y):
    # print("Mouse moved to ({0}, {1})".format(x, y))
    async def main():
        light = wizlight("192.168.18.59") # Call The IP of the Particular Bulb
        await light.turn_on(PilotBuilder()) #os.system('"wizlight on"') '''Turn On The Bulb'''
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
    time.sleep(2.5)
    loop.close()
    # return None
'''
def on_click(x, y, button, pressed):
    if pressed:
        btn = '{0}'.format(button)
        if(btn == "Button.middle"):
            # print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button)) #logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
            async def main():
                light = wizlight("192.168.1.28") # Call The IP of the Particular Bulb
                await light.turn_off() #os.system('"wizlight off"')
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(main())
            time.sleep(5)
            loop.close()
            # return None
'''
    
with Listener(on_move=on_move) as listener: #, on_scroll=on_scroll, on_click=on_click,
    listener.join()

