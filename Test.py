from Class_Matrices import Linear_Matrices

X = [[1,2104,5,1,45],[1,1416,3,2,40],[1,1534,3,2,30],[1,852,2,1,36]]

X2 = [[1,2104,5,1,45],[1,1416,3,2,40],[1,1534,3,2,30],[1,852,2,1,36]]

Y = [[460],[232],[315],[178]]

X_t_X_inverse = [[16.41,0.007,-2.93,-4.466,-0.263],[-0.01,-0.00001,0.007,0.008,-0.00005], [5.63,0.006,-3.34,-4.06,-0.013],[-0.44,0.001,-0.931,-0.32,0.024], [-0.45,-0.00029,0.1175,0.1468,0.009]]

X_t_X_inverse = Linear_Matrices(X_t_X_inverse)

X = Linear_Matrices(X)

X2 = Linear_Matrices(X2)

Y = Linear_Matrices(Y)

X.transpose()

X_t_Y = X.multiplication(Y)

X_t_Y = Linear_Matrices(X_t_Y)

Beta = X_t_X_inverse.multiplication(X_t_Y)

Beta = Linear_Matrices(Beta)

X1 = [[1,2105,3,2,43]]

X1 = Linear_Matrices(X1)

Pred_Observ = X1.multiplication(Beta)

print(Pred_Observ)