import collecter_github
import collecter_gitlab
import json
import os
import time

WORKING_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

# Getting the list of repositories which should be checked
github_links_file = "teams_github.json"
github_links_file_absolute = os.path.join(WORKING_DIRECTORY, github_links_file)
with open(github_links_file_absolute, "r") as link_file:
    GITHUB_TEAM_LIST = json.loads(link_file.read())["team_list"]

# Getting the list of repositories which should be checked
gitlab_links_file = "teams_gitlab.json"
gitlab_links_file_absolute = os.path.join(WORKING_DIRECTORY, gitlab_links_file)
with open(gitlab_links_file_absolute, "r") as link_file:
    GITLAB_TEAM_LIST = json.loads(link_file.read())["team_list"]

def aggregate_languages():
    """
    Returning the leaderboard with information about used languages
    """
    LANGUAGES_INFORMATION = []

    for team in GITHUB_TEAM_LIST:
        team_name = team["team_name"]
        table_number = team["table_number"]
        repo_link = team["repo_link"]

        user_name, repo_name = collecter_github._extract_name_and_repo_from_link(
            repo_link)

        result = collecter_github.get_languages(
            user_name=user_name, repo_name=repo_name)
        language_amount = result["language_amount"]
        language_names = result["language_names"]

        LANGUAGES_INFORMATION.append(
            {
                "team_name": team_name,
                "table_number": table_number,
                "repo_link": repo_link,
                "language_amount": language_amount,
                "language_names": language_names
            }
        )

    for team in GITLAB_TEAM_LIST:
        team_name = team["team_name"]
        table_number = team["table_number"]
        repo_link = team["repo_link"]
        project_ids = team["project_ids"]

        # Making a set, if these languages would be repeating in multiple projects
        language_names = set()

        for project_id in project_ids:
            result = collecter_gitlab.get_languages(project_id=project_id)
            for language in result["language_names"]:
                language_names.add(language)

        # To serialize into json we cannot use set unfortunatelly
        language_names = list(language_names)
        language_amount = len(language_names)

        LANGUAGES_INFORMATION.append(
            {
                "team_name": team_name,
                "table_number": table_number,
                "repo_link": repo_link,
                "language_amount": language_amount,
                "language_names": language_names
            }
        )

    LANGUAGES_INFORMATION.sort(key=lambda x: x["language_amount"], reverse=True)

    print(json.dumps(LANGUAGES_INFORMATION))

    return json.dumps(LANGUAGES_INFORMATION)

def aggregate_branches():
    """
    Returning the leaderboard with information about branches
    """
    BRANCHES_INFORMATION = []

    for team in GITHUB_TEAM_LIST:
        team_name = team["team_name"]
        table_number = team["table_number"]
        repo_link = team["repo_link"]

        user_name, repo_name = collecter_github._extract_name_and_repo_from_link(
            repo_link)

        result = collecter_github.get_branches(
            user_name=user_name, repo_name=repo_name)
        branch_amount = result["branch_amount"]
        branch_names = result["branch_names"]

        BRANCHES_INFORMATION.append(
            {
                "team_name": team_name,
                "table_number": table_number,
                "repo_link": repo_link,
                "branch_amount": branch_amount,
                "branch_names": branch_names
            }
        )

    for team in GITLAB_TEAM_LIST:
        team_name = team["team_name"]
        table_number = team["table_number"]
        repo_link = team["repo_link"]

        user_name, repo_name = collecter_github._extract_name_and_repo_from_link(
            repo_link)

        result = collecter_github.get_branches(
            user_name=user_name, repo_name=repo_name)
        branch_amount = result["branch_amount"]
        branch_names = result["branch_names"]

        BRANCHES_INFORMATION.append(
            {
                "team_name": team_name,
                "table_number": table_number,
                "repo_link": repo_link,
                "branch_amount": branch_amount,
                "branch_names": branch_names
            }
        )

    BRANCHES_INFORMATION.sort(key=lambda x: x["branch_amount"], reverse=True)

    print(json.dumps(BRANCHES_INFORMATION))

    return json.dumps(BRANCHES_INFORMATION)

def aggregate_contributors_and_commits():
    """
    Returning the leaderboard with information contributors and commits
    """
    CONTRIBUTORS_INFORMATION = []

    for team in GITHUB_TEAM_LIST:
        team_name = team["team_name"]
        table_number = team["table_number"]
        repo_link = team["repo_link"]

        user_name, repo_name = collecter_github._extract_name_and_repo_from_link(
            repo_link)

        result = collecter_github.get_contributors_and_amounts_of_commits(
            user_name=user_name, repo_name=repo_name)
        contributors_amount = result["contributors_amount"]
        commit_amounts = result["commit_amounts"]
        overall_commit_amount = result["overall_commit_amount"]

        CONTRIBUTORS_INFORMATION.append(
            {
                "team_name": team_name,
                "table_number": table_number,
                "repo_link": repo_link,
                "contributors_amount": contributors_amount,
                "commit_amounts": commit_amounts,
                "overall_commit_amount": overall_commit_amount
            }
        )

    for team in GITLAB_TEAM_LIST:
        team_name = team["team_name"]
        table_number = team["table_number"]
        repo_link = team["repo_link"]
        project_ids = team["project_ids"]

        overall_commit_amount = 0
        contributors = set()
        commit_amounts = {}

        for project_id in project_ids:

            result = collecter_gitlab.get_contributors_and_amounts_of_commits(
                project_id=project_id)
            current_commit_amounts = result["commit_amounts"]
            for person in current_commit_amounts:
                contributors.add(person)
                if person in commit_amounts:
                    commit_amounts[person] += current_commit_amounts[person]
                else:
                    commit_amounts[person] = current_commit_amounts[person]
            overall_commit_amount += result["overall_commit_amount"]

        contributors_amount = len(contributors)

        CONTRIBUTORS_INFORMATION.append(
            {
                "team_name": team_name,
                "table_number": table_number,
                "repo_link": repo_link,
                "contributors_amount": contributors_amount,
                "commit_amounts": commit_amounts,
                "overall_commit_amount": overall_commit_amount
            }
        )

    CONTRIBUTORS_INFORMATION.sort(key=lambda x: x["overall_commit_amount"], reverse=True)

    print(json.dumps(CONTRIBUTORS_INFORMATION))

    return json.dumps(CONTRIBUTORS_INFORMATION)


if __name__ == "__main__":
    # aggregate_languages()
    # aggregate_branches()
    aggregate_contributors_and_commits()
