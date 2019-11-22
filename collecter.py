import requests
import json

# Information for Github API
# NOTE: the first token suddently disappeared, and I do not know why
TOKEN = "f868e0139417bf8ffc09341baa0376759c04587f"
HEADERS = {"Authorization": "token {}".format(TOKEN)}

TEAM_LIST = [
    {
        "team_name": "Gray Team",
        "table_number": 5,
        "repo_link": "https://github.com/blaza168/hack_2019"
    },
    {
        "team_name": "grepnebonic",
        "table_number": 6,
        "repo_link": "https://github.com/atthack-2019/rogue-ap-detection"
    },
    {
        "team_name": "Prestiz",
        "table_number": 9,
        "repo_link": "https://github.com/Fenristan/Hackathon-2019"
    },
    {
        "team_name": "Hundiska",
        "table_number": 10,
        "repo_link": "https://github.com/szymsza/happy-chick-house"
    },
    {
        "team_name": "Uzlabina",
        "table_number": 13,
        "repo_link": "https://github.com/kubax2000/ATTHACK2019"
    },
    {
        "team_name": "Team20",
        "table_number": 20,
        "repo_link": "https://github.com/Kubos-cz/atthack20"
    }
]

# Dictionaries to store the aggregated information
CONTRIBUTORS_INFORMATION = {}
LANGUAGES_INFORMATION = {}
BRANCHES_INFORMATION = {}

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
    endpoint = BRANCHES_ENDPOINT_TEMPLATE.format(user_name, repo_name)
    response = requests.get(endpoint, headers=HEADERS).text
    response_dict = json.loads(response)

    branch_amount = len(response_dict)
    branch_names = []
    for branch in response_dict:
        branch_names.append(branch["name"])

    print("branch_amount", branch_amount)
    print("branch_names", branch_names)

    return {
        "branch_amount": branch_amount,
        "branch_names": branch_names
    }


def get_languages(user_name, repo_name):
    """
    Returning number of languages for a certain repository,
        together with their names
    """
    endpoint = LANGUAGES_ENDPOINT_TEMPLATE.format(user_name, repo_name)
    response = requests.get(endpoint, headers=HEADERS).text
    response_dict = json.loads(response)

    language_amount = len(response_dict)
    language_names = []
    for language in response_dict:
        language_names.append(language)

    print("language_amount", language_amount)
    print("language_names", language_names)

    return {
        "language_amount": language_amount,
        "language_names": language_names
    }


if __name__ == "__main__":
    get_rate_limit()
    for team in TEAM_LIST:
        repo_link = team["repo_link"]
        user_name, repo_name = _extract_name_and_repo_from_link(repo_link)

        # get_languages(user_name=user_name, repo_name=repo_name)
        # get_branches(user_name=user_name, repo_name=repo_name)
        get_contributors_and_amounts_of_commits(user_name=user_name, repo_name=repo_name)

    # get_rate_limit()
    # get_languages(user_name="szymsza", repo_name="att-hackathon")
    # get_branches(user_name="szymsza", repo_name="att-hackathon")
    # get_contributors_and_amounts_of_commits(user_name="szymsza", repo_name="att-hackathon")

# rate_limit = rate_limit_dict["resources"]["core"]["limit"]
# print(rate_limit)
# print(response.request.headers)

# print(response_text)

# print("hello world")

# {
#     [
#         "team_name": "xxx",
#         "table_number": 16,
#         "repo_link": "www.fwfwe.cz",
#         "commit_amount":45
#     ],
#     [
#         "team_name": "yyy",
#         "table_number": 4,
#         "repo_link": "www.fwfwfwee.cz",
#         "commit_amount":43
#     ]
# }
