import typer
import time

def loading_func():
    with typer.progressbar(range(10))as sp:
        for i in sp:

            time.sleep(0.1)
        time.sleep(0.3)