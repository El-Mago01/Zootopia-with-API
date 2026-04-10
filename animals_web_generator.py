import os
import data_fetcher

def load_html_file(file_path):
    with open(file_path, "r") as handle:
        return handle.read()

def write_to_new_html_file(content):
    with open("animals.html", "w") as f:
        f.write(content)
        dir_path=os.path.dirname(os.path.realpath(__file__))
        print(f'File stored in: {dir_path}/{f.name}')

def html_if_animal_not_in_DB(user_input):
    animal_repository_str = ''
    animal_repository_str += f'<li class="cards__item">\n'
    animal_repository_str += f'<div class="card__title">\n'
    animal_repository_str += f'<h2>\n'
    animal_repository_str += f'The animal {user_input} does not exist'
    animal_repository_str += f'</div></li>\n'
    animal_repository_str += f'</h2>\n'
    return animal_repository_str

def serialize_animal(animal):
    animal_repository_str=''
    animal_repository_str += f'<li class="cards__item">\n'
    animal_repository_str += f'<div class="card__title">\n'
    if "name" in animal:
        animal_repository_str += f'{animal['name']}</div>\n'
        animal_repository_str += f'<div class="card__text">\n'
        animal_repository_str += f'<ul>\n'
        if "taxonomy" in animal:
            if "scientific_name" in animal["taxonomy"]:
                animal_repository_str += f"<li><strong>Scientific name:</strong> {animal["taxonomy"]["scientific_name"]}</li>\n"
            if "characteristics" in animal:
                if "diet" in animal["characteristics"]:
                    animal_repository_str += f"<li><strong>Diet:</strong> {animal["characteristics"]["diet"]}</li>\n"
            if "locations" in animal:
                animal_repository_str += f"<li><strong>Location:</strong> {animal["locations"][0]}</li>\n"
            if "characteristics" in animal:
                if "type" in animal["characteristics"]:
                    animal_repository_str += f"<li><strong>Type:</strong> {animal["characteristics"]["type"]}</li>\n"
        animal_repository_str+='</li>\n'
        animal_repository_str+='</ul>\n'
    else:
        animal_repository_str="ERROR: animal without a name"
    return animal_repository_str

def main():
    user_input=input("Animal: ")
    animals_data=data_fetcher.fetch_data(user_input)

    html_data = load_html_file("animals_template.html")
    __replace__ = "__REPLACE_ANIMALS_INFO__"
    animal_repository_string = ""
    # print("This is the length", len(animals_data))

    if len(animals_data) > 0:
        # Animal is found
        # for each type of animal in the input json file, create a repository string
        print("Animal is found in database, please check the outputfile")

        for animal in animals_data:
            animal_repository_string += serialize_animal(animal)
    else:
        # Animal is not found
        print("Animal not found in database, please try again")
        animal_repository_string += html_if_animal_not_in_DB(user_input)

    # The replacement below is necessary to avoid a mojibake
    animal_repository_string = animal_repository_string.replace("â€™", "\'")
    # Replace the string to replace in the html with the animal repository
    html_data = html_data.replace(__replace__, animal_repository_string)

    write_to_new_html_file(html_data)


if __name__ == "__main__":
    main()
