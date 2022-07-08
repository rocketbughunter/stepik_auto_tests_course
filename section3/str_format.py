#просто примеры на объединение строк и assert

# объединение строк
print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))

# другой вариант
str1 = "one"
str2 = "two"
str3 = "three"
print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")

def test_input_text(expected_result, actual_result):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"

# поиск подстроки в строке
s = 'My Name is Julia'
if 'Name' in s:
    print('Substring found')
    
# другой вариант поиска
index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')

#сообщения об ошибке если нет подстроки
def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"
