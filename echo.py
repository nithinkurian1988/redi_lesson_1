import sys
import signal

try:
  while True:
    i_data = input()
    print(i_data)  
except KeyboardInterrupt:
  print("Ctrl-C pressed!")
  sys.exit(0)