import requests
from datetime import datetime
from bs4 import BeautifulSoup


def get_wordle_answer() -> str:
    """ function to retrieve the answer to the wordle puzzle for the current date from the mashable website

        returns:
        * solution (str) wordle answer for the current date
    """

    today_date = datetime.now().strftime("%B-%-d-%Y")

    url = f"https://mashable.com/article/wordle-today-answer-{today_date}"

    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, "html.parser")

    # parse today's wordle answer
    article_content = soup.find("article", class_="mt-8 font-serif editor-content")
    solution_section = article_content.findAll("p")[-4].find("strong").text.strip().replace(".", "")
    solution = solution_section.lower()

    return solution
