import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def copy_image(from_array, to_array):
    f_arr_rows, f_arr_cols = from_array.shape
    t_arr_rows, t_arr_cols = to_array.shape
    updated_array = to_array
    i = 0
    while i < f_arr_rows:
        j = 0
        while j < f_arr_cols:
            updated_array[i][j] = from_array[i][j] | to_array[i][j]
            j += 1
        i += 1
    return updated_array

all_digits = pd.read_csv('d:/pythondata/all_numbers.csv')
x_features = ['c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','c11','c12','c13','c14','c15','c16','c17','c18','c19','c20','c21','c22','c23','c24','c25']
y_label = ['Number']
final_list = []
num_list = []
X = all_digits[x_features]
y = all_digits[y_label]
m = 0
while m < 10:
    image_array = X.loc[m].to_numpy()
    image_array = image_array.reshape(5,5)
    larger_array = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    larger_array = larger_array.reshape(8,8)
    larger_array = copy_image(image_array, larger_array)
    i = 0
    k = 1
    orig_array = larger_array
    while i < 4:
        larger_array = np.roll(orig_array, i, axis=0)
        j = 0
        while j < 3:
            new_array = np.roll(larger_array, j+1, axis=1)
            if k < 10:
                plt.subplot(3,3,k)
                plt.imshow(new_array, cmap=plt.cm.gray)
                new_array1 = new_array.reshape(1,64)
                list1 = new_array1.tolist()
                final_list.extend(list1)
                num_list.append(m)
            j += 1
            k += 1
        i += 1
    m += 1
#   plt.show()
features = ['C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13','C14','C15','C16','C17','C18','C19','C20','C21','C22','C23','C24','C25','C26','C27','C28','C29','C30','C31','C32','C33','C34','C35','C36',
            'C37','C38','C39','C40','C41','C42','C43','C44','C45','C46','C47','C48','C49','C50','C51','C52','C53','C54','C55','C56','C57','C58','C59','C60','C61','C62','C63','C64']
new_df = pd.DataFrame(final_list, columns=features)
new_df['Number'] = num_list
print(new_df)

new_df.to_csv('d:/pythondata/digits_dataset.csv')