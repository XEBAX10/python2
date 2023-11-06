# My proyect CRUD -> Generar, actualizar, eliminar, buscar
clients = 'Luis, Kevin,'

def create_cliente(client_name) :
    global clients
    if client_name not in clients: #when the client noy found 
        def _add_comma():
         global clients
         clients+=","
         clients += client_name 
    else: 
         print("client already exists {}: ".format(client_name))
    def _add_comma():
           global clients
    clients+=","

def read_client():
   pass

def update_client(client_name, new_client):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name + "," , new_client+",")
    else:
        print("client is not in client list ")
def delete_client():
    global clients
    pass

def _print_welcome():
    print("WELCOME UNIVERSIDAD DEL VALLE -TULUÁ")
    print('*' * 100)
    print("What would you like to do today:")
    print("[C]reate Client o user:")
    print("[R]read Client o user:")
    print("[U]pdate Client o user:")
    print("[D]elete Client o user:")

def _get_client_name(): # la funcion me permite preguntar por el nombre del cliente 
   return input("Type your name client: ")

def _get_list_client_names():
    global clients
    print(clients)

if __name__ == '_main_':
    _print_welcome()
    option = input("type option desired client: ").upper()
   
    if option == "C":
        client_name = _get_client_name
        create_cliente(client_name)
        _get_list_client_names()

    elif option == "R":
       _get_list_client_names

    elif option == "U":
        client_name = _get_client_name()
        if clients in client_name:

         client_name_update = input("What is the update client Name:")
         update_client(client_name, client_name_update)
         _get_list_client_names()

    elif option == "D":
         client_name = _get_client_name
         _get_list_client_names()
    else:
        print("command invalid")


    

