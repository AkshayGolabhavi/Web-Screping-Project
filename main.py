import requests
from bs4 import BeautifulSoup

products_to_track = [
    {
        "product_URL" :"https://www.amazon.in/Samsung-Galaxy-M12-Storage-Processor/dp/B08XGDN3TZ/ref=sxin_2_hcs-la-in-1?cv_ct_cx=samsung&dchild=1&keywords=samsumg&pd_rd_i=B08XGDN3TZ&pd_rd_r=38b49bea-2291-4739-bf94-127d8fb986c8&pd_rd_w=zFhv6&pd_rd_wg=Iu5y5&pf_rd_p=b6d118af-97d2-4a68-bf40-4cd2a7c6b3cd&pf_rd_r=8Q1WN3XQDTC2YHF7TWEQ&qid=1623335398&sr=1-1-99b054f1-0e42-4e3b-b375-028105b26bc6",
        "name":"samsung M12",
        "target_price":10500
    },
    {
        "product_URL":"https://www.amazon.in/Samsung-Galaxy-Ocean-128GB-Storage/dp/B07HGGYWL6/ref=sr_1_1_sspa?crid=29M4L4P1V9Q3E&dchild=1&keywords=samsung+m31&qid=1623337325&sprefix=SAM%2Caps%2C570&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExQ1FVQUFKTTlKTlZNJmVuY3J5cHRlZElkPUEwNzI0MDE0MjU4ODZHV0ZLWTVYSSZlbmNyeXB0ZWRBZElkPUEwNTQ1MDgzM1YwWENGMUo3SUFKMyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=",
        "name":"samsung m31",
        "target_price":14500
    },
    {
        "product_URL":"https://www.amazon.in/Test-Exclusive_2020_1180-Multi-3GB-Storage/dp/B089MT34QL/ref=sr_1_4?dchild=1&keywords=oneplus&qid=1623337500&sr=8-4",
        "name":"one pluse 9r",
        "target_price":38000
    },
    {
        "product_URL":"https://www.amazon.in/New-Apple-iPhone-11-128GB/dp/B08L8BQ4H9/ref=sr_1_1_sspa?dchild=1&keywords=apple&qid=1623347567&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExRFROME1HWFNPMFAmZW5jcnlwdGVkSWQ9QTAyNzY4MTQxWFkwUlpZNEFQREdXJmVuY3J5cHRlZEFkSWQ9QTA0ODg5NDUxVDdaWVUwMkdCSjdHJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==",
        "name":"new apple iphone 11",
        "target_price":58000
    },
    {
        "product_URL":"https://www.amazon.in/iQOO-Ace-Black-128GB-Storage/dp/B07WHS6QT7/ref=sr_1_9_sspa?dchild=1&keywords=redmi&qid=1623347748&sr=8-9-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzMlAzNlpYNFVMRjRYJmVuY3J5cHRlZElkPUEwMjYyMzk0RFUxUk5OV1gzSUxaJmVuY3J5cHRlZEFkSWQ9QTA4MDMxODcxRVRIUVk0WjlOQ1RGJndpZGdldE5hbWU9c3BfbXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==",
        "name":"iQoo z3",
        "target_price":20000
    }

]

def give_product_price(URL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0"
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    product_price = soup.find(id="priceblock_dealprice")
    if (product_price == None):
        product_price = soup.find(id="priceblock_ourprice")

    return product_price.getText()[2:]

result_file = open('my_result_file.txt','w')

try:
    for every_product in products_to_track:
        product_price_returned = give_product_price(every_product.get("product_URL"))
        print(product_price_returned + "-" + every_product.get("name"))

        my_product_price = product_price_returned[2:]
        my_product_price = my_product_price.replace(',', '')
        my_product_price = int(float(my_product_price))

        print(my_product_price)

    if my_product_price < every_product.get("target_price"):
        print("available at your required price")
        result_file.write(
            every_product.get("name") + '- \t' + 'available at Target price' + 'current price-' + str(my_product_price)+'\n')

    else:
        print("still at current price")

finally:
    result_file.close()