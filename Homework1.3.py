def savings_after_months(start_salary, saving_rate, raise_rate, months=36):
    current_savings = 0.0
    annual_salary = start_salary
    monthly_salary = annual_salary / 12

    for month in range(1, months + 1):
        current_savings += current_savings * 0.04 / 12
        current_savings += saving_rate * monthly_salary

        if month % 6 == 0:
            annual_salary = annual_salary + annual_salary * raise_rate
            monthly_salary = annual_salary / 12

    return current_savings


def bisection_search(start_salary):
    low = 0
    high = 10000  
    down_payment = 1000000 * 0.25
    epsilon = 100 
    steps = 0

    if savings_after_months(start_salary, 1, 0.07) < down_payment - epsilon:
        return None, steps

    while low <= high:
        steps += 1
        mid = (low + high) // 2
        rate = mid / 10000
        saved = savings_after_months(start_salary, rate, 0.07)

        if abs(saved - down_payment) <= epsilon:
            return rate, steps
        elif saved < down_payment:
            low = mid + 1
        else:
            high = mid - 1

    return None

def main():
    initial_salary = float(input("Enter the starting salary in Lyon: "))
    result = bisection_search(initial_salary)
    if result[0] is None:
        print("It is not possible to pay the down payment in three years.")
    else:
        rate, step_count = result
        print("Best savings rate: ", rate)
        print("Steps in bisection search:", step_count)


if __name__ == "__main__":
    main()

