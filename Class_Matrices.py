import copy

class Linear_Matrices:
    def __init__(self,A):
        """
        the object must have a form of vectors,
        so that we could create a matrix object.
        self.row_vectors would hold its row vectors.
        self.col_vectors would hold its column vectors.
        self.dim hold the dimension of the matrix.
        """
        if len(max(A)) != len(min(A)):
            raise ValueError('This matrix is not valid')
        self.row_vectors = []
        self.col_vectors = [[] for j in range(len(max(A)))]
        self.dim = [len(A), len(A[0])]
        if A == [[]]:
            self.dim = [0,0]
        for v in A:
            self.row_vectors.append(v)
            for value_index,value in enumerate(v):
                self.col_vectors[value_index].append(value)

    def validation(self):
        """
        a user would be able to validate a certain matrix.
        :return: if the matrix is valid or not, by checking it dimension and each row vector values.
        """
        for v_index,v in enumerate(self.row_vectors):
            for value in v:
                if isinstance(value,(int,float)) == False:
                    print("This matrix is not a valid matrix,"
                            " not every component is an integer or float.")
                    return False
        if len(v) != self.dim[1]:
            print("This matrix is not valid,"
                    " the vector",v_index+1,"is of different dimension.")
            return False
        print("This matrix is valid")
        return True

    def multiplication(self,matrix):
        """
        multiply each row of the left matrix by each column of right matrix.
        :param matrix: the matrix which would be mupltiplied by user matrix,
        has to be an object too.
        :return: the product of matrix multiplication
        """
        if self.dim[1] == matrix.dim[0]:
            new_matrix_row_vectors = [[] for j in range(self.dim[0])]
            new_matrix_row_index = 0
            for row_vector in self.row_vectors:
                for column_vector in matrix.col_vectors:
                    sum = 0
                    for component_index in range(len(column_vector)):
                        sum += row_vector[component_index] * column_vector[component_index]
                    new_matrix_row_vectors[new_matrix_row_index].append(sum)
                new_matrix_row_index += 1
            return new_matrix_row_vectors
        print("Matrices are not compatible for multiplication,"
              " not valid dimensions")
        return False

    def addition(self,matrix):
        """
        add each row of each matrix with matching row in either matrix.
        :param matrix: the matrix which will be added to self, must be object too!
        :return: the product of adding two matrices
        """
        if self.dim == matrix.dim:
            new_matrix_row_vectors = [[] for j in range(self.dim[0])]
            new_matrix_row_index = 0
            sum = 0
            for self_row_vector,matrix_row_vector in zip(self.row_vectors,matrix.row_vectors):
                for component_index in range(self.dim[1]):
                    sum += self_row_vector[component_index] + matrix_row_vector[component_index]
                    new_matrix_row_vectors[new_matrix_row_index].append(sum)
                    sum = 0
                new_matrix_row_index += 1
            return new_matrix_row_vectors
        print("Matrices are not compatible for addition,"
              " not valid dimensions")
        return False

    def transpose(self):
        """
        :return: transposed matrix
        """
        column = self.col_vectors
        row = self.row_vectors
        self.col_vectors = row
        self.row_vectors = column
        row_dim = self.dim[0]
        col_dim = self.dim[1]
        self.dim[0] = col_dim
        self.dim[1] = row_dim

    def find_trace(self):
        """
        calculates the sum of all diagonal values of matrix only if its a square matrix
        :return: trace = sum of diagonal
        """
        if self.dim[0] == self.dim[1]:
            trace_of_matrix = 0
            for k in range(len(self.row_vectors)):
                trace_of_matrix += self.row_vectors[k][k]
            self.trace = trace_of_matrix
            return trace_of_matrix
        else:
            return False

    def find_rank(self):
        fake_value = self.echelon("row")
        rank_count = 0
        for index in range(len(self.row_echelon)):
            if self.row_echelon[index][index] != 0:
                rank_count += 1
        self.rank = rank_count
        return self.rank

    def echelon(self,column_or_row,operation_log = "No"):
        """
        iterates over each row, and reducts all rows at the same col_index of
        current pivot, until reaches end of matrix (columns wise).
        :param column_or_row = user can ask for column echelon or row echelon of a matrix
        :param operation_log: the user can save the elementary operations used to create the canonical form matrix.
        the second index is the row that the operation was made on, first index is the row performing the operation,
        multiplied by the third index value.
        :return: row/column echelon form
        """
        operations_log = []
        if column_or_row == "row":
            self.row_echelon = copy.deepcopy(self.row_vectors)
            column_or_row = self.row_echelon
        if column_or_row == "column":
            self.col_echelon = copy.deepcopy(self.col_vectors)
            column_or_row = self.col_echelon
        for index,vector in enumerate(column_or_row):
            for reduct_index,reduct_vector in enumerate(column_or_row):
                if index == reduct_index:
                    continue
                value_numerator = reduct_vector[index]
                value_denominator = vector[index]
                if value_denominator == 0 or value_numerator == 0:
                    continue
                for through_index in range(self.dim[1]):
                    reduct_vector[through_index] = -(value_numerator / value_denominator) * vector[through_index] + reduct_vector[through_index]
                operations_log.append([index, reduct_index, -(value_numerator / value_denominator)])
        if operation_log == "Yes":
            return column_or_row, operations_log
        return column_or_row

    def canonical_form(self, column_or_row, operation_log = "No"):
        """
        returns the canonical form of the matrix.
        uses the self.echelon method.
        :param column_or_row: the user can decide if he wants the row or column canonical form.
        :param operation_log: the user can save the elementary operations used to create the canonical form matrix.
        the second index is the row that the operation was made on, first index is the row performing the operation,
        multiplied by the third index value.
        :return: canonical form of the matrix.
        """
        operations_log = []
        self.echelon(column_or_row)
        if column_or_row == "row":
            self.row_canonical = copy.deepcopy(self.row_echelon)
            column_or_row = self.row_canonical
        if column_or_row == "column":
            self.col_canonical = copy.deepcopy(self.col_echelon)
            column_or_row = self.col_canonical
        for vector in column_or_row:
            for value_index,value in enumerate(vector):
                if value != 0:
                    numerator = 1
                    denominator = value
                    operations_log.append([value_index,value_index,(numerator / denominator)])
                    for through_index in range(self.dim[1]):
                        vector[through_index] = (numerator / denominator) * vector[through_index]
                    break
        if operation_log == "Yes":
            return column_or_row, operations_log
        return column_or_row

    def basis(self,column_or_row):
        """
        by using the find_echelon func, we find the echelon form and extract the non-zero vectors, which will
        form the basis (column or row)
        :param column_or_row: the user can choose to extract the row basis or column basis
        :return: row or column basis
        """
        if column_or_row == "row":
            self.echelon("row")
            self.row_basis = []
            for vector in self.row_echelon:
                count = 0
                for value in vector:
                    if value == 0:
                        continue
                    count += 1
                if count >= 1:
                    self.row_basis.append(vector)
            return self.row_basis
        elif column_or_row == "column":
            self.echelon("column")
            self.col_basis = []
            for col_vector in self.col_echelon:
                count = 0
                for value in col_vector:
                    if value == 0:
                        continue
                    count += 1
                if count >= 1:
                    self.col_basis.append(col_vector)
            return self.col_basis

    def determinant(self):
        """
        find the determinant by multiplying the row base of the matrix's diagonal.
        :return: determinant
        """
        if self.dim[0] != self.dim[1]:
            return 0
        matrix = self.echelon("row")
        multi = 1
        index = 0
        for vector in matrix:
            multi = vector[index]*multi
            index += 1
        return multi

    def create_block_matrix(self,B,direction):
        """
        creating block matrix, only if a valid one can be created
        :param B: the matrix which will be added to the main matrix
        :param direction: the user can choose to add the matrix below the main matrix or to its right.
        also gives us the opportunity to validate if the block matrix asked by the user is valid.
        :return: block matrix if valid, False if not valid
        """
        empty_matrix = [[]]
        block_matrix = Linear_Matrices(empty_matrix)
        if self.dim[0] == B.dim[0] and direction == "right":
            block_matrix.col_vectors.clear()
            block_matrix.col_vectors.append(self.col_vectors)
            block_matrix.col_vectors.append(B.col_vectors)
            block_matrix.row_vectors.clear()
            for k in range(len(self.row_vectors)):
                empty_lst = []
                empty_lst.append(self.row_vectors[k])
                empty_lst.append(B.row_vectors[k])
                block_matrix.row_vectors.append(empty_lst)
            return block_matrix
        elif self.dim[1] == B.dim[1] and direction == "down":
            block_matrix.row_vectors.clear()
            block_matrix.row_vectors.append(self.row_vectors)
            block_matrix.row_vectors.append(B.row_vectors)
            block_matrix.col_vectors.clear()
            for k in range(len(self.col_vectors)):
                empty_lst = []
                empty_lst.append(self.col_vectors[k])
                empty_lst.append(B.col_vectors[k])
                block_matrix.col_vectors.append(empty_lst)
            return block_matrix
        else:
            print("Could not create block matrix")
            return False

    def create_I_matrix(self):
        I = [[] for i in range(self.dim[0])]
        for vector_index, vector in enumerate(I):
            for j in range(self.dim[1]):
                if vector_index == j:
                    I[vector_index].append(float(1))
                else:
                    I[vector_index].append(0)
        return I

    def invert(self):
        I = self.create_I_matrix()
        fake, operations_log = self.echelon("row","Yes")
        fake_2, operations_log_canonical = self.canonical_form("row","Yes")
        for record in operations_log_canonical:
            operations_log.append(record)
        for operation in operations_log:
            for rep in range(len(I)):
                if operation[1] == operation[0]:
                    I[operation[1]][rep] = I[operation[1]][rep] * operation[2]
                    continue
                I[operation[1]][rep] = I[operation[1]][rep] + (I[operation[0]][rep] * operation[2])
        self.inverse = I
        return I

    def is_symmetric(self):
        if self.dim[0] == self.dim[1]:
            row_vectors_non_transpose = self.row_vectors
            self.transpose()
            for vector,vector_transpose in zip(row_vectors_non_transpose,self.row_vectors):
                if vector != vector_transpose:
                    self.symmetric = "False"
                    self.transpose()
                    return self.symmetric
            self.symmetric = "True"
            self.transpose()
            return self.symmetric
        self.symmetric = "False"
        return self.symmetric

    def is_diagonal(self):
        if self.dim[0] == self.dim[1]:
            for vector_index,vector in enumerate(self.row_vectors):
                for index in range(len(vector)):
                    if vector_index == index:
                        if vector[index] == 0:
                            self.diagonal = "False"
                            return self.diagonal
                    if vector_index != index:
                        if vector[index] != 0:
                            self.diagonal = "False"
                            return self.diagonal
            self.diagonal = "True"
            return self.diagonal
        self.diagonal = "False"
        return self.diagonal

    def is_orthogonal(self):
        I = self.create_I_matrix()
        matrix = copy.deepcopy(self)
        matrix.transpose()
        if self.multiplication(matrix) == I and matrix.multiplication(self) == I:
            self.orthogonal = True
            return True
        self.orthogonal = False
        return False