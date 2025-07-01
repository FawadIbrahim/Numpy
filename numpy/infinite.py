import numpy as np
prices=np.array([100,200,np.inf,300,-np.inf])
print(np.isinf(prices))
cleaned=np.nan_to_num(prices, posinf=1000 , neginf=-1000)
print(cleaned)