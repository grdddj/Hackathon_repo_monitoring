import collecter

# Lists to store the aggregated information
CONTRIBUTORS_INFORMATION = []
LANGUAGES_INFORMATION = []
BRANCHES_INFORMATION = []

def aggregate_languages():
    """
    Returning the leaderboard with information about used languages
    """
    for team in collecter.TEAM_LIST:
        team_name = team["team_name"]
        table_number = team["table_number"]
        repo_link = team["repo_link"]

        user_name, repo_name = collecter._extract_name_and_repo_from_link(repo_link)

        result = collecter.get_languages(user_name=user_name, repo_name=repo_name)
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

    # LANGUAGES_INFORMATION.sort(lambda x: x.modified, reverse=True)

    print(LANGUAGES_INFORMATION)

if __name__ == "__main__":
    aggregate_languages()
