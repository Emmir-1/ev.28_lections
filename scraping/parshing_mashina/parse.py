from bs4 import BeautifulSoup
import requests
import csv

count = 0
def get_html(url: str) -> str:
    '''Получаем html разметку определенного сайта по url'''
    responce = requests.get(url)
    return responce.text

def get_soup(html: str) -> BeautifulSoup:
    '''Наша функция html разметку и структурирует ее в bs'''
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_last_page(soup: BeautifulSoup) -> int:
    """Функция которая возращает последнию страницу на сайте!"""
    pages = soup.find("ul", class_="pagination").find_all("a", class_="page-link")
    last_page = pages[-1].get("data-page")
    return int(last_page)

def get_data(soup: BeautifulSoup) -> list:
    """Функция парсер, получает нужные данные с сайта mashina.kg и возращает в виде списка"""
    container = soup.find("div", class_="table-view-list")
    cars = container.find_all("div", class_="list-item")
    result = []
    for car in cars:
        name = car.find("h2", class_='name').contents[0].strip()
        try:
            img = car.find("img", class_="lazy-image").get("data-src")
        except:
            img = "No image!"
        price_div = car.find("div", class_="block price")
        price = price_div.find("p").find("strong").text

        # desc1 = car.find("p", class_="year-miles").tetx.strip()
        # desc2 = car.find("p", class_="body-type").tetx.strip()
        # desc3 = car.find("p", class_="volume").tetx.strip()
        # description = f"{desc1} {desc2} {desc3}"
        # print(description)
        ls = ["year-miles", "body-type", "volume"]
        desc = ", ".join(car.find("p", class_=x).text.strip() for x in ls)
        print(desc)
        data = {
            "name":name, 
            "desc":desc,
            "price":price,
            "img":img,
        }
        result.append(data)
    return result
def prepare_csv() -> None:
    """Функция которая подготавливает csv файл!"""
    with open("cars.csv", "w") as file:
        fieldnames = ["№", "Name", "Description", "Price", "Image Url"]
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow({
            "№":"№",
            "Name":"Name",
            "Description":"Discription",
            "Price":"Price",
            "Image Url":"image Url",
        })

count = 1

def write_to_csv(data: dict) -> None:
    """Записывает все данные в csv файл"""
    with open("cars.csv", "a") as file:
        fieldnames = ["№", "Name", "Description", "Price", "Image Url"]
        writer = csv.DictWriter(file, fieldnames)
        global count
        for car in data:
            writer.writerow ({
                "№":count,
                "Name":car["name"],
                "Description":car["desc"],
                "Price":car["price"],
                "Image Url":car["img"],
            })
            count += 1



def main():
    i = 1
    prepare_csv
    while True:
        url = 'https://www.mashina.kg/search/all/?page={i}'
        html = get_html(url)
        soup = get_soup(html)
        last_page = get_last_page(soup)
        data = get_data(soup)
        write_to_csv(data)
        print(f"Спарсили {i}/{last_page} страницу!")
        if i == 15:
            break
        i += 1
main()


