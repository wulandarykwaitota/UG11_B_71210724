def check_data_type(data, data_type):
    if type(data).__name__ == data_type.lower():
        print("Jawaban Anda benar")
        return True
    else:
        print(f"Jawaban Anda salah, seharusnya adalah: {type(data).__name__}")
        return False


print(check_data_type("Kevin", "STr"))
print(check_data_type("Kevin", "str"))
print(check_data_type(12345, "str"))
print(check_data_type("9347", "int"))
print(check_data_type(9876, "int"))