# Passo 1: Definindo a classe base
class BaseClass:
    def __init__(self, value):
        self.value = value

    def display_value(self):
        print(f'Value: {self.value}')

# Passo 2: Função para criar classes dinamicamente
def create_dynamic_class(class_name):
    # Cria uma nova classe dinamicamente
    return type(class_name, (BaseClass,), {})

# Passo 3: Criando novas classes com nomes diferentes
NewClass1 = create_dynamic_class('Teste1')
NewClass2 = create_dynamic_class('Teste2')

print(BaseClass.__name__)
print(NewClass1.__name__)
print(NewClass2.__name__)

# Instanciando e utilizando as novas classes
obj1 = NewClass1(10)
obj2 = NewClass2(20)

obj1.display_value()  # Saída: Value: 10
obj2.display_value()  # Saída: Value: 20
