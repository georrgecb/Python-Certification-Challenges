def problem_dash(number):
    nr_dashes = (len(number) + 2) * "-"
    return nr_dashes

def problem_result(first, op, second):
    if op == "+":
        result = int(first) + int(second)
    else:
        result = int(first) - int(second)
    return result

def problem_small_space(result, dashes):
    result = str(result)
    dashes = str(dashes)
    if len(result) < len(dashes):
        small_space = (len(dashes) - len(result)) * " "
    else:
        small_space = ""
    return small_space

def arithmetic_arranger(problems, answer = None):

    big_space = "    "
    small_space = ""

    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    count_problems = 0

    for problem in problems:

        problem = problem.split()

        first_number = problem[0].strip()
        operator = problem[1].strip()
        second_number = problem[2].strip()

        # Error - Numbers Don't Contain Digits:
        try:
            first_number = int(first_number)
            second_number = int(second_number)
        except:
            return "Error: Numbers must only contain digits."

        first_number = str(first_number)
        second_number = str(second_number)

        if len(first_number) < len(second_number):
            top_space = (len(second_number) - len(first_number) + 2) * " "
            bottom_space = " " # one space
            dashes = problem_dash(second_number)

        elif len(first_number) > len(second_number):
            top_space = "  " # two spaces
            bottom_space = (len(first_number) - len(second_number) + 1) * " "
            dashes = problem_dash(first_number)

        # This applies if both numbers have the same lenght:
        else:
            top_space = "  " # two spaces
            bottom_space = " " # one space
            dashes = problem_dash(first_number)

        line1 += top_space + first_number + big_space
        line2 += operator + bottom_space + second_number + big_space
        line3 += dashes + big_space

        if answer:
            result = problem_result(first_number, operator, second_number)
            small_space = problem_small_space(result, dashes)
            line4 += small_space + str(result) + big_space

        # Error - Too Many Problems:
        count_problems += 1
        if count_problems > 5:
            return "Error: Too many problems."
        else:
            pass

        # Error - Operator Not Appropriate:
        if operator == "+" or operator == "-":
            pass
        else:
            return "Error: Operator must be '+' or '-'."

        # Error - Numbers More Than Four Digits:
        if len(str(first_number)) > 4 or len(str(second_number)) > 4:
            return "Error: Numbers cannot be more than four digits."
        else:
            pass

    if answer:
        arranged_problems = line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip() + "\n" + line4.rstrip()
    else:
        arranged_problems = line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip()

    return arranged_problems