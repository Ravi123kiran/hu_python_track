Keys = ['Ten', 'Twenty', 'Thirty']
Values = [10, 20, 30]
result= {}
for key in Keys:
    for value in Values:
        result[key] = value
        Values.remove(value)
        break

print("Resultant dictionary is : " + str(result))
