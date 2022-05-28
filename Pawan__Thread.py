import time as Samay
import threading
import concurrent.futures 


def Kar__Do__Na():
	print("Starting now")
	Samay.sleep(3)
	print("Ending now")



#Old <ethgod with No Threading .........
def main0():
	Arambh = Samay.perf_counter()
	Kar__Do__Na()
	Kar__Do__Na()
	Kar__Do__Na()
	Kar__Do__Na()
	Kar__Do__Na()
	Kar__Do__Na()
	Kar__Do__Na()
	Kar__Do__Na()
	Kar__Do__Na()
	Kar__Do__Na()
	Aanth = Samay.perf_counter()
	Kaal = Aanth - Arambh
	print(f'Time elapsed is calculated to be {Kaal} seconds')




#Threads created but no loop used at all
def main1():
	Arambh = Samay.perf_counter()
	T0 = threading.Thread(target = Kar__Do__Na)
	T1 = threading.Thread(target = Kar__Do__Na)
	T2 = threading.Thread(target = Kar__Do__Na)
	T3 = threading.Thread(target = Kar__Do__Na)
	T4 = threading.Thread(target = Kar__Do__Na)
	T5 = threading.Thread(target = Kar__Do__Na)
	T6 = threading.Thread(target = Kar__Do__Na)
	T7 = threading.Thread(target = Kar__Do__Na)
	T8 = threading.Thread(target = Kar__Do__Na)
	T9 = threading.Thread(target = Kar__Do__Na)
	T0.start()
	T1.start()
	T2.start()
	T3.start()
	T4.start()
	T5.start()
	T6.start()
	T7.start()
	T8.start()
	T9.start()
	T0.join()
	T1.join()
	T2.join()
	T3.join()
	T4.join()
	T5.join()
	T6.join()
	T7.join()
	T8.join()
	T9.join()	
	Aanth = Samay.perf_counter()
	Kaal = Aanth - Arambh
	print(f'Time elapsed is calculated to be {Kaal} seconds')




#Threads created and loop used
def main3():
	Thread__List = []
	Arambh = Samay.perf_counter()
	for _ in range(10):
		T = threading.Thread(target = Kar__Do__Na)
		T.start()
		Thread__List.append(T)
	for Single__Thread in Thread__List:
		Single__Thread.join()
	Aanth = Samay.perf_counter()
	Kaal = Aanth - Arambh
	print(f'Time elapsed is calculated to be {Kaal} seconds')	



#Using Concurrenbt Futures Method (Python Version 3.2 and above)
def main4():
	Arambh = Samay.perf_counter()
	with concurrent.futures.ThreadPoolExecutor() as Dhaga__Kund__Chalak:
		for _ in range(10):
			Dhaga__Kund__Chalak.submit(Kar__Do__Na) 
	Aanth = Samay.perf_counter()
	Kaal = Aanth - Arambh
	print(f'Time elapsed is calculated to be {Kaal} seconds')	



if __name__ == '__main__':
	main4()

