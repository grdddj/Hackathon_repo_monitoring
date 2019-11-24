import requests
import json
import os

# Information for GITLAB API
TOKEN = "1u2sfVGydCx-S9p21sxQ"
HEADERS = {"Private-Token": TOKEN}

WORKING_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

# Getting the list of repositories which should be checked
gitlab_links_file = "teams_gitlab.json"
gitlab_links_file_absolute = os.path.join(WORKING_DIRECTORY, gitlab_links_file)
with open(gitlab_links_file_absolute, "r") as link_file:
    GITLAB_TEAM_LIST = json.loads(link_file.read())["team_list"]

# Templates for endpoints, to which project ID should be inputted
CONTRIBUTORS_ENDPOINT_TEMPLATE = "https://gitlab.com/api/v4/projects/{}/repository/contributors"
COMMITS_ENDPOINT_TEMPLATE = "https://gitlab.com/api/v4/projects/{}/repository/commits"
LANGUAGES_ENDPOINT_TEMPLATE = "https://gitlab.com/api/v4/projects/{}/languages"
BRANCHES_ENDPOINT_TEMPLATE = "https://gitlab.com/api/v4/projects/{}/repository/branches"

def get_contributors_and_amounts_of_commits(project_id):
    """
    Returning number of contributors and overall number of commits
        for the whole repository
    """
    try:
        endpoint = CONTRIBUTORS_ENDPOINT_TEMPLATE.format(project_id)
        response = requests.get(endpoint, headers=HEADERS).text
        response_dict = json.loads(response)

        contributors_amount = len(response_dict)
        commit_amounts = {}
        for person in response_dict:
            commit_amounts[person["name"]] = person["commits"]

        overall_commit_amount = 0
        for person  in commit_amounts:
            overall_commit_amount += commit_amounts[person]

        try:
            print("overall_commit_amount", overall_commit_amount)
            print("commit_amounts", commit_amounts)
            print("contributors_amount", contributors_amount)
        except UnicodeEncodeError as e:
            print("UnicodeEncodeError", e)
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

def get_branches(project_id):
    """
    Returning number of branches for a certain repository,
        together with their names
    """
    try:
        endpoint = BRANCHES_ENDPOINT_TEMPLATE.format(project_id)
        response = requests.get(endpoint, headers=HEADERS).text
        response_dict = json.loads(response)

        branch_amount = len(response_dict)
        branch_names = []
        for branch in response_dict:
            branch_names.append(branch["name"])

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

def get_languages(project_id):
    """
    Returning number of languages for a certain repository,
        together with their names
    """
    try:
        endpoint = LANGUAGES_ENDPOINT_TEMPLATE.format(project_id)
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
    for team in GITLAB_TEAM_LIST:
        project_ids = team["project_ids"]
        for id in project_ids:
            # get_branches(project_id=id)
            # get_languages(project_id=id)
            get_contributors_and_amounts_of_commits(project_id=id)
