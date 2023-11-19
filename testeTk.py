from tkinter import Tk, Button, messagebox

def exibir_caixa_dialogo():
    messagebox.showinfo("Caixa de Diálogo", "Você clicou no botão")

janela = Tk();
janela.title("Exemplo de Janela");
janela.geometry("600x600");

botao = Button(janela, text="Clique em mim!", command=exibir_caixa_dialogo);
botao.pack();


janela.mainloop();