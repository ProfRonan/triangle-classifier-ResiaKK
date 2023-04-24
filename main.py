a = int(input("Digite o primeiro valor:  "))
b = int(input("Digite o primeiro valor:  "))
c = int(input("Digite o primeiro valor:  "))

if a < b + c and b < a + c and c < a + b:
        if a == b == c:
            print("Equilátero")
        elif a != b != c != a:
            print("Escaleno")
        else:
             print("Isósceles")
              
                    
              
              
else:
       print("Não é um triangulo")