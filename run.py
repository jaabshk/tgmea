import threading
import os

def run_script(script_name):
    os.system(f'python3 {script_name}')

scripts = []

scripts.append('6723617312.py')#2024-02-08 13:08:34.072241

scripts.append('6845465895.py')#2023-12-23 02:07:08.257455

threads = []
for script in scripts:
    thread = threading.Thread(target=run_script, args=(script,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

