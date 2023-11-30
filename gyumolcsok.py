gyumolcsok = ["alma", "körte", "szilva", "narancs", "banán"]


print("Gyümölcsök betűrendben:")
for gyumolcs in sorted(gyumolcsok):
    print(gyumolcs)


print("\nCsak az 'a' betűvel kezdődő gyümölcsök:")
for gyumolcs in gyumolcsok:
    if gyumolcs.startswith("a"):
        print(gyumolcs)

