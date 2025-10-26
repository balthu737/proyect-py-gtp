import json

class Libro():
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año

    def to_dict(self):
        return{
            "titulo": self.titulo,
            "autor": self.autor.to_dict(),
            "año": self.año
        }

    @classmethod
    def from_dict(cls, data):
        autor = Autor.from_dict(data["autor"])
        return cls(data["titulo"], autor, data["año"])

class Autor():
    def __init__(self, nombre):
        self.nombre = nombre
    def to_dict(self):
        return{
            "autor": self.nombre
        }
    @classmethod
    def from_dict(cls, data):
        return cls(data["autor"])

class Biblioteca():
    def __init__(self):
        self._libros = []

    def añadir_libro(self, libro):
        self._libros.append(libro)
        print(f'Tu libro {libro.titulo} fue añadido correctamente')

    def eliminar_libro(self, titulo):
        encontrado = False
        for libro in self._libros:
            if libro.titulo == titulo:
                self._libros.remove(libro)
                encontrado = True
                print(f'El libro {titulo} fue eliminado correrctamente')
                break
        if encontrado == False:
            print(f'El libro {titulo} no se puedo encontrar, no fue eliminado')

    def listar_libros(self):
        for libro in self._libros:
            print(f'El libro es: {libro.titulo}')  
        # return self._libros

    def buscar_libro(self, titulo):
        encontrado = False
        for libro in self._libros:
            if libro.titulo == titulo:
                encontrado = True
                print(f'''El libro existe y sus datos son,
{libro.titulo} | {libro.autor.nombre} | {libro.año}''')
                break
        if encontrado == False:
            print(f'El libro {titulo} no fue encontrada')

    def guardar_json(self):
        lista = [libro.to_dict() for libro in self._libros]
        with open("biblioteca.json", "w", encoding="utf-8") as archivo:
            json.dump(lista, archivo, ensure_ascii=False, indent=4)
        print("Felicidades, tus libros se guardaron correctamente en tu biblioteca")

    def cargar_json(self):
        with open("biblioteca.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            print(datos)
            self._libros = []
            for dato in datos:
                libro = Libro.from_dict(dato)
                self._libros.append(libro)
            print("Libros cargados correctamente desde el archivo JSON")


autor1 = Autor("Gabriel García Márquez")
autor2 = Autor("J.K. Rowling")
autor3 = Autor("Miguel de Cervantes")
libro1 = Libro("Cien años de soledad", autor1, 1967)
libro2 = Libro("Harry Potter y la piedra filosofal", autor2, 1997)
libro3 = Libro("Don Quijote de la Mancha", autor3, 1605)
biblioteca = Biblioteca()
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)
biblioteca.añadir_libro(libro3)
biblioteca.listar_libros()
biblioteca.buscar_libro("Harry Potter y la piedra filosofal")
biblioteca.guardar_json()
biblioteca.cargar_json()
