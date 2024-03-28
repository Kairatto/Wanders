import os


def delete_files(file_names, folders):
    for folder in folders:
        for file_name in file_names:
            file_path = os.path.join(folder, file_name)
            try:
                os.remove(file_path)
                print(f"File {file_path} Удаление прошло успешно!")
            except FileNotFoundError:
                print(f"File {file_path} Файл не найден")
            except Exception as e:
                print(f" Произошла ошибка при удалении {file_path}: {e}")


if __name__ == "__main__":
    file_names_to_delete = ["0001_initial.py", "0002_initial.py", "db.sqlite3"]
    folders_to_search = ["apps/accommodation/migrations", "apps/collection_point/migrations",
                         "apps/concrete_tour/migrations", ".", "apps/days/migrations", "apps/guide/migrations",
                         "apps/includes/migrations", "apps/list_of_things/migrations", "apps/question/migrations",
                         "apps/recommendations/migrations", "apps/tags/migrations", "apps/tour/migrations",
                         "apps/tour_images/migrations", "apps/account/migrations", "apps/location_info/migrations",
                         "apps/review/migrations", "apps/user/migrations",
                         "apps/favorites/migrations", "apps/business/migrations", "apps/about_us/migrations",]

    delete_files(file_names_to_delete, folders_to_search)
