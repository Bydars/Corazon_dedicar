import time

class C:
    R = '\x1b[0;31;50m'
    BR = '\x1b[1;31;50m'
    N = '\x1b[0m'

def c_():
    with open('heart.txt', 'r', encoding='utf-8') as f:
        return f.read()

def r_(n):
    h = c_()
    l = list(n)
    i = 0
    while '@' in h:
        h = h.replace('@', l[i % len(l)], 1)
        i += 1
    return h

def m():
    n = input("Nombre de tu persona especial: ").strip() or "Amor"
    h = r_(n)

    print(f"\n{C.BR}❤️ Formando corazón... {C.N}\n")
    for ln in h.split('\n'):
        if ln.strip():
            print(f"{C.R}{ln}{C.N}")
            time.sleep(0.3)

    print(f"\n{C.BR}💌 ¡Listo, {n}! 💌{C.N}\n")

if __name__ == '__main__':
    m()
