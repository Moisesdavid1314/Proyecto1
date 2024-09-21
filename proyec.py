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
        if ronda == 3:
            d = suertes(50)
            if d == 'suerte':
                print(
                    f'EL ENEMIGO {self.nombre} SE EMPODERA AUMENTANDO SU VIDA EN {self.vida*1.5}')
                self.vida += self.vida*1.5
                tm.sleep(3)
                print(f'su vida ahora aumenta a {self.vida}')
                tm.sleep(2.5)
        if self.nombre == 'titan macizo con pampel cagao de lo adove' and ronda > 4:
            t = suertes(55)
            if t == 'suerte':
                print(
                    'EL TITAN SE QUILLA Y DA UN GOLPE DEL DIABLO QUE SE TE HUNDE EL ANO PLAAAAA')
                print(F'SU ATAQUE AUMENTA A {self.atack*1.5}')
                self.atack *= 1.5

    def ver_estadisticas_enemigas(self):
        print(
            f'Vida:{self.vida}\nAtaque:{self.atack}\nArmadura:{self.armadura}\nNombre:{self.nombre}\n')
        tm.sleep(5.5)

    def regenerar(self, n=None):
        if n == 'Vagur macizo':
            if suertes(35) == 'suerte':
                if suertes(25) == 'suerte':
                    self.nombre += ' nivel 3'
                    self.vida = 155
                else:
                    self.nombre += ' nivel 2'
                    self.vida = 125
            else:
                self.nombre = 'Vagur macizo'
                self.vida = 95
        elif n == 'titan macizo con pampel cagao de lo adove':
            if suertes(25) == 'suerte':
                if suertes(15) == 'suerte':
                    self.nombre = n+' nivel 3'
                    self.vida = 185
                    self.atack = 41
                else:
                    self.nombre = n+' nivel 2'
                    self.vida = 145
                    self.atack = 38
            else:
                self.nombre = 'titan macizo con pampel cagao de lo adove'
                self.vida = 110
                self.atack = 35

    def loot(self):
        if suertes(50) == 'suerte':
            if suertes(25) == 'suerte':
                if suertes(5) == 'suerte' and self.nombre == 'titan macizo con pampel cagao de lo adove nivel 3':
                    return {'la AVASALLADORA': 80}
                else:
                    ws = rd.randrange(1, 4)
                    loot1 = [[1, {'espada aniquiladora': 55}], [
                        2, {'destruye anos': 62}], [3, {'abanico filoso': 69.5}]]
                for t, s in loot1:
                    if t == ws:
                        print(f'te solto {s}')
                        personaje.inventario(arma=s)
                        break

            else:
                ws = rd.randrange(1, 4)
                loot1 = [[1, {'espada mojonica': 35}], [
                    2, {'lazo con olor a culo': 37}], [3, {'lanza despellejaora': 40}]]
                for t, s in loot1:
                    if t == ws:
                        print(f'te solto {s}')
                        personaje.inventario(arma=s)
                        break
        else:
            ws = rd.randrange(1, 4)
            loot1 = [[1, {'pocion de vida normal': 80}], [
                2, {'pocion de vida mayor': 110}], [3, {'antidoto': 'cura'}]]
            for t, s in loot1:
                if t == ws:
                    print(f'te solto {s}')
                    personaje.utensilios(ute=s)
                    break


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
    def __init__(self, vida, ataque, suerte, defensa, mochila, habilidad, estados, experiencia, sani, mana, lim, utensilios, vida_max):
        self.vida = vida
        self.ataque = ataque
        self.suerte = suerte
        self.defensa = defensa
        self.mochila = mochila
        self.habilidad = habilidad
        self.estado = estados
        self.exp = experiencia
        self.sanidad = sani
        self.mana = mana
        self.lim = lim
        self.ute = utensilios
        self.maxv = vida_max

    def subir_nivel(self):
        while True:
            if self.exp > 99:
                nivel = input(
                    'que estadisticas deseas subir\n1.Suerte + 5\n2.Armadura + 1\n3.Limite Mana:+20\n4.Limite Vida + 10\n')
                tm.sleep(1)
                if nivel == '1':
                    self.suerte += 5
                    self.exp -= 100
                    print(f'ahora tienes {self.suerte} de suerte\n')
                    tm.sleep(3)
                elif nivel == '2':
                    self.defensa += 1
                    self.exp -= 100
                    print(f'ahora tienes {self.defensa} de defensa\n')
                elif nivel == '3':
                    self.lim = self.lim+20
                    self.exp -= 100
                    print(f'tu limite de mana aumento a {self.lim}')
                    tm.sleep(3)
                elif nivel == "4":
                    self.max_vida += 10
                    self.exp -= 100
                    print(f"Tu limite de vida aumento a {self.maxv}")
            else:
                print(
                    f'no tienes suficiente experiencia para subir nivel nesesitas un minimo de 100 tienes {self.exp}\n')
                tm.sleep(1)
                break

    def ver_stats(self):
        print('STADISTICAS')
        print(
            f'************\nVida: {self.vida}\nAtaque: {self.ataque}\nSuerte:{self.suerte}\nDefensa: {self.defensa}\nExperiencia: {self.exp}\nEstados:{self.estado}\nMana: {self.mana}\nVida Maxima: {self.maxv}')
        print('**************\n')
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
            print(f'ok tu inventario ahora esta  {self.mochila}')
            tm.sleep(1)
        else:
            print(self.mochila)
            tm.sleep(2.5)

    def agarrar_arma(self):
        print('************************')
        print('que arma deseas agarrar'.title())
        listado = []
        for s, t in enumerate(self.mochila):
            print(f'{s}.{t}')
            listado.append([s, t])
        equipo = int(input('elije el arma: '))
        for l, s in listado:
            if equipo == l:
                self.ataque = self.mochila[s]
                print(f'arma {s} equipada')
                print(f'tu ataque ahora es {self.ataque}\n')
                tm.sleep(3)
                break
        else:
            print(f'arma {equipo} no encontrado')
            return personaje.agarrar_arma()

    def salud(self):
        print(f'te queda {self.vida} de vida ')
        tm.sleep(1)

    def golpe(self, golpe):
        if 'raminolis' in personaje.estado:
            self.defensa -= 2
            print('la defensa bajo en 2 por la infeccion de raminolis')
            tm.sleep(1.5)
        golpe -= self.defensa
        self.vida -= golpe
        if self.vida < 1:
            print('PERDISTE')
            tm.sleep(1)
            raise print('GAME OVER')

        else:
            print(f'te hicieron {golpe} de daño')
            return golpe

    def habilidades(self, hab=None, name=None):
        while True:
            if hab:
                self.habilidad.update(hab)
                print(f'habilidad aprendida {name} ')
                break
            else:
                elec = input(
                    f'1.habilidad que deseas utilizar\n2.ver habilidades\n3.volver\n')
                if elec == '2':
                    for x in self.habilidad:
                        print(x)
                if elec == '3':
                    print('ok volveras')
                    tm.sleep(3)
                    break
                if elec == '1':
                    elec2 = input('que habilidad deseas utilizar\n')
                    if elec2 in self.habilidad:
                        if self.mana < 40:
                            print('no tienes suficiente mana')
                            tm.sleep(3)
                            break
                        else:
                            for t in self.habilidad[elec2]:
                                if t[0] == 'O':
                                    print(t)
                                    tm.sleep(4)
                                    self.mana -= 40
                                elif t == 'curar':
                                    personaje.curar(
                                        int(self.habilidad[elec2][2]))

                    else:
                        print(f'la habilidad {elec2} no existe')
                        tm.sleep(1)
                        break
        return print('\n')

    def curar(self, x):
        self.vida += x
        print(f'te curaste {x} de vida')
        tm.sleep(1)

    def estados(self, est=None):
        if est:
            self.estado.update(est)
            for t in est:
                print(f'contuviste {t}')
                tm.sleep(1)
        else:
            if self.estado:
                for s, p in self.estado.items():
                    print(f'{s} te infligio un total de {p} daño \n')
                    self.vida -= p
                    tm.sleep(1)
                self.sanidad += 1
                if self.sanidad == 3:
                    d = (self.estado.popitem())
                    if 'raminolis' in d:
                        print('parte de tu defensa vuelve a la normalidad')
                        self.defensa += 6
                    print(f'el estado {d}')
                    print('ha desaparecido\n')
                    tm.sleep(1)
                    self.sanidad -= 3

    def regenerar_mana(self):
        self.mana += 15
        if self.mana > self.lim:
            self.mana = self.lim
        print(f'tu mana aumento a {self.mana}/{self.lim}')
        tm.sleep(3)

    def utensilios(self, ute=None):
        if ute:
            self.ute.update(ute)
            print(f'{ute} añadido a la bolsa de utensilios\n')
            tm.sleep(2.5)
        else:
            while True:
                utensilios_temp = []
                for r, t in enumerate(self.ute, start=1):
                    print(f'{r}.{t}')
                    utensilios_temp.append((r, t))
                eleccion = (input(
                    'cual deseas utilizar  \nVer:. si desesa ver todos los objetos\nvolver si quiere regresar : '))
                if eleccion == 'ver':
                    print(f'UTENSILIOS: {self.ute}')
                    tm.sleep(1.5)
                    continue
                elif eleccion == 'regresar':
                    print('regresando')
                    tm.sleep(1)
                    break
                for s, p in utensilios_temp:
                    if str(s) == eleccion:
                        if 'pocion' in p:
                            self.vida += self.ute[p]
                            personaje.max_vida()
                            print(f'la {p} te ha curado {self.ute[p]}\n')
                            t = self.ute.pop(p)
                            print(f'elemento eliminado {t}')
                            tm.sleep(1)
                            break
                        elif 'antidoto' in p:
                            t=self.estado.popitem()
                            print(f'el antidoto curo {t}')
                            self.ute.pop(p)
                            tm.sleep(1.5)
                            break
                    else:
                        print('no valido')
    def max_vida(self):
        i = self.maxv
        if self.vida > self.maxv:
            self.vida = self.maxv
            print(f"Alcanzaste el maximo de vida {self.vida}")


nombre_personaje = None
print('un humano despierta su concienta quebrada y su nombre borrado\nquiere dar comienzo a una aventura y se llamara')
while True:
    nombre = input('como se llamara este aventurero: ')
    tm.sleep(1)
    if not nombre.isdigit():
        e = input(f'estas seguro que deseas llamarlo {nombre}: ')
        if e == 'si':
            nombre_personaje = nombre
            print('Bien ahora empieza tu LEYENDA')
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
    tm.sleep(1)
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
            tm.sleep(1)
            continue
    else:
        print('clase no valida')
        tm.sleep(1)
        continue


personaje = Humano(clase[0][1], 8, clase[1][1],
                   clase[2][1], {}, {}, {}, 0, 0, 50, 100, {'pocion de vida': 50}, clase[0][1])
ar = input('con cual arma deseas empezar \n1.cuchillo oxidado\n2.maza con palo podrido\n3.papel de bano cagado\n')
if ar == '1':
    personaje.inventario(arma={'cuchilla oxidada': 24})
    tm.sleep(1)
elif ar == '2':
    personaje.inventario(arma={'maza con palo podrido': 24})
    tm.sleep(1)
elif ar == '3':
    personaje.inventario(arma={'papel cagado': 24})
    tm.sleep(1)
else:
    print('al no elegir correctamente pues corriste como hembra y te encontraste una navaja doblada')
    personaje.inventario(arma={'navaja doblada': 5})
    tm.sleep(1)

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
                        tm.sleep(1)
                        if 'espada tula' not in personaje.mochila:
                            print('CONSEGUISTE ESPADA TULA')
                            tm.sleep(1.5)
                            personaje.inventario(arma={'espada tula': 34})
                            tm.sleep(1)
                            break
                        else:
                            if 'pico acero' not in personaje.mochila:
                                print('felicidades conseguiste picoacero')
                                tm.sleep(1)
                                personaje.inventario(arma={'pico acero': 36})
                                tm.sleep(1)
                                break
                            else:
                                pass
                    else:
                        if 'sangrado' in personaje.estado:
                            print('gusano come nalgas te infecto de raminolis')
                            personaje.estados(est={'raminolis': 8})

                        else:
                            print('te mordio una rata')
                            personaje.estados(est={'sangrado': 3})
                            tm.sleep(1.5)
                            break

                else:
                    print('ok te diste media vuelva')
                    break

        elif opcion1 == 2:
            vagur.regenerar('Vagur macizo')
            print('Te encontraste con un vagur')
            while True:
                if pr % 2 == 0:
                    pelea = input(
                        'empieza el ataque que elijes\n1.atacar\n2.ver tu estado\n3.equipar arma\n4.ver enemigo\n5.Usar habilidad\n6.subir_nivel\n7.Utensilios\n\n ')
                    if pelea == '1':
                        at = personaje.atacar()
                        tm.sleep(1)
                        vagur.golpe_ataque(at)
                        print(f'quitaste un total de {at}\n')
                        personaje.estados()
                        tm.sleep(1.5)
                        personaje.regenerar_mana()
                        if vagur.vida < 1:
                            print('GANASTE\n')
                            print('obtuviste 50 de experiencia\n')
                            personaje.vida += 40
                            personaje.max_vida()
                            personaje.exp += 50
                            x = vagur.loot()
                            personaje.inventario(x)
                            tm.sleep(1)
                            vagur.regenerar()
                            rondas = 0

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
                    elif pelea == '6':
                        personaje.subir_nivel()
                    elif pelea == '7':
                        personaje.utensilios()
                else:
                    at_enemigo = vagur.ataque()
                    personaje.golpe(at_enemigo)
                    personaje.salud()
                    pr += 1
                    rondas += 1
                    vagur.rondas(rondas)
        elif opcion1 == 3:
            if 'sed carmesi' not in personaje.habilidad:
                if suertes(personaje.suerte) == 'suerte':
                    print('aprendiste una habilidad SED CARMESI')
                    personaje.habilidades(hab={'sed carmesi': (
                        'O te encaminas en la oscuridad\nO REY CARMESI DAME DE TU SANGRE', 'curar', '40', 'SED CARMESI')}, name='SED CARMESI')
                    tm.sleep(4)
                else:
                    print('te chupo un gusarapo')
                    personaje.estados(est={'mordedura verde': 5})
            else:
                titan.regenerar('titan macizo con pampel cagao de lo adove')
                print(f'te encontraste con {titan.nombre}')
                while True:
                    if pr % 2 == 0:
                        pelea = input(
                            'empieza el ataque que elijes\n1.atacar\n2.ver tu estado\n3.equipar arma\n4.ver enemigo\n5.Usar habilidad\n6.subir_nivel\n7.utensilios ')
                        if pelea == '1':
                            at = personaje.atacar()
                            tm.sleep(1)
                            titan.golpe_ataque(at)
                            print(f'quitaste un total de {at}')
                            tm.sleep(2.5)
                            personaje.estados()
                            tm.sleep(1.5)
                            personaje.regenerar_mana()
                            if titan.vida < 1:
                                print('GANASTE')
                                tm.sleep(1)
                                personaje.vida += 40
                                personaje.max_vida() 
                                print('Ganaste 120 de exp')
                                personaje.exp += 120
                                tm.sleep(1)
                                y = titan.loot()
                                print(f'el enemigo te solto {y}')
                                personaje.inventario(y)
                                titan.regenerar()
                                rondas = 0

                                break
                            pr += 1

                        elif pelea == '2':
                            personaje.ver_stats()
                        elif pelea == '3':
                            personaje.agarrar_arma()
                        elif pelea == '4':
                            titan.ver_estadisticas_enemigas()
                        elif pelea == '5':
                            personaje.habilidades()
                        elif pelea == '6':
                            personaje.subir_nivel()
                        elif pelea == '7':
                            personaje.utensilios()

                    else:
                        at_enemigo = titan.ataque()
                        personaje.golpe(at_enemigo)
                        personaje.salud()
                        pr += 1
                        rondas += 1
                        titan.rondas(rondas)
