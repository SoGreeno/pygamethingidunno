import time
from progressbar import ProgressBar
# Progress bar nie działa bo pokazuje że ProgressBar nie istnieje :'(
bar = ProgressBar(maxval = 100)
bar.start()
time.sleep(0.2)
bar.update(20)
time.sleep(0.2)
bar.update(30)
time.sleep(0.5)
bar.update(40)
time.sleep(1)
bar.update(10)

