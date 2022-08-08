def arithmetic_arranger(problems, answer=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    # checking problems for errors
    for problem in problems:
        first_operand, operator, second_operand = problem.split(" ")
        if not (operator == '+' or operator == '-'):
            return "Error: Operator must be '+' or '-'."
        if not (first_operand.isdigit() and second_operand.isdigit()):
            return "Error: Numbers must only contain digits."
        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."

    arranged_problems = conversion_rules(problems, answer)
    return arranged_problems


def conversion_rules(problems, answer=False):

    """rules for the conversions"""
    first = ""
    second = ""
    dashes = ""
    sumx = ""
    arranged_problems = ""
    for problem in problems:
        align = 0
        first_operand, operator, second_operand = problem.split(" ")
        arranged_problems = ""
        longest = 0
        longest_operand = ""
        shortest_operand = ""
        sum = ""
        if operator == "+":
            sum = str(int(first_operand) + int(second_operand))
        else:
            sum = str(int(first_operand) - int(second_operand))

        if len(first_operand) > len(second_operand):
            longest = len(first_operand)
            longest_operand = first_operand
            shortest_operand = second_operand
        else:
            longest = len(second_operand)
            longest_operand = second_operand
            shortest_operand = first_operand

        align += longest + 2
        dash = "-" * align
        res = f"{sum: >{align}}"
        if longest_operand == first_operand:
            top = f"{first_operand : >{align}}"
            bottom = f"{operator} {second_operand : >{align - 2}}"
        else:
            top = f"{first_operand : >{align}}"
            bottom = f"{operator} {second_operand}"

        if not problem == problems[-1]:
            first += top + "    "
            second += bottom + "    "
            dashes += dash + "    "
            sumx += res + "    "
        else:
            first += top
            second += bottom
            dashes += dash
            sumx += res
    if answer:
        arranged_problems = first + "\n" + second + "\n" + dashes + "\n" + sumx
    else:
        arranged_problems = first + "\n" + second + "\n" + dashes
    return arranged_problems


#print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))

