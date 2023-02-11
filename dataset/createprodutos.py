import requests

produtos = [
   {
      "nome":"Liquidificador",
      "descricao":"Liquidificador potente com capacidade de 1,5 litros",
      "preco":99.99,
      "estoque":20
   },
   {
      "nome":"Fogão",
      "descricao":"Fogão a gás de 4 bocas com forno elétrico",
      "preco":479.99,
      "estoque":15
   },
   {
      "nome":"Geladeira",
      "descricao":"Geladeira frost free com capacidade de 500 litros",
      "preco":999.99,
      "estoque":10
   },
   {
      "nome":"Microondas",
      "descricao":"Microondas de 20 litros com grill",
      "preco":199.99,
      "estoque":30
   },
   {
      "nome":"Ar condicionado",
      "descricao":"Ar condicionado split 9000 BTUs",
      "preco":699.99,
      "estoque":25
   },
   {
      "nome":"Lavadora de roupa",
      "descricao":"Lavadora de roupa de 10 kg com agitação pulsativa",
      "preco":799.99,
      "estoque":20
   },
   {
      "nome":"TV",
      "descricao":"TV LED de 50 polegadas",
      "preco":1499.99,
      "estoque":15
   },
   {
      "nome":"Aspirador de pó",
      "descricao":"Aspirador de pó potente com filtro HEPA",
      "preco":199.99,
      "estoque":25
   },
   {
      "nome":"Ferro de passar roupa",
      "descricao":"Ferro de passar roupa com potência de 2200W",
      "preco":49.99,
      "estoque":30
   },
   {
      "nome":"Secador de cabelo",
      "descricao":"Secador de cabelo de alta potência",
      "preco":89.99,
      "estoque":20
   }
]

url = "http://127.0.0.1:8000/api/v1/operational/products/"

for produto in produtos:
    response = requests.post(url, json=produto)
    if response.status_code == 201:
        print(f"Produto {produto['nome']} adicionado com sucesso")
    else:
        print(f"Erro ao adicionar o produto {produto['nome']}: {response.content}")