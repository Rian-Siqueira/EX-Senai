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
        print("-" * 80)
   
    def devolver(self):
        if  self.disponivel == False:
            print("Livro Devolvido")
            self.disponivel = True
        else:
            print("O livro já foi devolvido")
    
    def emprestar(self):
        if self.disponivel == True:
            self.disponivel = False
        else:
            print("Livro Emprestado")

class Usuario:
    def __init__(self,nome,matricula):
        self.nome = nome
        self.matricula = matricula
        self.limite = 1
        self.emprestados = []
    
    def pegar_livro(self,Livro):
        if len(self.emprestados) < self.limite:
            Livro.emprestar()
            self.emprestados.append(Livro) 
           

class Aluno(Usuario):
    limite = 2

class Professor(Usuario):
    limite = 5


L1 = Livro("Tudo e Rio", "Carla Madeira", 302, False)




L1.emprestar()
L1.descrição()
L1.devolver()
L1.descrição()


