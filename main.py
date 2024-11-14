# Local Machine
# --> It works on GCP
# from my_package.math_operations import * 
# import my_package.math_operations as m
# import my_package.string_operations as s
# m.add(1,2,3,4)
# m.multiply(1,2,3)
# print(f"Value of x is {m.x}")

# print(m.power(2,3))
# print(s.reverse("Jatin"))



# chatgpt script 
# --> It works on GCP
# import my_package.math_operations as m
# import my_package.string_operations as s

# def main_function(request):
#     # Sample usage of your package functions
#     a = 10
#     b = 5
#     results = {
#         "Addition": m.add(a, b),  # Fixed reference to function directly in the module
#         "Multiplication": m.multiply(a, b),  # Fixed reference
#         "Power": m.power(a, b),  # Fixed reference
#         "Reverse String": s.reverse("Jatin")  # Correct reference to reverse function
#     }
#     return results

# if __name__ == "__main__":
#     request = None  # You can define the request or pass arguments as needed
#     results = main_function(request)
#     print(results)


# chatgpt2 example
# --> It also works on GCP
from pyspark.sql import SparkSession
import my_package.math_operations as m
import my_package.string_operations as s

def main_function():
    # Sample usage of your package functions
    a = 10
    b = 5
    results = {
        "Addition": m.add(a, b),
        "Multiplication": m.multiply(a, b),
        "Power": m.power(a, b),
        "Reverse String": s.reverse("Jatin")
    }

    # Create a Spark DataFrame to display results
    spark = SparkSession.builder.appName("PackageOperationsJob").getOrCreate()
    
    # Convert results to DataFrame
    df = spark.createDataFrame([(key, value) for key, value in results.items()], ["Operation", "Result"])

    # Show the DataFrame in the console
    df.show()

    return results

if __name__ == "__main__":
    main_function()


# chatgpt 3from pyspark.sql import SparkSession
# --> It works on GCP
# Initialize Spark session
# from pyspark.sql import SparkSession
# spark = SparkSession.builder.appName('HelloWorld').getOrCreate()

# # Print a Hello World message
# print("Hello, World from PySpark!")
# print("Hello, World from PySpark!")
# print("Hello, World from PySpark!")
# print("Hello, World from PySpark!")
# print("Hello, World from PySpark!")
# print("Hello, World from PySpark!")
# print("Hello, World from PySpark!")
# print("Hello, World from PySpark!")
# print("Hello, World from PySpark!")
# print("Hello, World from PySpark!")
# print("Hello, World from PySpark!")
# print("Hello, World from PySpark!")
# print("Hello, World from PySpark!")
# print("Hello, World from PySpark!")
# print("Hello, World from PySpark!")
# print("Hello, World from PySpark!")
# print("Hello, World from PySpark!")
# print("Hello, World from PySpark!")
# print("Hello, World from PySpark!")
# print("Hello, World from PySpark!")
# print("Hello, World from PySpark!")



# Stop the Spark session
# spark.stop()
