with open('test.log', 'w') as fh:
    fh.write("powitanie\n")
    fh.write("kolejne\n")
    fh.write("jeszcze jedno\n")

with open('test.log', 'w', encoding='utf-8') as file:
    file.write("Radek\n")

    with open('test.log', 'a', encoding='utf-8') as f:
        f.write('dodane\n')
        f.write("dośćdane\n")
        f.write("dośdane\n")
        f.write("dośdanńe\n")

with open('test.log', 'r', encoding='utf-8') as file:
    lines = file.read()

print(lines)
print(type(lines))
