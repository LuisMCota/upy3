class animal():
    def __init__(self, especie, IQ, capabilities):
        self.especie = especie
        self.IQ = IQ
        self.capabilities = capabilities

Exp_1 = animal('Tinto', 100, 'Reflejos de ninja mejorados')
Exp_2 = animal('Shrek', 50, 'Rayos laser por los ojos')

superior_intelligence = int
pinkify = str
super_powers = str

def antropomorfic(IQ):
    if IQ > 60:
        print('Is Anthropomorfic')
    else:
        print('Is not Anthropomorfic')

def pinkiesco(hab_1):

    def vocales(string, vowels): 
        final = [each for each in string if each in vowels] 
        print(len(final)) 
 
    vowels = "AaEeIiOoUu"
    second = hab_1[2:]

    first = hab_1[:2]
    if first == 'do':
        print('True')
    else:
        print('False')


print(antropomorfic(Exp_1.IQ))
print(pinkiesco('d adsn'))

