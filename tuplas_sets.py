#mas colecciones en python

#tuplas
#(item1, 2, 3)
#listas son mutables
#tuplas inmutables
my_tuple = (1, "dos", 3.1, True)
print(type (my_tuple))
print(my_tuple)
print(my_tuple[0])
print(my_tuple[-1])
#Error
#my_tuple[0]="Algo mas"

# conjuntos sets
# Desordenado
# Mutable
# no permite duplicados
my_set={"Uno","Dos","Tres","Uno"}
print(type(my_set))
print(my_set)
my_set.add(4)
print(my_set)

a={1,2,3,4}
b={3,4,5,6}
print(a.union(b))
print(a.intersection(b))