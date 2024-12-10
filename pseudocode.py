def find_vertical_seam(self) -> list[int]:

    energy_matrix = self.form_energy_matrix() # create energy matrix
    min_cost_matrix = [] # initialize min_cost_matrix
    min_cost_matrix.append(energy_matrix[0]) # start with first row which will be as is

    for i in range(1, Picture.height(self)):
        min_cost_row = [] # the calculated min energy cost in row i
        for j in range(Picture.width(self)):
            if j == 0: #leftmost
                min_cost_row.append(energy_matrix[i][j] + min(min_cost_matrix[i-1][j:j+2]))
            elif j == Picture.width(self) - 1: #rightmost
                min_cost_row.append(energy_matrix[i][j] + min(min_cost_matrix[i-1][j-1:j+1]))
            else: # everything in between
                min_cost_row.append(energy_matrix[i][j] + min(min_cost_matrix[i-1][j-1:j+2]))
        min_cost_matrix.append(min_cost_row)
    
    vertical_seam = [0 for i in range(Picture.height(self))]
    vertical_seam[-1] = min_cost_matrix[Picture.height(self)-1].index(min(min_cost_matrix[Picture.height(self)-1]))
    for i in range(Picture.height(self)-2, -1, -1):
        j = vertical_seam[i+1]
        if j == 0: # leftmost
            # let a = [0,1,2,3,4], b = a[0:2]
            # b.index() = output will be from 0-1
            # 0 + j = j, or 1 + j
            vertical_seam[i] = min_cost_matrix[i][j:j+2].index(min(min_cost_matrix[i][j:j+2])) + j
        elif j == Picture.width(self)-1: # rightmost
            # let a = [0,1,2,3,4], b = a[3:]
            # b.index() = output will be from 0-1
            # 0 + j - 1 = j - 1, or 1 + j - 1 = j
            vertical_seam[i] = min_cost_matrix[i][j-1:j+1].index(min(min_cost_matrix[i][j-1:j+1])) + j-1
        else: # everything in between
            # let a = [0,1,2,3,4], b = a[1:4]
            # b.index() = output will be from 0-2
            # 0 + j - 1 = j - 1, or 1 + j - 1 = j, 2 + j - 1 = j + 1
            vertical_seam[i] = min_cost_matrix[i][j-1:j+2].index(min(min_cost_matrix[i][j-1:j+2])) + j-1

    return vertical_seam

    raise NotImplementedError