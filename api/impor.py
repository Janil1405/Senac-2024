import requests
import openpyxl 

# url = "https://jsonplaceholder.typicode.com/users"

# responde = requests.get(url)

# print(responde)

# if responde.status_code == 200:
#    users = responde.json()
   
#    workbook = openpyxl.Workbook()
#    sheet = workbook.active
   
#    sheet.append(["ID", "Nome" "Email", "Endereço", "Latitude"])
   
#    for user in users:
#        sheet.append([user["id"], user["name"], user["email"], user["address"]["street"], user["address"]["geo"]["lat"]])

#        workbook.save("vida.xlsx")

#        print("Dados salvos com sucesso!")
# else:
#     print(f"Falha ao obter os dados. Código de status: {responde.status_code}")

url1 = "https://loteriascaixa-api.herokuapp.com/api/megasena"

responde = requests.get(url1)
print(responde)