import requests
import json

token = "f868e0139417bf8ffc09341baa0376759c04587f"
headers = {"Authorization": "token {}".format(token)}


def get_rate_limit():
    rate_limit_endpoint = "https://api.github.com/rate_limit"
    rate_limit_response = requests.get(
        rate_limit_endpoint, headers=headers).text
    print(rate_limit_response)
    rate_limit_dict = json.loads(rate_limit_response)
    rate_limit = rate_limit_dict["resources"]["core"]["limit"]
    print(rate_limit)


def get_contributors_and_amounts_of_commits():
    rate_limit_endpoint = "https://api.github.com/repos/grdddj/Diploma-Thesis---Inverse-Heat-Transfer/contributors"
    rate_limit_response = requests.get(
        rate_limit_endpoint, headers=headers).text
    print(rate_limit_response)
    rate_limit_dict = json.loads(rate_limit_response)

    contributors_amount = len(rate_limit_dict)
    print(contributors_amount)
    commit_amounts = {}
    for person in rate_limit_dict:
        commit_amounts[person["login"]] = person["contributions"]

    print(commit_amounts)


def get_branches():
    rate_limit_endpoint = "https://api.github.com/repos/grdddj/Diploma-Thesis---Inverse-Heat-Transfer/branches"
    rate_limit_response = requests.get(
        rate_limit_endpoint, headers=headers).text
    print(rate_limit_response)
    rate_limit_dict = json.loads(rate_limit_response)

    branch_amount = len(rate_limit_dict)
    print(branch_amount)
    branch_names = []
    for branch in rate_limit_dict:
        branch_names.append(branch["name"])
    print(branch_names)


def get_languages():
    rate_limit_endpoint = "https://api.github.com/repos/grdddj/Diploma-Thesis---Inverse-Heat-Transfer/languages"
    rate_limit_response = requests.get(
        rate_limit_endpoint, headers=headers).text
    print(rate_limit_response)
    rate_limit_dict = json.loads(rate_limit_response)

    language_amount = len(rate_limit_dict)
    print(language_amount)
    language_names = []
    for language in rate_limit_dict:
        language_names.append(language)
    print(language_names)


if __name__ == "__main__":
    # get_rate_limit()
    # get_languages()
    # get_branches()
    get_contributors_and_amounts_of_commits()

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
