def no_repeat(data: list) -> list:
    for i in range(len(data)): 
        try:
            current_number = data[i]
            print(current_number)
        except IndexError:
            return data

        for next_number in data[i+1:]:
            if next_number == current_number:
                data.remove(next_number)

print(no_repeat([0,0,0,1,3,1,2]))
