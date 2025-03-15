from fastapi import FastAPI
import random

app = FastAPI()

side_hustle = [
    "Offer freelance services online such as graphic design, web development, or writing.",
    "description Start a blog and monetize it through ads, affiliate marketing, or sponsored posts.",
    "Sell products online without holding inventory by using a dropshipping supplier.",
    "Create and sell custom-designed T-shirts, mugs, and other merchandise through platforms like Printful.",
    "Teach students online or in person in subjects you are skilled in.",
]

money_quote = [
    "Money is a terrible master but an excellent servant.",
    "Too many people spend money they earned to buy things they don’t want to impress people that they don’t like.",
    "An investment in knowledge pays the best interest.",
    "It’s not about how much money you make, but how much money you keep.",
    "Do not save what is left after spending, but spend what is left after saving.",
]


@app.get("/side_hustle")
def get_side_hustle():
    """Return a random hustle idea"""
    return {"side_hustle": random.choice(side_hustle)}

@app.get("/money_quote")
def get_money_quote():
    """Return a random money quote"""
    return {"side_hustle": random.choice(money_quote)}
