from model.test import CalcModel


def calc(a, b, c) -> CalcModel:
    '''
    :param a:
    :param b:
    :param c:
    :return:
    '''
    try:
        if c == "+":
            result = a + b
        elif c == "-":
            result = a-b
        elif c == "*":
            result = a * b
        elif c == "/":
            result = a / b
        else:
            result = 0
        return CalcModel(result=result)
    except:
        return CalcModel()