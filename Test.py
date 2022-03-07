import Class_Matrices
A = [[2,0,0],[0,2,0],[0,0,3]]
B = [[3,4],[6,7],[9,8]]
A = Class_Matrices.Linear_Matrices(A)
B = Class_Matrices.Linear_Matrices(B)
A.is_symmetric()
print(A.symmetric)