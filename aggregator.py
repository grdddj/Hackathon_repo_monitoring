import collecter
import json
import os
import time

WORKING_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

# Getting the list of repositories which should be checked
github_links_file = "teams_github.json"
github_links_file_absolute = os.path.join(WORKING_DIRECTORY, github_links_file)
with open(github_links_file_absolute, "r") as link_file:
    GITHUB_TEAM_LIST = json.loads(link_file.read())["team_list"]

def aggregate_languages():
    """
    Returning the leaderboard with information about used languages
    """
    LANGUAGES_INFORMATION = []

    for team in GITHUB_TEAM_LIST:
        team_name = team["team_name"]
        table_number = team["table_number"]
        repo_link = team["repo_link"]

        user_name, repo_name = collecter._extract_name_and_repo_from_link(
            repo_link)

        result = collecter.get_languages(
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

        user_name, repo_name = collecter._extract_name_and_repo_from_link(
            repo_link)

        result = collecter.get_branches(
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

        user_name, repo_name = collecter._extract_name_and_repo_from_link(
            repo_link)

        result = collecter.get_contributors_and_amounts_of_commits(
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

    CONTRIBUTORS_INFORMATION.sort(key=lambda x: x["overall_commit_amount"], reverse=True)

    print(json.dumps(CONTRIBUTORS_INFORMATION))

    return json.dumps(CONTRIBUTORS_INFORMATION)


if __name__ == "__main__":
    # aggregate_languages()
    # aggregate_branches()
    aggregate_contributors_and_commits()
