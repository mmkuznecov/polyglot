import numpy as np
import _pickle as pickle
from dictionary_words import dictio

dictionary = dictio

with open('ru.sent.pkl','rb') as f:
    u = pickle.Unpickler(f,encoding="latin1")
    #u.encoding = 'latin1'
    p = u.load()



first_list_of_words = [i for i in p[0]]
print(first_list_of_words)
print('-----------------------------------------')

#print(first_list_of_words)


items = [i for i in dictionary.keys() if dictionary[i]!='0']
print(items)
print('-----------------------------------------')

list_of_words = first_list_of_words + items

print(list_of_words)

values = [int(dictionary[key]) for key in dictionary.keys() if dictionary[key]!='0']

print(values)
print('-----------------------------------------')

a = p[1].tolist()
a = [i[0] for i in a]

list_of_values = a + values



list_of_values = [[i] for i in list_of_values]

values = np.array(list_of_values)


np.reshape(values,(1,len(values)))

#print(values)

out = (list_of_words,values)

output = open('myfile.pkl', 'wb')
pickle.dump(out, output)
output.close()