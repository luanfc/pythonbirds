class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__=='__main__':
    renzo = Pessoa(nome='Renzo')
    p = Pessoa(renzo, nome='Luan')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    for filho in p.filhos:
        print(filho.nome)
    p.sobrenome = 'Carvalho'
    del p.idade
    p.olhos = 1
    del p.olhos
    print(p.__dict__)
    print(renzo.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(p.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(p.olhos), id(renzo.olhos))
