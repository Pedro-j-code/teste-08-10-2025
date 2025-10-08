def criar_pessoa(nome: str, idade: int, id: int):
  pessoa = {
      "id": id,
      "nome": nome,
      "idade": idade
  }
  return pessoa
p1 = criar_pessoa("Seya", 20, 1)
p2 = criar_pessoa("Saori", 21, 2)
p3 = criar_pessoa("Carlitos", 39, 3)
print(p1)