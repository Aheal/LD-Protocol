
import time
class test:
  def __init__(self):
    self.timecont=0

  def printit(self):
    while True:
      print ("Hello, World!") 
      time.sleep(1)
      

def main():
  try:
    test().printit()
  except KeyboardInterrupt:
    print('Good')
    
main()