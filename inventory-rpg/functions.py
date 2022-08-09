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
        nome = input("\033[35mEnter the name of the item: \033[m")
        tipo = input("\033[35mEnter the type of the item: \033[m")
        classe = input("\033[35mEnter the class of the item: \033[m")
        raridade = input("\033[35mEnter the rarity of the item: \033[m")
        print()

        if nome == "" or classe == "" or raridade == "":
            print("\033[31mYou must fill all the fields!\033[m")
            print()
            return self.new_item()
        if tipo == '':
            tipo = 'item'

        create = 'INSERT INTO inventory(name, type, class, rarity) VALUES' \
            f'("{nome}", "{tipo}", "{classe}", "{raridade}")'

        self.cursor.execute(create)
        self.db.commit()

        print("\033[32mItem created!\033[m")

    def show_inventory(self):
        self.cursor.execute("SELECT * FROM inventory")
        result = self.cursor.fetchall()

        for row in result:
            print(row)


inventory = Inventory()
