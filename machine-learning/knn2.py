def dist(x1,×2):

return np.sqrt(sum((x1-×2)**2))



# Test Time

def knn (X, Y, queryPoint, k=5):



vals = []

m = X. shape [0]



for i in range(m):

d = dist(queryPoint, X[i])

vals.append( (d, Y [1]))



vals = sorted(vals)

# Nearest/First K points

vals = vals[:k]



vals = np.array (vals)



#print(vals)



new_vals = np. unique(vals [:, 11, return_counts=True)



#print (new_vals)



index = new_vals (1]. argmax ()

pred = new_vals [0] (index]



return pred
