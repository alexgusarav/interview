class Stack:
    def __init__(self):
        self.init = []

    def isEmpty(self):
        if self.init == []:
            return True
        else:
            return False

    def push(self, simbol):
        self.init.append(simbol)

    def pop(self):
        if self.init != []:
            simbol = self.init[-1]
            del self.init[-1]
            return simbol
        else:
            print('Ошибка! Стек пустой')

    def peek(self):
        if self.init != []:
            return self.init[-1]
        else:
            print('Ошибка! Стек пустой')

    def size(self):
        return len(self.init)


if __name__ == '__main__':
    print('введите строку:')
    stroka = input()
    stack = Stack()
    f = False
    for i in range(len(stroka)):
        if stroka[i] == '(' or stroka[i] == '[' or stroka[i] == '{':
            stack.push(stroka[i])
            continue
        if stroka[i] == ')' or stroka[i] == ']' or stroka[i] == '}':
            if stroka[i] == ')' and stack.peek() == '(':
                stack.pop()
            elif stroka[i] == ']' and stack.peek() == '[':
                stack.pop()
            elif stroka[i] == '}' and stack.peek() == '{':
                stack.pop()
            else:
                f = True
                break
    if stack.size() == 0 and f is not True:
        print('Сбалансировано')
    else:
        print('Несбалансированно')
