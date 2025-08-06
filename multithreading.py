#Multithreading1

import threading
import time

def task1(GW1,version):
	time.sleep(3)
	print(f"Downloading the {GW1}software {version} from the repo is completed")
	
def task2(GW1):
	time.sleep(8)
	print(f"Loading the software in the {GW1} device is completed")
	
def task3(GW1):
	time.sleep(60)
	print(f"checking the software in the {GW1}is successful")

output1 =threading.Thread(target=task1,args=("Edge IoT GW","2.3"))
output1.start()

output2 =threading.Thread(target=task2,args=("Edge IoT GW",))
output2.start()

output3 =threading.Thread(target=task3,args=("Edge IoT GW",))
output3.start()

output1.join()
output2.join()
output3.join()

print("All the tasks regarding the software update is successful!")

