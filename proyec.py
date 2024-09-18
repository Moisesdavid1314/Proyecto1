import random as rd
import time as tm


class enemigos:
    def __init__(self, salud, daño, armor, nombre):
        self.vida = salud
        self.atack = daño
        self.armadura = armor
        self.nombre = nombre

    def ataque(self):
        print(f' y {self.nombre} ataca con un total de {self.atack}')
        tm.sleep(2.5)
        return self.atack

    def golpe_ataque(self, daño):
        self.vida -= daño
        self.vida += self.armadura
        print(f' le quedan {self.vida} de vida  a {self.nombre}')
        tm.sleep(2.5)
        if self.vida < 0:
            return 'derrota'
        else:
            return 'combate'

    def rondas(self, ronda):
        if ronda > 3:
            d = suertes(50)
            if d == 'suerte':
                print(
                    f'EL ENEMIGO {self.nombre} SE EMPODERA AUMENTANDO SU VIDA EN {self.vida*1.5}')
                self.vida += self.vida*1.5
                tm.sleep(3)
                print(f'su vida ahora aumenta a {self.vida}')
                tm.sleep(2.5)
        elif ronda == -95:
            print(
                'EL TITAN SE QUILLA Y DA UN GOLPE DEL DIABLO QUE SE TE HUNDE EL ANO PLAAAAA')
            print(F'SU ATAQUE AUMENTA A {self.atack*1.5}')
            self.atack *= 1.5

    def ver_estadisticas_enemigas(self):
        print(
            f'Vida:{self.vida}\nAtaque:{self.atack}\nArmadura:{self.armadura}\nNombre:{self.nombre}\n')
        tm.sleep(5.5)

    def regenerar(self):
        self.vida += 95


titan = enemigos(
    110, 35, 11, 'titan macizo con pampel cagao de lo adove')
vagur = enemigos(95, 14, 8, 'Vagur macizo')


def suertes(x):
    random_suerte = rd.randrange(1, 95)
    for t in range(x+1):
        random_prueba = rd.randrange(1, 95)
        if random_prueba == random_suerte:
            return 'suerte'
    else:
        return 'normal'


class Humano:
    def __init__(self, vida, ataque, suerte, defensa, mochila, habilidad):
        self.vida = vida
        self.ataque = ataque
        self.suerte = suerte
        self.defensa = defensa
        self.mochila = mochila
        self.habilidad = habilidad

    def ver_stats(self):
        print('STADISTICAS')
        print(
            f'************\nVida:{self.vida}\nAtaque:{self.ataque}\nSuerte:{self.suerte}\nDefensa{self.defensa}')
        print('**************')
        tm.sleep(5.5)

    def atacar(self):
        atacar_enemigo = suertes(self.suerte)
        if atacar_enemigo == 'suerte':
            print('CRITICO')
            tm.sleep(2.5)
            return self.ataque*3
        else:
            return self.ataque

    def inventario(self, arma=None):
        if arma:
            self.mochila.update(arma)
            print(f'ok obtuviste {self.mochila}')
            tm.sleep(2)
        else:
            print(self.mochila)
            tm.sleep(2.5)

    def agarrar_arma(self):
        while True:
            d = self.mochila
            agarrar = input('que arma deseas agarrar: '.title())
            if agarrar in d:
                self.ataque = d[agarrar]
                break
            else:
                print('dicho arma no esta')
                tm.sleep(2.2)
                print(personaje.inventario())
                tm.sleep(2.5)
                continue
        print('arma equipada con exito')
        return f'{agarrar} equipado con exito y su ataque es {d[agarrar]}'

    def salud(self):
        print(f'te queda {self.vida} de vida ')
        tm.sleep(2)

    def golpe(self, golpe):
        if self.vida < 1:
            raise print('perdiste')
        golpe -= self.defensa
        self.vida -= golpe
        print(f'te hicieron {golpe} de daño')
        return golpe

    def habilidades(self, hab=None, name=None):
        while True:
            if hab:
                self.habilidad.update(hab)
                print(f'habilidad aprendida {name} ')
                break
            else:
                elec = input(f'que habilidad deseas utilizar')
                if elec in self.habilidad:
                    for t in self.habilidad[elec]:
                        if t[0] == 'O':
                            print(t)
                            tm.sleep(4)
                        elif t == 'curar':
                            personaje.curar(int(self.habilidad[elec][2]))
                else:
                    print(f'la habilidad {elec} no existe')
                    tm.sleep(2)
                    break
        return print('\n')

    def curar(self, x):
        self.vida += x
        print(f'te curaste {x} de vida')


nombre_personaje = None
print('un humano despierta su concienta quebrada y su nombre borrado\nquiere dar comienzo a una aventura y se llamara')
while True:
    nombre = input('como se llamara este aventurero: ')
    tm.sleep(2)
    if not nombre.isdigit():
        e = input(f'estas seguro que deseas llamarlo {nombre}: ')
        if e == 'si':
            nombre_personaje = nombre
            print('bien ahora empieza tu LEYENDA')
            tm.sleep(3)
            break
        else:
            print('ok')
            tm.sleep(3)
            continue
    else:
        print('vaya nombre de mierda repitelo')
        tm.sleep(3)
        continue
clase = None
while True:
    clases = {'aventurero': [['vida', 95], ['suerte', 25], ['defensa', 8]], 'saqueador': [['vida', 55], [
        'suerte', 45], ['defensa', 10]], 'maton': [['vida', 130], ['suerte', 12], ['defensa', 5]]}
    eleccion = input(
        'que clase deseas elegir \naventurero\nsaqueador\nmaton\n'.title())
    tm.sleep(2)
    if eleccion in clases:
        for t in clases[eleccion]:
            print(t)
        ele = input('estas seguro de tu eleccion? ')
        if ele == 'si':
            tm.sleep(3)
            print('ok buena eleccion')
            clase = clases[eleccion]
            break
        else:
            print('ok')
            tm.sleep(2)
            continue
    else:
        print('clase no valida')
        tm.sleep(2)
        continue


personaje = Humano(clase[0][1], 8, clase[1][1], clase[2][1], {}, {})
ar = input('con cual arma deseas empezar \n1.cuchillo oxidado\n2.maza con palo podrido\n3.papel de bano cagado\n')
if ar == '1':
    personaje.inventario(arma={'cuchilla oxidada': 15})
    tm.sleep(2)
elif ar == '2':
    personaje.inventario(arma={'maza con palo podrido': 11})
    tm.sleep(2)
elif ar == '3':
    personaje.inventario(arma={'papel cagado': 9})
    tm.sleep(2)
else:
    print('al no elegir correctamente pues corriste como hembra y te encontraste una navaja doblada')
    personaje.inventario(arma={'navaja doblada': 8})
    tm.sleep(2)

rondas = 0
pr = 0
sitio = input('donde deseas ir \nfosa\nciudad\ncloaca\n')
if sitio == 'fosa':
    while True:
        print('Estas caminando')
        tm.sleep(5)
        opcion1 = rd.randrange(1, 4)
        if opcion1 == 1:
            while True:
                print('encontraste un cofre')
                e1 = input('deseas abrirlo? ')
                if e1 == 'si':
                    if suertes(personaje.suerte) == 'suerte':
                        print('Bien tuviste un golpe de suerte ')
                        tm.sleep(2)
                        if 'espada tula' not in personaje.mochila:
                            print('CONSEGUISTE ESPADA TULA')
                            tm.sleep(1.5)
                            personaje.inventario(arma={'espada tula': 18})
                            tm.sleep(1)
                            break
                        else:
                            if 'pico acero' not in personaje.mochila:
                                print('felicidades conseguiste picoacero')
                                tm.sleep(2)
                                personaje.inventario(arma={'pico acero': 22})
                                tm.sleep(2)
                                break
                            else:
                                pass
                    else:
                        print('te mordio una rata')
                        print('te hizo 10 de ataque')
                        personaje.golpe(10)
                        break

                else:
                    print('ok te diste media vuelva')
                    break

        elif opcion1 == 2:
            print('Te encontraste con un vagur')
            while True:
                if pr % 2 == 0:
                    pelea = input(
                        'empieza el ataque que elijes\n1.atacar\n2.ver tu estado\n3.equipar arma\n4.ver enemigo\n5.Usar habilidad ')
                    if pelea == '1':
                        at = personaje.atacar()
                        tm.sleep(1)
                        vagur.golpe_ataque(at)
                        print(f'quitaste un total de {at}')
                        tm.sleep(1.5)
                        if vagur.vida < 1:
                            print('ganaste')
                            vagur.regenerar()

                            break
                        pr += 1
                    elif pelea == '2':
                        personaje.ver_stats()
                    elif pelea == '3':
                        personaje.agarrar_arma()
                    elif pelea == '4':
                        vagur.ver_estadisticas_enemigas()
                    elif pelea == '5':
                        personaje.habilidades()

                else:
                    at_enemigo = vagur.ataque()
                    personaje.golpe(at_enemigo)
                    personaje.salud()
                    pr += 1
                    rondas += 1
                    vagur.rondas(rondas)
        elif opcion1 == 3:
            if suertes(personaje.suerte) == 'suerte':
                print('aprendiste una habilidad SED CARMESI')
                personaje.habilidades(hab={'sed carmesi': (
                    'O te encaminas en la oscuridad\nO REY CARMESI DAME DE TU SANGRE', 'curar', '30', 'SED CARMESI')}, name='SED CARMESI')

