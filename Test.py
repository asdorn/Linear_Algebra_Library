import Class_Matrices
A = [[1,0,0],[0,1,0],[0,0,1]]
B = [[3,4],[6,7],[9,8]]
A = Class_Matrices.Linear_Matrices(A)
B = Class_Matrices.Linear_Matrices(B)
M_A = A.create_block_matrix(B,"right")
M_B = B.create_block_matrix(A,"right")
print(M_A.row_vectors)
print(M_A.is_block_matrix)