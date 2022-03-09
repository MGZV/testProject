import requests


def get_access():
    header = {"apiLogin": "874af36d"}
    url = 'https://api-ru.iiko.services/api/1/access_token'
    access = requests.post(url, json=header)
    if access.status_code == 200:
        return access.json()
    else:
        return access.status_code


def get_organization():
    token = get_access()['token']
    header = {"Authorization": f"Bearer {token}"}
    json = { }
    url = 'https://api-ru.iiko.services/api/1/organizations'
    organization = requests.post(url, headers=header, json=json)
    if organization.status_code == 200:
        return organization.json()
    else:
        return 'Error', organization.status_code


def get_terminal():  # 1 Получить список терминалов
    token = get_access()['token']
    header = {"Authorization": f"Bearer {token}"}
    organization = get_organization()['organizations']
    terminal_list = list()
    for org in organization:
        org = [str(org['id'])]
        json = {"organizationIds": org}
        url = 'https://api-ru.iiko.services/api/1/terminal_groups'
        terminal = requests.post(url=url, headers=header, json=json)
        print(terminal.json())
        if terminal.status_code == 200:
            for term in terminal.json()['terminalGroups']:
                print(term)
                terminal_list.append(term['items'][0]['id'])
            return terminal_list
        else:
            return 'Error', terminal.status_code


def get_customer_category():  # 2 Получить список категорий товаров
    token = get_access()['token']
    header = {"Authorization": f"Bearer {token}"}
    organization = get_organization()['organizations']
    for org in organization:
        org = str(org['id'])
        json = {
            "organizationId": org,
            "startRevision": 0
        }
    url = 'https://api-ru.iiko.services/api/1/nomenclature'
    customer_cat = requests.post(url, headers=header, json=json)
    cats = list()
    if customer_cat.status_code == 200:
        for cat in customer_cat.json()['productCategories']:
            cats.append(cat['name'])
        return cats
    else:
        return 'Error', customer_cat.status_code, customer_cat.json()


def get_products():  # 3 Получить список товаров
    token = get_access()['token']
    header = {"Authorization": f"Bearer {token}"}
    organization = get_organization()['organizations']
    for org in organization:
        org = str(org['id'])
        json = {
            "organizationId": org,
            "startRevision": 0
        }
    url = 'https://api-ru.iiko.services/api/1/nomenclature'
    customer_prod = requests.post(url, headers=header, json=json)
    prods = list()
    if customer_prod.status_code == 200:
        for cat in customer_prod.json()['products']:
            prods.append(cat['name'])
        return prods
    else:
        return 'Error', customer_prod.status_code, customer_prod.json()


def create_products():  # 4 Создать заказ
    token = get_access()['token']
    header = {"Authorization": f"Bearer {token}"}
    organization = get_organization()['organizations']
    term = get_terminal()[0]
    for org in organization:
        org = str(org['id'])
        json = {
        "organizationId": org,
        "terminalGroupId": term,
        "order": {
        "id": "",
        "tableIds": [
        ""
        ],
        "customer": {
        "id": "",
        "name": "",
        "surname": "",
        "comment": "",
        "birthdate": "2021-08-24 14:15:22.123",
        "email": "",
        "shouldReceivePromoActionsInfo": True,
        "gender": ""
        },
        "phone": "",
        "guestCount": 0,
        "guests": {
        "count": 0
        },
        "tabName": "",
        "items": [
        {
        "type": "",
        "amount": 0,
        "productSizeId": "",
        "comboInformation": {
        "comboId": "4",
        "comboSourceId": "",
        "comboGroupId": ""
        },
        "comment": ""
        }
        ],
        "combos": [
        {
        "id": "",
        "name": "",
        "amount": 0,
        "price": 0,
        "sourceId": "",
        "programId": ""
        }
        ],
        "payments": [
        {
        "paymentTypeKind": "",
        "sum": 0,
        "paymentTypeId": "",
        "isProcessedExternally": True,
        "paymentAdditionalData": {},
        "isFiscalizedExternally": True
        }
        ],
        "tips": [
        {
        "paymentTypeKind": "",
        "tipsTypeId": "",
        "sum": 0,
        "paymentTypeId": "",
        "isProcessedExternally": True,
        "paymentAdditionalData": {},
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
        "coupon": "",
        "applicableManualConditions": [
        ""
        ]
        },
        "orderTypeId": "9"
        },
        "createOrderSettings": {
        "transportToFrontTimeout": 0
        }
        }
    url = 'https://api-ru.iiko.services/api/1/order/create'
    create_prods = requests.post(url, headers=header, json=json)
    if create_prods.status_code == 200:
        return create_prods
    else:
        return 'Error', create_prods.status_code, create_prods.json()






# result = get_access()
# print(result)
# term_result = get_organization()
# print(term_result)

# term_result = create_products()
# print(term_result)
#
# customer_category = get_customer_category()
# print(customer_category)


# customer_categories = get_customer_category()
# print(customer_categories)

# products = get_products()
# print(products)