import time
from datetime import date

x = time.time()
x = "{0:.4f}".format(x)
x = float(x)


print("Seconds since January 1, 1970: ", f"{x:,}", " or","{:.2e}".format(x) ," in scientific notation")

today =date.today()
d = today.strftime("%b %d %Y")
print(d)

