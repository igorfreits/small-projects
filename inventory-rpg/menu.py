from functions import inventory

while True:
    option = int(
        input('\033[36m'
              '[1] - New item'
              '\n[2] - Show inventory'
              '\n[3] - Drop item'
              '\n[4] - Exit'
              '\nchoose option: \033[m'))
    match option:
        case 1:
            inventory.new_item()
        case 2:
            inventory.show_inventory()
        case 3:
            inventory.drop_item()
        case 4:
            break
