import requests
import json


class Iiko:
    login = "874af36d"

    def get_token(self):
        """Получаем токен"""
        inf = {
            "apiLogin": self.login
        }
        url = 'https://api-ru.iiko.services/api/1/access_token'
        token = requests.post(url, json=inf)
        if token.status_code == 200:
            json_object = json.dumps(token.json())
            with open("sample.json", "w") as outfile:
                outfile.write(json_object)
            return 'Token was written'
        else:
            return 'Error', token.status_code

    def read_file(self):
        with open('sample.json', 'r') as openfile:
            json_object = json.load(openfile)
            return json_object

    header = {"Authorization": f"Bearer {read_file(1)['token']}"}
    organization = []
    terminal = []
    customer_cat = {}

    def get_organization(self):
        """Получаем id организации"""
        url = 'https://api-ru.iiko.services/api/1/organizations'
        organization = requests.post(url, headers=self.header, json={})
        if organization.status_code == 200:
            self.organization = organization.json()
            # ['organizations'][0]['id']
            return self.organization
        else:
            return 'Error', organization.status_code

    def get_terminal(self):
        """Получаем id терминала"""
        url = 'https://api-ru.iiko.services/api/1/terminal_groups'
        terminal = requests.post(url, headers=self.header,
                                 json={"organizationIds": [self.organization['organizations'][0]['id']]})
        if terminal.status_code == 200:
            self.terminal = terminal.json()['terminalGroups']
            return self.terminal
        else:
            return 'Error', terminal.status_code

    def get_customer_category(self):  # 2 Получить список категорий товаров
        url = 'https://api-ru.iiko.services/api/1/nomenclature'
        customer_cat = requests.post(url, headers=self.header, json={
            "organizationId": self.terminal[0]['organizationId'],
            "startRevision": 0
        })
        cats = list()
        self.customer_cat = customer_cat.json()
        if customer_cat.status_code == 200:
            for cat in customer_cat.json()['groups']:
                cats.append(cat['name'])
            return cats
        else:
            return 'Error', customer_cat.status_code, customer_cat.json()

    def get_products(self):  # 3 Получить список товаров
        url = 'https://api-ru.iiko.services/api/1/nomenclature'
        customer_prod = requests.post(url, headers=self.header, json={
            "organizationId": self.terminal[0]['organizationId'],
            "startRevision": 0
        })
        prods = list()
        if customer_prod.status_code == 200:
            for cat in customer_prod.json()['products']:
                prods.append(cat['name'])
            return prods
        else:
            return 'Error', customer_prod.status_code, customer_prod.json()

    def create_products(self):  # 4 Создать заказ
        url = 'https://api-ru.iiko.services/api/1/order/create'
        create_prods = requests.post(url, headers=self.header,
                                     json={
                                         "organizationId": self.terminal[0]['organizationId'],
                                         "terminalGroupId": self.terminal[0]['items'][0]['id'],
                                         "order": {
                                             "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
                                             "tableIds": [
                                                 "497f6eca-6276-4993-bfeb-53cbbbba6f08"
                                             ],
                                             "customer": {
                                                 "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
                                                 "name": "Customer",
                                                 "surname": "string",
                                                 "comment": "string",
                                                 "birthdate": "2019-08-24 14:15:22.123",
                                                 "email": "string",
                                                 "shouldReceivePromoActionsInfo": True,
                                                 "gender": "NotSpecified"
                                             },
                                             "phone": "string",
                                             "guestCount": 0,
                                             "guests": {
                                                 "count": 0
                                             },
                                             "tabName": "Product",
                                             "items": [
                                                 {
                                                     "type": "Product",
                                                     'productId': "f28bc0a8-4d1b-4cf1-ad9f-509d54ea06ae",
                                                     "amount": 0,
                                                     "productSizeId": "b4513563-032a-4dbc-8894-4b05c402f7de",
                                                     "comboInformation": {
                                                         "comboId": "1fa22bdf-8ea5-4d3f-a6cf-3abb16e9aa74",
                                                         "comboSourceId": "dd3c663c-f4a0-4960-be17-31d91758b3a4",
                                                         "comboGroupId": "2cb9710d-2ed9-4514-8333-275a9727b4dd"
                                                     },
                                                     "comment": "Coffee"
                                                 }
                                             ],
                                             "combos": [
                                                 {
                                                     "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
                                                     "name": "Coffee",
                                                     "amount": 0,
                                                     "price": 0,
                                                     "sourceId": "797f5a94-3689-4ac8-82fd-d749511ea2b2",
                                                     "programId": "bc59f66b-913a-48ec-ae2b-7ee29d7bcfbb"
                                                 }
                                             ],
                                             "payments": [
                                                 {
                                                     "paymentTypeKind": "Cash",
                                                     "sum": 0,
                                                     "paymentTypeId": "a681b746-24d1-4f1c-aa71-6af3f1e19567",
                                                     "isProcessedExternally": True,
                                                     "paymentAdditionalData": {
                                                         "paymentType":
                                                             {
                                                              "type": "string"

                                                             }
                                                     },
                                                     "isFiscalizedExternally": True
                                                 }
                                             ],
                                             "tips": [
                                                 {
                                                     "paymentTypeKind": "string",
                                                     "tipsTypeId": "e8b7f419-5ea5-4f5b-b897-d30febf1d59c",
                                                     "sum": 0,
                                                     "paymentTypeId": "a681b746-24d1-4f1c-aa71-6af3f1e19567",
                                                     "isProcessedExternally": True,
                                                     "paymentAdditionalData": {
                                                         "type": "string"
                                                     },
                                                     "isFiscalizedExternally": True
                                                 }
                                             ],
                                             "sourceKey": "string",
                                             "discountsInfo": {
                                                 "card": {
                                                     "track": "string"
                                                 },
                                                 "discounts": [
                                                     {
                                                         "type": "string"
                                                     }
                                                 ]
                                             },
                                             "iikoCard5Info": {
                                                 "coupon": "string",
                                                 "applicableManualConditions": [
                                                     "497f6eca-6276-4993-bfeb-53cbbbba6f08"
                                                 ]
                                             },
                                             "orderTypeId": "c21c7b56-cdb7-4141-bc14-77df36146699"
                                         },
                                         "createOrderSettings": {
                                             "transportToFrontTimeout": 0
                                         }
                                     })

        if create_prods.status_code == 200:
            return create_prods
        else:
            return 'Error', create_prods.status_code, create_prods.json()


i = Iiko()

i.get_token() # выключить после первого использования, включить на 1 раз при просрочке токена
i.read_file()
i.get_organization()
i.get_terminal()
i.get_customer_category()
i.get_products()

print(i.organization)
print(i.terminal)
print(i.get_customer_category())
print(i.get_products())

i.create_products()
print(i.create_products())