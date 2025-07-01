import numpy as np
prices=np.array([100,200,np.nan,300,np.nan])
# print(np.isnan(prices))
cleaned=np.nan_to_num(prices, nan=400)
print(cleaned)