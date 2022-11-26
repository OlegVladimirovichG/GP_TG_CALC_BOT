def poly_init(user_data):
    first = read_polynomial(user_data['first_poly'])
    second = read_polynomial(user_data['second_poly'])
    merged = merge_dicts(first, second)
    lst = dict_to_list(merged)
    res = write_polynomial(lst)
    return res


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


def merge_dicts(fst, snd):
    fst_dict = {i: fst[i] if i not in snd else fst[i] + snd[i] for i in fst}
    snd_dict = {i: snd[i] for i in snd if i not in fst_dict}
    dict_sum = fst_dict | snd_dict
    return dict_sum


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
    if all(j == 0 for j in exp_lst):
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
