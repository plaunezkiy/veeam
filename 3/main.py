from testing import TestCase


class TestCase1(TestCase):
    name = 'List of Files'
    tc_id = 1

    def prep(self):
        from datetime import datetime
        import time
        seconds = time.mktime(datetime.now().timetuple())
        if seconds % 2:
            raise Exception('Odd Number of Seconds')

    def run(self):
        from pathlib import Path
        from os import listdir
        print(listdir(str(Path.home())))


class TestCase2(TestCase):
    name = 'Random File'
    tc_id = 2

    def prep(self):
        from psutil import virtual_memory
        ram = virtual_memory().total / (1024.0 ** 3)
        if ram < 1:
            raise Exception('Not Enough RAM')

    def run(self):
        from random import randint
        with open('test', 'w+') as file:
            for i in range(1024 ** 2):
                file.write(chr(randint(33, 126)))

    def clean_up(self):
        from os import remove
        remove('test')


TestCase1().execute()
TestCase2().execute()
