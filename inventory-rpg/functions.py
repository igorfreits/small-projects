import mysql.connector


class Connection:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="IGOR4467",
            database="rpg"
        )

        self.cursor = self.db.cursor()

        print("\033[36mWelcome to the inventory RPG!\033[m ")
        print()


class Inventory(Connection):
    def new_item(self):
        nome = input("\033[35mEnter the name of the item: \033[m").title()
        tipo = input("\033[35mEnter the type of the item: \033[m").title()
        classe = input("\033[35mEnter the class of the item: \033[m").title()
        raridade = input("\033[35mEnter the rarity of the item: \033[m").title()
        print()

        if nome == "" or classe == "" or raridade == "":
            print("\033[31mYou must fill all the fields!\033[m")
            print()
            return self.new_item()
        if tipo == '':
            tipo = 'Item'

        create = 'INSERT INTO inventory(name, type, class, rarity) VALUES' \
            f'("{nome}", "{tipo}", "{classe}", "{raridade}")'

        self.cursor.execute(create)
        self.db.commit()

        print(f"\033[32mThe \033[m{nome}\033[32m item was created!\033[m")

    def show_inventory(self):
        self.cursor.execute("SELECT * FROM inventory")
        result = self.cursor.fetchall()

        for row in result:
            print(
                f'\033[35mItem:\033[m{row[1]} - '
                f'\033[35mType:\033[m{row[2]} - '
                f'\033[35mClass:\033[m{row[3]}\033[m')

    def drop_item(self):
        self.cursor.execute("SELECT id, name FROM inventory")
        result = self.cursor.fetchall()
        for row in result:
            print(f'code: {row[0]} - {row[1]}')
        drop = input('select the code: ')

        print(f'\033[32mthe \033[m{row[1]} \033[32mwas item has been deleted\033[m')
        self.cursor.execute('DELETE FROM inventory WHERE id = %s', (drop,))
        self.db.commit()


inventory = Inventory()
