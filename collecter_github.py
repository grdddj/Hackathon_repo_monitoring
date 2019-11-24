import requests
import json
import os

WORKING_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

# Information for Github API
# NOTE: the first token suddently disappeared, and I do not know why
TOKEN = "f868e0139417bf8ffc09341baa0376759c04587f"
HEADERS = {"Authorization": "token {}".format(TOKEN)}

# Getting the list of repositories which should be checked
github_links_file = "teams_github.json"
github_links_file_absolute = os.path.join(WORKING_DIRECTORY, github_links_file)
with open(github_links_file_absolute, "r") as link_file:
    GITHUB_TEAM_LIST = json.loads(link_file.read())["team_list"]

# Templates for endpoints, to which user_name and repo_name should be inputted
CONTRIBUTORS_ENDPOINT_TEMPLATE = "https://api.github.com/repos/{}/{}/contributors"
LANGUAGES_ENDPOINT_TEMPLATE = "https://api.github.com/repos/{}/{}/languages"
BRANCHES_ENDPOINT_TEMPLATE = "https://api.github.com/repos/{}/{}/branches"

def _extract_name_and_repo_from_link(github_link):
    """
    Returns the username and repository name from the github repo link
    """
    split_link = github_link.split("/")
    user_name = split_link[-2]
    repo_name = split_link[-1]
    print(user_name, repo_name)

    return (user_name, repo_name)


def get_rate_limit():
    """
    Helper function to see what limit we have
    """
    rate_limit_endpoint = "https://api.github.com/rate_limit"
    rate_limit_response = requests.get(rate_limit_endpoint, headers=HEADERS).text
    rate_limit_dict = json.loads(rate_limit_response)
    rate_limit = rate_limit_dict["resources"]["core"]["remaining"]
    print("rate_limit", rate_limit)

def get_contributors_and_amounts_of_commits(user_name, repo_name):
    """
    Returning number of contributors and overall number of commits
        for the whole repository
    """
    try:
        endpoint = CONTRIBUTORS_ENDPOINT_TEMPLATE.format(user_name, repo_name)
        response = requests.get(endpoint, headers=HEADERS).text
        response_dict = json.loads(response)

        contributors_amount = len(response_dict)
        commit_amounts = {}
        for person in response_dict:
            commit_amounts[person["login"]] = person["contributions"]

        overall_commit_amount = 0
        for person  in commit_amounts:
            overall_commit_amount += commit_amounts[person]

        print("overall_commit_amount", overall_commit_amount)
        print("commit_amounts", commit_amounts)
        print("contributors_amount", contributors_amount)
    except Exception as e:
        print(f"ERROR: {e}")
        contributors_amount = 0
        commit_amounts = {}
        overall_commit_amount = 0

    return {
        "contributors_amount": contributors_amount,
        "commit_amounts": commit_amounts,
        "overall_commit_amount": overall_commit_amount
    }

def get_branches(user_name, repo_name):
    """
    Returning number of branches for a certain repository,
        together with their names
    """
    try:
        endpoint = BRANCHES_ENDPOINT_TEMPLATE.format(user_name, repo_name)
        response = requests.get(endpoint, headers=HEADERS).text
        response_dict = json.loads(response)

        branch_amount = len(response_dict)
        branch_names = []
        for branch in response_dict:
            try:
                branch_names.append(branch["name"])
            except TypeError:
                pass

        print("branch_amount", branch_amount)
        print("branch_names", branch_names)
    except Exception as e:
        print(f"ERROR: {e}")
        branch_amount = 0
        branch_names = []

    return {
        "branch_amount": branch_amount,
        "branch_names": branch_names
    }


def get_languages(user_name, repo_name):
    """
    Returning number of languages for a certain repository,
        together with their names
    """
    try:
        endpoint = LANGUAGES_ENDPOINT_TEMPLATE.format(user_name, repo_name)
        response = requests.get(endpoint, headers=HEADERS).text
        response_dict = json.loads(response)

        language_amount = len(response_dict)
        language_names = []
        for language in response_dict:
            language_names.append(language)

        print("language_amount", language_amount)
        print("language_names", language_names)
    except Exception as e:
        print(f"ERROR: {e}")
        language_amount = 0
        language_names = []

    return {
        "language_amount": language_amount,
        "language_names": language_names
    }


if __name__ == "__main__":
    get_rate_limit()
    for team in GITHUB_TEAM_LIST:
        repo_link = team["repo_link"]
        user_name, repo_name = _extract_name_and_repo_from_link(repo_link)

        # get_languages(user_name=user_name, repo_name=repo_name)
        # get_branches(user_name=user_name, repo_name=repo_name)
        get_contributors_and_amounts_of_commits(user_name=user_name, repo_name=repo_name)
