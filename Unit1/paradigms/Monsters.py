scream = lambda onomatopoeia, intensity, bedwetting: (onomatopoeia, intensity, bedwetting)

kid = lambda name, age, isTall: (name, age, isTall)

energiaDescream = lambda scream: len(scream[0]) * (scream[1] ** 2) if scream[2] else 3 * len(scream[1]) + scream[2]

sullivan = lambda kid: ("A" * len(kid[0] + "GH"), 20 / kid[1], True if kid[1] < 3 else False)

Vocals_Count = lambda chain: chain.count("a") + chain.count("e") + chain.count("i") + chain.count("o") + chain.count("u")

randall = lambda kid: ("¡Mamadera!", Vocals_Count(kid[0]), True if kid[2] > 0.8 and kid[2] < 1.2 else False)

chuck = lambda kid: ("abcdefghijklmnopqrstuvwxyz", 1000, True)

apply = lambda functions, element: list(map(lambda function: function(element), functions))

team= lambda monstruos, kid: apply(monstruos, kid)