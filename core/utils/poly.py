users_data = {'first_poly': '3x14 + 2x12 + 6x11 + 9x10 + 5x9 + 6x8 + 8x7 + x6 + 8x5 + 2x4 + x3 + 3x2 + 10x + 3 = 0',
              'second_poly': '33x14 + 2x13 + 64x12 + 62x11 + 59x10 + 6x9 + 66x8 + 75x7 + 55x6 + 67x5 + 74x4 + 44x3 + 34x2 + 12x + 15 = 0'}


def poly_init(user_data):
    first = read_polynomial(user_data['first_poly'])
    second = read_polynomial(user_data['second_poly'])
    merged = first | second
    lst = dict_to_list(merged)
    return write_polynomial(lst)


def read_polynomial(expr):
    expr_dic = {}
    expr = expr.replace(" = 0", "x0")
    expr_lst = expr.split(" + ")
    for i in range(len(expr_lst)):
        expr_lst[i] = expr_lst[i].split('x')
        if expr_lst[i][0] == "":
            expr_lst[i][0] = 1
        if expr_lst[i][1] == "":
            expr_lst[i][1] = "1"
        expr_dic[int(expr_lst[i][1])] = int(expr_lst[i][0])
    return expr_dic


def dict_to_list(mrgd_dict):
    dict_lst = []
    i = max(mrgd_dict)
    while i >= 0:
        if i not in mrgd_dict:
            dict_lst.append(0)
        else:
            dict_lst.append(mrgd_dict.pop(i))
        i -= 1
    return dict_lst


def write_polynomial(exp_lst):
    result = ""
    sup_chr = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    if all(i == 0 for i in exp_lst):
        result += "0"
    else:
        count = len(exp_lst) - 1
        for i in range(0, len(exp_lst)):
            if exp_lst[i] == 0:  # Проверяем на нулевое значение
                count -= 1
                continue
            if i == 0:
                if exp_lst[i] > 1 or exp_lst[i] < 0:
                    result += str(exp_lst[i])
            elif exp_lst[i] < 0:
                result += str(exp_lst[i])
            elif exp_lst[i] > 0:
                if result != "":
                    result += "+ "
                if exp_lst[i] != 1 or i == len(exp_lst) - 1:
                    result += str(exp_lst[i])
            if i == len(exp_lst) - 2:
                result += "x "
            elif i == len(exp_lst) - 1:
                result += " "
            else:
                result += "x" + str(count).translate(sup_chr) + " "
            count -= 1
        result += "= 0"
    return result
