import requests
import time

user = [
   {
      "email":"afonso.afancar@magazineaziul.com.br",
      "first_name":"Afonso",
      "last_name":"Afancar",
      "password":"123mudar"
   },
   {
      "email":"alceu.andreoli@magazineaziul.com.br",
      "first_name":"Alceu",
      "last_name":"Andreoli",
      "password":"123mudar"
   },
   {
      "email":"amalia.zago@magazineaziul.com.br",
      "first_name":"Amalia",
      "last_name":"Zago",
      "password":"123mudar"
   },
   {
      "email":"carlos.eduardo@magazineaziul.com.br",
      "first_name":"Carlos",
      "last_name":"Eduardo",
      "password":"123mudar"
   },
   {
      "email":"luiz.felipe@magazineaziul.com.br",
      "first_name":"Luiz",
      "last_name":"Felipe",
      "password":"123mudar"
   },
   {
      "email":"breno@magazineaziul.com.br",
      "first_name":"Breno",
      "last_name":"",
      "password":"123mudar"
   },
   {
      "email":"emanuel@magazineaziul.com.br",
      "first_name":"Emanuel",
      "last_name":"",
      "password":"123mudar"
   },
   {
      "email":"ryan@magazineaziul.com.br",
      "first_name":"Ryan",
      "last_name":"",
      "password":"123mudar"
   },
   {
      "email":"vitor.hugo@magazineaziul.com.br",
      "first_name":"Vitor",
      "last_name":"Hugo",
      "password":"123mudar"
   },
   {
      "email":"yuri@magazineaziul.com.br",
      "first_name":"Yuri",
      "last_name":"",
      "password":"123mudar"
   },
   {
      "email":"benjamin@magazineaziul.com.br",
      "first_name":"Benjamin",
      "last_name":"",
      "password":"123mudar"
   },
   {
      "email":"erick@magazineaziul.com.br",
      "first_name":"Erick",
      "last_name":"",
      "password":"123mudar"
   },
   {
      "email":"enzo.gabriel@magazineaziul.com.br",
      "first_name":"Enzo",
      "last_name":"Gabriel",
      "password":"123mudar"
   },
   {
      "email":"fernando@magazineaziul.com.br",
      "first_name":"Fernando",
      "last_name":"",
      "password":"123mudar"
   },
   {
      "email":"joaquim@magazineaziul.com.br",
      "first_name":"Joaquim",
      "last_name":"",
      "password":"123mudar"
   },
   {
      "email":"andre@magazineaziul.com.br",
      "first_name":"André",
      "last_name":"",
      "password":"123mudar"
   },
   {
      "email":"raul@magazineaziul.com.br",
      "first_name":"Raul",
      "last_name":"",
      "password":"123mudar"
   },
   {
      "email":"marcelo@magazineaziul.com.br",
      "first_name":"Marcelo",
      "last_name":"",
      "password":"123mudar"
   },
   {
      "email":"julio.cesar@magazineaziul.com.br",
      "first_name":"Julio",
      "last_name":"Cesar",
      "password":"123mudar"
   },
   {
      "email":"caua@magazineaziul.com.br",
      "first_name":"Caua",
      "last_name":"",
      "password":"123mudar"
   },
   {
      "email":"benicio@magazineaziul.com.br",
      "first_name":"Benicio",
      "last_name":"",
      "password":"123mudar"
   },
   {
      "email":"vitor.gabriel@magazineaziul.com.br",
      "first_name":"Vitor",
      "last_name":"Gabriel",
      "password":"123mudar"
   },
   {
      "email":"augusto@magazineaziul.com.br",
      "first_name":"Augusto",
      "last_name":"",
      "password":"123mudar"
   },
   {
      "email":"pedro.lucas@magazineaziul.com.br",
      "first_name":"Pedro",
      "last_name":"Lucas",
      "password":"123mudar"
   },
   {
      "email":"luiz.gustavo@magazineaziul.com.br",
      "first_name":"Luiz",
      "last_name":"Gustavo",
      "password":"123mudar"
   },
   {
      "email":"giovanni@magazineaziul.com.br",
      "first_name":"Giovanni",
      "last_name":"",
      "password":"123mudar"
   },
   {
      "email":"renato@magazineaziul.com.br",
      "first_name":"Renato",
      "last_name":"",
      "password":"123mudar"
   },
   {
      "email":"diego@magazineaziul.com.br",
      "first_name":"Diego",
      "last_name":"",
      "password":"123mudar"
   },
   {
      "email":"joao.paulo@magazineaziul.com.br",
      "first_name":"Joao",
      "last_name":"Paulo",
      "password":"123mudar"
   },
   {
      "email":"renan@magazineaziul.com.br",
      "first_name":"Renan",
      "last_name":"",
      "password":"123mudar"
   },
   {
      "email":"luiz.fernando@magazineaziul.com.br",
      "first_name":"Luiz",
      "last_name":"Fernando",
      "password":"123mudar"
   },
   {
      "email":"anthony@magazineaziul.com.br",
      "first_name":"Anthony",
      "last_name":"",
      "password":"123mudar"
   },
   {
      "email":"lucas.gabriel@magazineaziul.com.br",
      "first_name":"Lucas",
      "last_name":"Gabriel",
      "password":"123mudar"
   },
   {
      "email":"thales@magazineaziul.com.br",
      "first_name":"Thales",
      "last_name":"",
      "password":"123mudar"
   },
   {
      "email":"luiz.miguel@magazineaziul.com.br",
      "first_name":"Luiz",
      "last_name":"Miguel",
      "password":"123mudar"
   },
   {
      "email":"henry@magazineaziul.com.br",
      "first_name":"Henry",
      "last_name":"",
      "password":"123mudar"
   },
   {
      "email":"marcos.vinicius@magazineaziul.com.br",
      "first_name":"Marcos",
      "last_name":"Vinicius",
      "password":"123mudar"
   },
   {
      "email":"kevin@magazineaziul.com.br",
      "first_name":"Kevin",
      "last_name":"",
      "password":"123mudar"
   },
   {
      "email":"levi@magazineaziul.com.br",
      "first_name":"Levi",
      "last_name":"",
      "password":"123mudar"
   },
   {
      "email":"enrico@magazineaziul.com.br",
      "first_name":"Enrico",
      "last_name":"",
      "password":"123mudar"
   },
   {
      "email":"joao.lucas@magazineaziul.com.br",
      "first_name":"Joao",
      "last_name":"Lucas",
      "password":"123mudar"
   },
   {
      "email":"hugo@magazineaziul.com.br",
      "first_name":"Hugo",
      "last_name":"",
      "password":"123mudar"
   },
   {
      "email":"luiz.guilherme@magazineaziul.com.br",
      "first_name":"Luiz",
      "last_name":"Guilherme",
      "password":"123mudar"
   },
   {
      "email":"matheus.henrique@magazineaziul.com.br",
      "first_name":"Matheus",
      "last_name":"Henrique",
      "password":"123mudar"
   },
   {
      "email":"miguel@magazineaziul.com.br",
      "first_name":"Miguel",
      "last_name":"",
      "password":"123mudar"
   },
   {
      "email":"davi@magazineaziul.com.br",
      "first_name":"Davi",
      "last_name":"",
      "password":"123mudar"
   },
   {
      "email":"gabriel@magazineaziul.com.br",
      "first_name":"Gabriel",
      "last_name":"",
      "password":"123mudar"
   },
   {
      "email":"arthur@magazineaziul.com.br",
      "first_name":"Arthur",
      "last_name":"",
      "password":"123mudar"
   },
   {
      "email":"lucas@magazineaziul.com.br",
      "first_name":"Lucas",
      "last_name":"",
      "password":"123mudar"
   },
   {
      "email":"matheus@magazineaziul.com.br",
      "first_name":"Matheus",
      "last_name":"",
      "password":"123mudar"
   },
   {
      "email": "ronaldinho.gaucho@magazineaziul.com.br",
      "first_name": "Ronaldinho",
      "last_name": "Gaucho",
      "password": "123mudar",
   },
   {
      "email": "roberto.firmino@magazineaziul.com.br",
      "first_name": "Roberto",
      "last_name": "Firmino",
      "password": "123mudar",
   },
   {
      "email": "alex.de.souza@magazineaziul.com.br",
      "first_name": "Alex",
      "last_name": "de Souza",
      "password": "123mudar",
   },
   {
      "email": "ricardo.goulart@magazineaziul.com.br",
      "first_name": "Ricardo",
      "last_name": "Goulart",
      "password": "123mudar",
   },
   {
      "email": "dejan.petkovic@magazineaziul.com.br",
      "first_name": "Dejan",
      "last_name": "Petkovic",
      "password": "123mudar",
   },
   {
      "email": "deyverson.acosta@magazineaziul.com.br",
      "first_name": "Deyverson",
      "last_name": "Acosta",
      "password": "123mudar",
   },
   {
      "email": "harlei.silva@magazineaziul.com.br",
      "first_name": "Harlei",
      "last_name": "Silva",
      "password": "123mudar",
   },
   {
      "email": "walter.henrique@magazineaziul.com.br",
      "first_name": "Walter",
      "last_name": "Henrique",
      "password": "123mudar",
   },
   {
      "email": "francoaldo.souza@magazineaziul.com.br",
      "first_name": "Fracoaldo",
      "last_name": "Souza",
      "password": "123mudar",
   },
   {
      "email": "romario.faria@magazineaziul.com.br",
      "first_name": "Romário",
      "last_name": "Faria",
      "password": "123mudar",
   }
   
]



   
url = "http://127.0.0.1:8000/api/v1/accounts/register/"
print(f"Quantidade de itens na lista: {len(user)}")

for item in user:
   response = requests.post(url, json=item)
   if response.status_code == 201:
      print(f"usuário {item['email']} adicionado com sucesso")
   else:
      print(f"Erro ao adicionar o usuário {item['email']}: {response.content}")