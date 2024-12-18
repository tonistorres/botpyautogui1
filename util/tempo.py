import time as tm

def PauseApp(qtdeSeconds):
    for x in range(0,qtdeSeconds):
        tm.sleep(1)
        print(f"{x+1}s")
