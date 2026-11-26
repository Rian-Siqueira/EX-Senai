class Livro:
    def __init__(self,titulo,autor,isbn,disponivel):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = disponivel

    def descrição(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Isbn: {self.isbn}")
        print(f"Disponivel: {self.disponivel}")
       
   
    def devolver(self):
        if  self.disponivel == False:
            print(f"Livro {self.titulo } foi Devolvido")
            self.disponivel = True
        else:
            print("O livro já foi devolvido")
    
    def emprestar(self):
        if self.disponivel == True:
            self.disponivel = False
        else:
            print(f"O Livro {self.titulo} foi Emprestado")

class Usuario:
    def __init__(self,nome,matricula):
        self.nome = nome
        self.matricula = matricula
        self.limite = 1
        self.emprestados = []
    
    def pegar_livro(self,livro):
        if len(self.emprestados) < self.limite:
            livro.emprestar()
            self.emprestados.append(Livro) 
           
class Aluno(Usuario):
    def __init__(self, nome, matricula):
        super().__init__(nome, matricula)
        self.limite = 1
   
class Professor(Usuario):
   def __init__(self, nome, matricula):
       super().__init__(nome, matricula)
       self.limite = 5


L1 = Livro("Tudo e Rio", "Carla Madeira", 302, False)
L2 = Livro("L2", "A2", 304, True)
L3 = Livro("L3", "A3", 301, False)
A1 = Aluno("Rian", 67)
A2 = Aluno("J", 76)



A1.pegar_livro(L1)
L1.devolver()
print("-" * 80)
L2.descrição()

