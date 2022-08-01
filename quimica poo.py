from xml.sax import parseString


class quimica:
     #trabajr por el metodo constructor e ingresar los atributos
    def __imit__(self):
        self.nombre=str(input("Ingresar el nombre del elemento:"))
        self.atomico=str(input("ingresar el numero atomico ."))
        self.electronegatividad=int(input("ingresar el numero de electronegatividad:"))
    #realizar los metodos
    def quimcompleto(self):
        self.todo=self.nombre + " "+ self.atomico +" "+  self.electronegatividad
        print ("el nombre completo del atomo es:", self.todo)
    
#crear el objeto
    
#el objeto es una variable que se le asigna la clase
#a esto se le llama instanciar la clase o llamr a la clase

quim= quimica()
#para mostrar los metodos se utiliza el objeto un punto y se llama al METODO
print()
print("los datos son:")
quim.todo()

