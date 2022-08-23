import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  list_3d = [] 
  new_list = []
  count = 1
  for n in list:
    new_list.append(n)
    if count % 3 == 0:
      list_3d.append(new_list)
      new_list = []
    count += 1

  arr = np.array(list_3d)
  calculations = {}
  functions = [np.mean, np.var, np.std, np.amax, np.amin, np.sum]
  names = ["mean", "variance", "standard deviation", "max", "min", "sum"]
  for i in range(0, 6):
    axis1 = (functions[i](arr, axis=0)).tolist()
    axis2 = (functions[i](arr, axis=1)).tolist()
    flattened = (functions[i](arr))
    calculations[names[i]] = [axis1, axis2, flattened]
  return calculations