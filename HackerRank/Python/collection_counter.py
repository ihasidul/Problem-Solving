from collections import Counter


if __name__ == '__main__':
    number_of_shoes = int(input())
    shoes_sizes = Counter(map(int,list(input().strip().split(" "))))
    customers = int(input())
    total_sale = 0 
    for customer in range(customers):
        customer_sale = list(map(int,list(input().strip().split(" "))))

        if shoes_sizes[customer_sale[0]] > 0: 
            shoes_sizes[customer_sale[0]] = shoes_sizes[customer_sale[0]] - 1
            total_sale = total_sale + customer_sale[1]
        else:
            continue

    print(total_sale)
