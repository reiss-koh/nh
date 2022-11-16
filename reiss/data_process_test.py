p25 = multiprocessing.Process(target=func_process25)
p25.start()

p26 = multiprocessing.Process(target=func_process26)
p26.start()

p27 = multiprocessing.Process(target=func_process27)
p27.start()

p28 = multiprocessing.Process(target=func_process28)
p28.start()

p25.join()
p26.join()
p27.join()
p28.join()