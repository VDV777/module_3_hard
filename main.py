
data_structure = [
  [1, 2, 3,
   [5, 2],
   (9, 12),
   {'one': 11, 'two': 15, 'def': [7, 77]},
   'Hello',
   'World'
   ]
]


def getElementsSum(*args):

    sumElements: int = 0

    for i in args:

        if isinstance(i, list) or isinstance(i, tuple):

            sumElements += getElementsSum(*i)

        elif isinstance(i, dict):

            # print(*i.values())
            sumElements += getElementsSum(*i.values())

        else:

            if isinstance(i, str):
                # print(i.__len__())
                sumElements += i.__len__()
                # print(sumElements)
            else:
                # print(i)
                sumElements += i
                # print(sumElements)

    return sumElements


print(getElementsSum(data_structure))
