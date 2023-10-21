class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right

    def __str__(self):
        return self.left, self.right


def huffman_code_tree(node, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, binString + '0'))
    d.update(huffman_code_tree(r, binString + '1'))
    return d

def make_tree(nodes):
    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        node = NodeTree(key1, key2)
        nodes.append((node, c1 + c2))
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
    return nodes[0][0]

if __name__ == '__main__':
    #Получаем на вход текстовый файл. Пока не знаем для кодирования или декодирования
    input_text= "jh" 
    #Создаём массив частотности встречи каждого символа
    frequency = {}
    #Заполняем этот массив 
    for i in input_text: 
        if i in frequency:
            frequency[i]+=1
    else: 
        frequency[i]=1   

    #Проверяем вывод
    print(frequency)
   #Отсортируем по частотности от самого редкого к самому частому 
    frequency=sorted(frequency.items(), key=lambda item: item[1],reverse=True)
    print(frequency)
    node = make_tree(frequency)
    encoding = huffman_code_tree(node)
    for i in encoding:
        print(f'{i} : {encoding[i]}')

''' Нам нужно отсортировать по возрастанию частотности
Варианты из stack overflow
dict(sorted(x.items(), key=lambda item: item[1]))
{0: 0, 2: 1, 1: 2, 4: 3, 3: 4}


for i in sorted(frequency, key=frequency.get, reverse=True):
    print(i, frequency[i])'''


 