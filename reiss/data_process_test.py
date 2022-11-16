p53 = multiprocessing.Process(target=func_process53)
p53.start()

p54 = multiprocessing.Process(target=func_process54)
p54.start()

p55 = multiprocessing.Process(target=func_process55)
p55.start()

p56 = multiprocessing.Process(target=func_process56)
p56.start()

p53.join()
p54.join()
p55.join()
p56.join()