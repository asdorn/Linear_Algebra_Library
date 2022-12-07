from Class_Matrices import Linear_Matrices
X = [[1,3,7,10,14],[1,4,9,12,15]]
Y = [[232],[300]]

X = Linear_Matrices(X)
Y = Linear_Matrices(Y)

print(X.row_vectors)
X.transpose()
print(X.row_vectors)

X_Y = X.multiplication(Y)
print(X_Y)

###########

X = [[1,2,3],[2,4,6],[3,4,9]]
X = Linear_Matrices(X)
print(X.basis(column_or_row="row"))
print(X.basis(column_or_row="column"))

############
X = [[1,2], [2000,3000]]
Y = [[2,3],[1000,20000]]

X = Linear_Matrices(X)
Y = Linear_Matrices(Y)

print(X.addition(Y))

print(X.invert())
print(Y.invert())

print(Y.canonical_form(column_or_row="row"))

print(X.determinant())
print(Y.determinant())

################
X = [[1,2], [2000,3000]]
Y = [[2,0,0],[0,20000,0],[0,0,-1]]

X = Linear_Matrices(X)
Y = Linear_Matrices(Y)

print(X.is_diagonal())
print(Y.is_diagonal())

print(X.find_rank())
print(Y.find_rank())

print(X.echelon(column_or_row="row"))
print(Y.echelon(column_or_row="column"))

###############
X = [[1,2], [2000,3000]]
Y = [[2,0],[0,20000,30000]]

X = Linear_Matrices(X)
Y = Linear_Matrices(Y)

print(X.create_I_matrix())
print(X.find_trace())