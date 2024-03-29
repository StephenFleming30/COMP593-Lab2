def main():
    about_me = {
        "fullname": "Stephen MacDonald",
        "student_id": 10308012,
        "pizza_toppings": ["PEPPERONI", "SPINACH", "BEEF"],
        "movies": [{"title" :"hacksaw ridge", "genre": "drama"}, 
                   {"title": "plane", "genre": "action"},
                   ]
    }

    about_me["movies"].append({"title": "old dads", "genre": "comedy"})
    pizza_toppings = ("pinnaple", "bacon")
    print_student_id(about_me)
    print_bullet_list(about_me)
    add_pizza_toppings(about_me, pizza_toppings)
    print_bullet_list(about_me)
    list_of_movies_genres(about_me)
    list_of_movie_titles(about_me)

def print_student_id(about_me):
    fullname = about_me["fullname"]
    last_name = about_me["fullname"].split(" ")
    student_id = about_me["student_id"]
    print(f"My name is {fullname}, but you can call me Sir {last_name[0]}.")
    print(f"My student ID is {student_id}.")

def add_pizza_toppings(about_me, pizza_toppings):
    for topping in pizza_toppings:
        about_me["pizza_toppings"].append(topping)
    about_me["pizza_toppings"] = [topping.casefold() for topping in about_me["pizza_toppings"]]
    return about_me["pizza_toppings"]

def print_bullet_list(about_me):
    about_me["pizza_toppings"].sort()
    print("\nMy favourite pizza toppings are:")
    for topping in about_me["pizza_toppings"]:
        print(f"- {topping}")

def list_of_movies_genres(about_me):
    genres = []
    count = 0
    last_genre = about_me["movies"][-1]["genre"]
    for _ in range(len(about_me["movies"]) - 1):
        genres.append(about_me["movies"][count]["genre"])
        count += 1
    print(f"\nI like to watch {', '.join(genres)} and {last_genre}.")

def list_of_movie_titles(about_me):
    titles = []
    count = 0
    last_movie = about_me["movies"][-1]["title"].title()
    for _ in range(len(about_me["movies"]) - 1):
        about_me["movies"][count]["title"] = about_me["movies"][count]["title"].title()
        titles.append(about_me["movies"][count]["title"])
        count += 1
    print(f"\nSome of my favourite movies are {', '.join(titles)} and {last_movie}!")

if __name__ == "__main__":
    main()
