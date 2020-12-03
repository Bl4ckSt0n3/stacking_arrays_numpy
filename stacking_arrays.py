import numpy as np

# adjust numpy random module and set as default_rng()
rg = np.random.default_rng()

def vertical_stack(x, y):
	
	arr_1 = np.floor(10*rg.random((x, y)))
	arr_2 = np.floor(10*rg.random((x, y)))
	
	print("vertical random array 1:\n\n", arr_1, "\n")
	print("vertical random array 2:\n\n", arr_2, "\n")
	
	res = np.vstack((arr_1, arr_2))
	
	print("***** vertical stacking togather arrays *****")
	print(res)
	
def horizontal_stack(x, y):
	
	arr_1 = np.floor(10*rg.random((x, y)))
	arr_2 = np.floor(10*rg.random((x, y)))
	
	print("horizontal random array 1:\n\n", arr_1, "\n")
	print("horizontal random array 2:\n\n", arr_2, "\n")
	
	res = np.hstack((arr_1, arr_2))
	
	print("***** horizontal stacking togather arrays *****")
	print(res)
	
if __name__ == "__main__":

	vertical_stack(2,2)
	print("\n")
	horizontal_stack(2,2)
