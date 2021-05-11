import os


class File:
    def __init__(self):
        self.file = 0
        self.new_string = ''

    def open_file(self, name):
        self.file = open(name + '.txt', 'r')
        read_file = self.file.read()
        decoupage = read_file.split(',')
        self.file.close()    
        return decoupage

    def create_file(self, name, nb_person):
        self.file = open(name + '.txt', 'w')
        self.file.write(str(nb_person) + ',' + '0')
        self.file.close()

    def mod(self, name, new_value):
        self.file = self.open_file(name)
        self.new_file = open(name + '.txt', 'w')
        if name != 'group':
            self.new_string = self.file[0] + ',' + str(new_value)
        else:
            for i in range(len(self.file)):
                self.new_string += self.file[i] + ','
            self.new_string += new_value
        self.new_file.write(self.new_string)
        self.new_file.close()

    def remove(self, name):
        self.new_string = ''
        self.file = self.open_file('group')
        self.new_file = open('group.txt', 'w')
        self.file.remove(name)
        for i in range(len(self.file) - 1):
            self.new_string += self.file[i] + ','
        self.new_string += self.file[-1]
        self.new_file.write(self.new_string)
        self.new_file.close()


class Bank:
    def __init__(self):
        self.gestion_file = File()
        self.list_group = {}
        self.nb_person_total = 0

    def new_group(self, name, nb_person):
        self.list_group[name] = [nb_person, 0]
        self.nb_person_total += nb_person
        self.gestion_file.create_file(name, nb_person)
        self.gestion_file.mod('group', name)


    def set_up(self):
        name = self.gestion_file.open_file('group')
        for i in range(len(name)):
            print(i)
            numbers = self.gestion_file.open_file(str(name[i]))
            self.list_group[str(name[i])] = [int(numbers[0]), float(numbers[1])]
            self.nb_person_total += int(numbers[0])

    def buy(self, name, value):
        part = value / self.nb_person_total
        self.list_group[name][1] -= value
        for person in self.list_group:
            self.list_group[person][1] += part * self.list_group[person][0]
            self.list_group[person][1] = round(self.list_group[person][1], 2) 
            self.gestion_file.mod(person, round(self.list_group[person][1], 2))
    
    def remove(self, name):
        bank.nb_person_total -= bank.list_group[name][0]
        bank.list_group.pop(name)
        print(name)
        self.gestion_file.remove(name)
        print(bank.list_group)



class Menu:
    def __init__(self):
        self.titre = 'compta loki'
        self.pre_select = 0
        self.feat = ['- compte(cpt)', '- ajouter une transaction(buy)', '- ajouter un groupe(add)', '- supprimer un groupe(rm)']
        self.clear = lambda: os.system('clear')

    def home(self):
        self.clear()
        print(self.titre)
        print('')
        for i in self.feat:
            print(i, '\n')
        self.cmd = input('>>> ')
        if self.cmd == 'buy':
            self.menu_buy()
        if self.cmd == 'add':
            self.menu_add()
        if self.cmd == 'rm':
            self.menu_remove()
        if self.cmd == 'cpt':
            self.menu_compte()
        if self.cmd == 'q':
            quit()
        else:
            self.home()

    
    def menu_buy(self):
        self.clear()
        print('compta loki \n')
        print("entrez le nom de l'acheteur et la valeur de l'achat (name,value)\n")
        self.choix = input('>>> ')
        print('')
        self.arg = self.choix.split(',')
        bank.buy(self.arg[0], round(float(self.arg[1]), 2))
        print('{0} à acheté pour {1} €'.format(self.arg[0], self.arg[1]))
        print('\nVoulez-vous rentrer un nouvel achat ? (y/n)\n')
        self.choix = input('>>> ')
        if self.choix == 'y':
            self.menu_buy()
        else:
            self.home()

    def menu_add(self):
        self.clear()
        print('compta loki \n')
        print("entrez le nom du groupe et le nombre de personnes qu'il contient (name,personnes)\n")
        self.choix = input('>>> ')
        self.arg = self.choix.split(',')
        print("\nLe nouveau groupe: '{0}' à été ajouté".format(self.arg[0]))
        bank.new_group(self.arg[0], int(self.arg[1]))
        print('\nVoulez-vous crer un nouveau groupe ? (y/n)\n')
        self.choix = input('>>> ')
        if self.choix == 'y':
            self.menu_add()
        else:
            self.home()

    def menu_remove(self):
        self.clear()
        print('compta loki \n')
        print("entrez le nom du groupe que vous voulez supprimer\n")
        self.arg = input('>>> ')
        print("\nLe groupe: '{0}' à été supprimé".format(self.arg))
        bank.remove(self.arg)
        print('\nVoulez-vous supprimer un autre groupe ? (y/n)\n')
        self.choix = input('>>> ')
        if self.choix == 'y':
            self.menu_remove()()
        else:
            self.home()
        
    def menu_compte(self):
        self.clear()
        print('compta loki \n')
        for j in bank.list_group.keys():
            print("compte de {0}:\n\t- nombre de personnes: {1}\n\t- reste à charge: {2}".format(j, bank.list_group[j][0],bank.list_group[j][1]))
        input('>>> ')
        self.home()

        
bank = Bank()
bank.set_up()
menu = Menu()
menu.home()