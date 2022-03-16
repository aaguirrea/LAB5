import pyfirmata

import time

board = pyfirmata.Arduino('COM3')


while True:
    
    # led rojo
    board.digital [10]. write (1)
    time.sleep(2)
    board.digital [10]. write (0)
    time.sleep(2)
    