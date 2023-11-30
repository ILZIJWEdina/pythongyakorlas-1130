gyumolcsok = []

# Gyümölcsök bekérése a felhasználótól
for i in range(5):
    gyumolcs = input(f"Adja meg a(z) {i + 1}. gyümölcs nevét: ")
    gyumolcsok.append(gyumolcs)

# Gyümölcsök kiírása betűrendben
print("\nGyümölcsök betűrendben:")
for gyumolcs in sorted(gyumolcsok):
    print(gyumolcs)

# Felhasználótól bekért betűvel kezdődő gyümölcsök kiírása
kezdo_betu = input("\nAdja meg a betűt, amivel kezdődő gyümölcsöket szeretne látni: ")
print(f"Gyümölcsök, amik '{kezdo_betu}' betűvel kezdődnek:")
for gyumolcs in gyumolcsok:
    if gyumolcs.startswith(kezdo_betu):
        print(gyumolcs)
