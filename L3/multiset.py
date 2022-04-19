class MultiSet(object):
    '''
    **Multiconjunto**

    Un multiconjunto es una modificación del concepto de conjunto 
    en la que se permite la existencia de más de una instancia de 
    cada elemento. Al número de instancias de un elemento dentro 
    de un multiconjunto se le denomina multiplicidad del elemento.

    **Atributos**

    multi_set:
        Representación del multiconjunto mediante un diccionario.
        Las claves del diccionario representan cada elemento del 
        multiconjunto y los valores, el número de instancias de dicho
        elemento.

    **Los multiconjuntos pueden sumarse, restarse y mostrarse por pantalla
    con los operadores habituales +, - y print() respectivamente.**
    '''
    def __init__(self, arg):
        self.multi_set = {}
        if type(arg) is list:
            for elem in arg:
                self.multi_set[elem] = self.multi_set.get(elem, 0) + 1
        elif type(arg) is dict:
            for value in arg.values():
                if not type(value) is int:
                    raise ValueError("Values from your dictionary should be integers")
            self.multi_set = arg
        elif type(arg) is str:
            for char in arg:
                self.multi_set[char] = self.multi_set.get(char, 0) + 1
        else:
            raise ValueError("Arguments to construct a multiset should be list, dictionary or string")
    
    def __repr__(self):
        '''
        Representación del multiconjunto en forma de cadena.
        Esta cadena contendrá un elemento repetido tantas veces
        como su instancias del mismo existan.
        '''
        res = ""
        for key, value in self.multi_set.items():
            res += str(key) * value
        return res

    @classmethod
    def __is_instance(cls, multi_set_1):
        '''
        Lanza una excepción en caso de que el argumento recibido
        no sea una instancia de la clase MultiSet
        '''
        if not isinstance(multi_set_1, MultiSet):
            raise ValueError("Arguments should be Multisets")
    
    @classmethod
    def __are_instances(cls, multi_set_1, multi_set_2):
        if not isinstance(multi_set_1, MultiSet) and not isinstance(multi_set_2, MultiSet):
            raise ValueError("Arguments should be Multisets")

    @classmethod
    def is_included(cls, multi_set_1, multi_set_2):
        '''
        Método de clase que recibe dos multiconjuntos y determina si 
        el primero está incluido en el segundo. Lanza una excepción 
        en caso de que algún argumento no sea un multiconjunto.
        '''
        MultiSet.__are_instances(multi_set_1, multi_set_2)
        for key in multi_set_1.multi_set.keys():
            if multi_set_1.multi_set.get(key) > multi_set_2.multi_set.get(key, 0):
                return False
        return True
    
    @classmethod
    def union(cls, multi_set_1, multi_set_2):
        '''
        Método de clase que calcula la unión de dos multiconjuntos.
        Lanza una excepción en caso de que algún argumento no sea un
        multiconjunto.
        '''
        MultiSet.__are_instances(multi_set_1, multi_set_2)
        res_multi_set = {}
        for key in multi_set_1.multi_set.keys():
            res_multi_set[key] = max(multi_set_1.multi_set.get(key), multi_set_2.multi_set.get(key,  0))
        for key in multi_set_2.multi_set.keys():
            res_multi_set[key] = max(multi_set_2.multi_set.get(key), multi_set_1.multi_set.get(key, 0))
        return MultiSet(res_multi_set)
    
    def __add__(self, other_multi_set):
        '''
        Calcula la adición de un multiconjunto con otro.
        '''
        MultiSet.__is_instance(other_multi_set)
        res_multi_set = {}
        for key in self.multi_set.keys():
            res_multi_set[key] = self.multi_set.get(key) + other_multi_set.multi_set.get(key, 0)
        for key in other_multi_set.multi_set.keys():
            if key not in self.multi_set.keys():
                res_multi_set[key] = other_multi_set.multi_set.get(key) 
        return MultiSet(res_multi_set)
    
    def __sub__(self, other_multi_set):
        '''
        Calcula la sustracción de un multiconjunto con otro.
        '''
        MultiSet.__is_instance(other_multi_set)
        res_multi_set = {}
        for key in self.multi_set.keys():
            res_multi_set[key] = max(self.multi_set.get(key) - other_multi_set.multi_set.get(key, 0), 0)
        return MultiSet(res_multi_set)