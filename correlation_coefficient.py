def calculate_coefficient(lst1, lst2):
    # Step 1: Calculate the means of both datasets
    mean_data1 = sum(lst1) / len(lst1)
    mean_data2 = sum(lst2) / len(lst2)

    # Step 2: Calculate the deviations of both datasets from their respective means
    deviations_data1 = [x - mean_data1 for x in lst1]
    deviations_data2 = [x - mean_data2 for x in lst2]

    # Step 3: Multiply the deviations of both datasets together and sum them
    sum_of_products_of_deviations = sum([deviations_data1[i] * deviations_data2[i] for i in range(len(lst1))])

    # Step 4: Calculate the square root of the product of the sum of the squared deviations of both datasets
    sum_of_squared_deviations_data1 = sum([(x - mean_data1) ** 2 for x in lst1])
    sum_of_squared_deviations_data2 = sum([(x - mean_data2) ** 2 for x in lst2])
    correlation_coefficient = sum_of_products_of_deviations / ((sum_of_squared_deviations_data1 * sum_of_squared_deviations_data2) ** 0.5)

    print("Correlation coefficient between the two datasets:", correlation_coefficient)

data1 = [32, 45, 39, 43, 58, 84, 65]
data2 = [17, 20, 23, 7, 24, 49, 38]
calculate_coefficient(data1, data2)