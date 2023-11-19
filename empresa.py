client = {};

print("\n\nSeja bem vindo(a) à Danones Gourmet\n")
print("Vamos iniciar com seu cadastro!\n")

client["name"] = input("Digite seu nome: ");
client["idade"] = input("Digite sua idade: ");
client["sex"] = input("Digite seu sexo (m/f): ");
client["state"] = input("Digite seu estado: ");
client["city"] = input("Digite sua cidade: ");
client["street"] = input("Digite sua rua: ");
client["number"] = input("Digite o número da sua casa: ");

print("\n\n");

for x in client:
  print(f'-{x}: {client.get(x)}');

