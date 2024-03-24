def sum_recursive(current_number, accumulated_sum):
    # base case - return the final state
    if current_number == 11:
        return accumulated_sum
    # recursive case - thread the state through the recursive call
    else:
        return sum_recursive(current_number + 1, accumulated_sum + current_number)


print(sum_recursive(1, 0))

# not recommended
current_number = 1
accumulated_sum = 0


def sum_recursive_not_recommended():
    global current_number
    global accumulated_sum
    # base case - return the final state
    if current_number == 11:
        return accumulated_sum
    # recursive case - thread the state through the recursive call
    else:
        accumulated_sum += current_number
        current_number += 1
    return sum_recursive_not_recommended()


print(sum_recursive_not_recommended())
