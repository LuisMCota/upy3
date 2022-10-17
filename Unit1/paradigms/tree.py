COEFFICIENT = 45

main = lambda species, height, width, vitality: (species, height, width, vitality)

eachTreeisLeafy = lambda eachTree: eachTree[1] > 6 and eachTree[1] < 15 and eachTree[2] > eachTree[1] and eachTree[3] > 1

life_exp= lambda eachTree: eachTree[3] * COEFFICIENT / 2

rain = lambda mm, eachTree: (eachTree[0], eachTree[1] + 1, eachTree[2], eachTree[3] + (eachTree[3] * mm / 100))

hail = lambda eachTree: (eachTree[0], eachTree[1] - 2, eachTree[3], eachTree[4]) if eachTree[1] >= 3 else eachTree

storm = lambda eachTree: hail(rain(100, eachTree))

isGood = lambda eachTree: rain(150, eachTree)[3] > 5

newBaobabeachTree = main("baobab", 5, 10, 1.7)