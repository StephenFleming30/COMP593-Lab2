def main():
    about_me = {
        "fullname": "Stephen MacDonald",
        "student_id": 10308012,
        "pizza_toppings": ["PEPPERONI", "SPINACH", "BEEF"],
        "movies": [{"title" :"hacksaw ridge", "genre": "action"}, 
                   {"title": "plane", "genre": "action"},
                   ]
    }

    about_me["movies"].append({"title": "the hunger games", "genre": "action and adventure"})
    print_student_id(about_me)

def print_student_id(about_me):
    fullname = about_me["fullname"]
    last_name = about_me["fullname"].split(" ")
    student_id = about_me["student_id"]
    print(f"My name is {fullname}, but you can call me Sir {last_name[0]}.")
    print(f"My student ID is {student_id}")

if __name__ == "__main__":
    main()
