import requests
from datetime import datetime
from bs4 import BeautifulSoup


def get_wordle_answer() -> object:
    today_date = datetime.now().strftime("%B-%-d-%Y")

    url = f"https://mashable.com/article/wordle-today-answer-{today_date}"

    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, "html.parser")

    article_content = soup.find("article", class_="mt-8 font-serif editor-content")
    solution_section = article_content.findAll("p")[-4].find("strong").text.strip().replace(".", "")
    solution_section = solution_section.lower()

    return solution_section
