from github import list_and_parse_repos
from Repo import categories
from export import to_docs

if __name__ == "__main__":
    """Get the repos, parse them, sort them by category, export them to build/*.html"""
    repos = list_and_parse_repos()

    dict_category_repos = {}
    for category_id in categories:
        category = categories[category_id]
        category_repos = [repo for repo in repos if repo.category.id == category_id]

        print(category_id)
        print("-----")
        for repo in category_repos:
            print(repo)
        print()
        print()

        dict_category_repos[category.name] = category_repos

    to_docs(dict_category_repos)