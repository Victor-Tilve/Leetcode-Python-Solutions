nums = [3,5,4,3,5,8,7,4]


def twosum(nums,target):
    h_nums = [hash(value) for value in nums]
    output = {}
    position = 0
    solutions = []
    evaluated = []

    #creación del diccionario con todos los keys(hash values) y valores
    for value,_hash in zip(nums,h_nums):
        if _hash in output:
            #la tabla hash tiene por cada key un par de valores que corresponden la posición y el valor de un dato especifico en la lista de posibles valores
            output[_hash].append((value, position))
            position += 1
            continue
        output[_hash] = [(value,position)]
        position += 1
    
    #Valido las posibles respuestas que se puedan encontrar dado un target y una lista de numero.
    for key in output:
        _hash = hash(target - output[key][0][0])
        
        if _hash > 0 and _hash in output:
            #Valido la cantidad de valores que se encuentran dentro de un mismo key
            for i in range(len(output[key])):
                for j in range(len(output[_hash])):
                    if key not in evaluated and _hash not in evaluated and output[_hash][j][1] != output[key][i][1]:
                        solutions.append((output[key][i][1],output[_hash][j][1]))
                if _hash not in evaluated:
                    evaluated.append(_hash)
            if key not in evaluated:
                evaluated.append(key)
                    
    if len(solutions) > 0:
        print(solutions)
    else:
        print("No two sum solution")


if __name__ == "__main__":

    twosum(nums,8)