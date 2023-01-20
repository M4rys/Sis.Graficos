class Mesa():
    def __init__(self) -> None:
        self.cuboFaces = ((0,3,6,4),(2,5,6,3),(1,2,5,7),(1,0,4,7),(7,4,6,5),(2,3,0,1))
        self.tmesa = ((1,1,1),(1,1,0.97),(1,-1,0.97),(1,-1,1),(-1,1,1),(-1,-1,0.97),(-1,-1,1),(-1,1,0.97))

        self.supD = ((0.96,0.65,0.97),(0.96,0.65,0.9),(0.96,-0.65,0.9),(0.96,-0.65,0.97),(0.9,0.65,0.97),(0.9,-0.65,0.9),(0.9,-0.65,0.97),(0.9,0.65,0.9))
        self.supE = ((-0.96,0.65,0.97),(-0.96,0.65,0.9),(-0.96,-0.65,0.9),(-0.96,-0.65,0.97),(-0.9,0.65,0.97),(-0.9,-0.65,0.9),(-0.9,-0.65,0.97),(-0.9,0.65,0.9))

        self.pernaED = ((0.96,-0.55,0.9),(0.96,0.75,-1),(0.96,0.65,-1),(0.96,-0.65,0.9),(0.9,-0.55,0.9),(0.9,0.65,-1),(0.9,-0.65,0.9),(0.9,0.75,-1))
        self.pernaEE = ((0.96,0.55,0.9),(0.96,-0.75,-1),(0.96,-0.65,-1),(0.96,0.65,0.9),(0.9,0.55,0.9),(0.9,-0.65,-1),(0.9,0.65,0.9),(0.9,-0.75,-1))

        self.pernaDD = ((-0.96,-0.55,0.9),(-0.96,0.75,-1),(-0.96,0.65,-1),(-0.96,-0.65,0.9),(-0.9,-0.55,0.9),(-0.9,0.65,-1),(-0.9,-0.65,0.9),(-0.9,0.75,-1))
        self.pernaDE = ((-0.96,0.55,0.9),(-0.96,-0.75,-1),(-0.96,-0.65,-1),(-0.96,0.65,0.9),(-0.9,0.55,0.9),(-0.9,-0.65,-1),(-0.9,0.65,0.9),(-0.9,-0.75,-1))


    def teste(self, prop, pos) :
        partes = []
        partes.append(self.tmesa) 
        partes.append(self.supD)
        partes.append(self.supE) 
        partes.append(self.pernaED)
        partes.append(self.pernaEE)
        partes.append(self.pernaDD)
        partes.append(self.pernaDE)
             
        axisList = []
        new_partes = []

        for parte in partes:
            for ponto in parte:
                x = ponto[0] * prop[0] + pos[0]
                y = ponto[1] * prop[1] + pos[1]
                z = ponto[2] * prop[2] + pos[2]
                axisList.append((x, y, z))
            new_partes.append((axisList[0], axisList[1], axisList[2], axisList[3], axisList[4], axisList[5], axisList[6], axisList[7]))
            axisList = []
                
        print(new_partes)
mesa =Mesa()

mesa.teste((2,2,2), (2,2,2))