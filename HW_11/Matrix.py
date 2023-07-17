class Matrix:
   

    def __init__(self, matrix: list) -> None:
        
        self.matrix = matrix

    def show_matrix(self):
        
        mat = ""
        for i in range(len(self.matrix)):
            mat = mat + '\t'.join(map(str,self.matrix[i])) + "\n"
        return mat
    
    def comparison(self, other):
        
        result = ""
        if self.matrix < other.matrix: result = "Вторая матрица больше первой"
        elif self.matrix > other.matrix: result = "Первая матрица больше второй"
        else: result = "Матрицы равны"
        return result

    def __add__(self, other):
        
        result = []
        nums = []
        for i in range(len(self.matrix)): 
            for j in range(len(self.matrix[i])):
                summa = self.matrix[i][j] + other.matrix[i][j]
                nums.append(summa)
                if len(nums) == len(self.matrix[i]):
                    result.append(nums)
                    nums = []
        return result

if __name__ == "__main__":
    m1 = Matrix([[4, 5, 2], [11, 10, 18], [55, 66, 4]])
    print(m1.show_matrix())
    m2 = Matrix([[40, 24, 10], [78, 22, 33], [7, 2, 3]])
    print(m2.show_matrix())
    ms = m1 + m2
    print(ms)
    m3 = Matrix([[4, 5, 2], [11, 10, 18], [55, 66, 4]])
    m4 = Matrix([[40, 24, 10], [78, 22, 33], [7, 2, 3]])
    mc = m4.comparison(m2)
    print(mc)