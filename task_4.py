import requests

def get_user_profile(username):
    r = requests.get(f"https://api.github.com/users/{username}")
    if r.status_code == 200:
        u = r.json()
        print(f"Имя: {u.get('name', '—')}")
        print(f"Ссылка: {u['html_url']}")
        print(f"Репозиториев: {u['public_repos']}")
        print(f"Обсуждений: {u['public_gists']}")
        print(f"Подписок: {u['following']}")
        print(f"Подписчиков: {u['followers']}")
    else:
        print("Пользователь не найден")

def get_user_repos(username):
    r = requests.get(f"https://api.github.com/users/{username}/repos", params={'per_page': 100})
    if r.status_code == 200:
        for repo in r.json():
            print(f"\nНазвание: {repo['name']}")
            print(f"Ссылка: {repo['html_url']}")
            print(f"Просмотров: —")
            print(f"Язык: {repo.get('language', '—')}")
            print(f"Видимость: {repo['visibility']}")
            print(f"Ветка: {repo['default_branch']}")
    else:
        print("Пользователь не найден")

def search_repos(query):
    r = requests.get("https://api.github.com/search/repositories", params={'q': query, 'per_page': 100})
    if r.status_code == 200:
        for repo in r.json()['items']:
            print(f"{repo['name']} - {repo['html_url']}")
    else:
        print("Ошибка поиска")

def main():
    while True:
        print("1. Профиль пользователя")
        print("2. Репозитории пользователя")
        print("3. Поиск репозиториев")
        print("4. Выход")
        c = input("Выбор: ")

        if c == '1':
            get_user_profile(input("Имя пользователя: "))
        elif c == '2':
            get_user_repos(input("Имя пользователя: "))
        elif c == '3':
            search_repos(input("Поиск: "))
        elif c == '4':
            break

if __name__ == "__main__":
    main()