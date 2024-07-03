# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

one_hot = pd.DataFrame()
one_hot['robot'] = (data['whoAmI'] == 'robot').astype(int)
one_hot['human'] = (data['whoAmI'] == 'human').astype(int)
data_one_hot = pd.concat([data, one_hot], axis=1)
print(data_one_hot.head())