import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

class TabC(customtkinter.CTkTabview):
    count = 0
    def __init__(self, master, titulo, **kwargs):
        super().__init__(master,  **kwargs)
        
    def newTab(self, titulo, vars):
        self.add("No name" if titulo == '' else titulo)
        TabC.count += 1;
        print(f"INSTANCES OF TABS: {TabC.count}")

        self.nome = customtkinter.CTkLabel(self.tab(titulo), text="Nome:")
        self.idade = customtkinter.CTkLabel(self.tab(titulo), text="Idade:")
        self.estado = customtkinter.CTkLabel(self.tab(titulo), text="Estado:")
        self.cidade = customtkinter.CTkLabel(self.tab(titulo), text="Cidade:")
        self.sexo = customtkinter.CTkLabel(self.tab(titulo), text="Gênero:")

        self.nome.grid(row=0, column=0)
        self.idade.grid(row=1, column=0)
        self.estado.grid(row=2, column=0)
        self.cidade.grid(row=3, column=0)
        self.sexo.grid(row=4, column=0)
        
        customtkinter.CTkLabel(self.tab(titulo), text=vars[0].get()).grid(row=0, column=1, padx=(30, 30), sticky='w')
        customtkinter.CTkLabel(self.tab(titulo), text=vars[1].get()).grid(row=1, column=1, padx=(30, 30), sticky='w')
        customtkinter.CTkLabel(self.tab(titulo), text=vars[2].get()).grid(row=2, column=1, padx=(30, 30), sticky='w')
        customtkinter.CTkLabel(self.tab(titulo), text=vars[3].get()).grid(row=3, column=1, padx=(30, 30), sticky='w')
        customtkinter.CTkLabel(self.tab(titulo), text=vars[4].get()).grid(row=4, column=1, padx=(30, 30), sticky='w')
        
class App(customtkinter.CTk):
  def __init__(self):
    super().__init__()

    tabC = TabC(self, "");
    tabC.grid(row=5, columnspan=2)

    self.title("Cadastro de Cliente");
    self.geometry(f'{360}x{540}')
    self.grid_columnconfigure(0, weight=0)
    self.grid_columnconfigure(1, weight=1)

    nome = customtkinter.StringVar(value="")
    idade = customtkinter.StringVar(value="")
    estado = customtkinter.StringVar(value="")
    cidade = customtkinter.StringVar(value="")
    sexoVar = customtkinter.StringVar(value="M")
    vars = []
    vars.append(nome)
    vars.append(idade)
    vars.append(estado)
    vars.append(cidade)
    vars.append(sexoVar)

    customtkinter.CTkLabel(self, text="Nome:").grid(row=0, column=0, padx=(25, 25), sticky='ew')
    customtkinter.CTkLabel(self, text="Idade:").grid(row=1, column=0, padx=(25, 25), sticky='ew')
    customtkinter.CTkLabel(self, text="Estado:").grid(row=2, column=0, padx=(25, 25), sticky='ew')
    customtkinter.CTkLabel(self, text="Cidade:").grid(row=3, column=0, padx=(25, 25), sticky='ew')
    customtkinter.CTkLabel(self, text="Gênero:").grid(row=4, column=0, padx=(25, 25), sticky='ew')

    customtkinter.CTkEntry(self, textvariable=nome).grid(row=0, column=1, padx=(20, 20), pady=5, sticky="ew")
    customtkinter.CTkEntry(self, textvariable=idade).grid(row=1, column=1, padx=(20, 20), pady=5, sticky="ew")
    customtkinter.CTkEntry(self, textvariable=estado).grid(row=2, column=1, padx=(20, 20), pady=5, sticky="ew")
    customtkinter.CTkEntry(self, textvariable=cidade).grid(row=3, column=1, padx=(20, 20), pady=5, sticky="ew")

    
    def sexoSwitchAction():
        print(f"Sexo selecionado: {sexoVar.get()}")
        
    self.sexoSwitch = customtkinter.CTkSwitch(
       self, text="(M/F)", variable=sexoVar, command=sexoSwitchAction, onvalue='F', offvalue='M'
       )
    self.sexoSwitch.grid(row=4, column=1, padx=70, sticky="w");
    #self.sexoText = ctk.CTkLabel(self, text="Gênero").grid(row=4, column=0, padx=20, sticky="w")

    

    def enviarDados():
        empty = False
        for var in vars:
           if var.get() == "":
              empty = True

        if empty:
           print("ALGUM CAMPO ESTÁ VAZIO!")
           return None 
        
        print(f'Nome: {nome.get()}')
        print(f'Idade: {idade.get()}')
        print(f'Estado: {estado.get()}')
        print(f'Cidade: {cidade.get()}')
        print(f'Sexo: {sexoVar.get()}')
        tabC.newTab(nome.get(), vars)
        for var in vars:
           print(var.set(''))
        self.sexoSwitch.deselect();

    customtkinter.CTkButton(self, text="Enviar", command=enviarDados).grid(padx=45, row=7, columnspan=(2))


app = App();
app.mainloop();
