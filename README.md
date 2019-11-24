# Hackathon_repo_monitoring
Repository to spy on other repositories. Works with GitHub and GitLab repositories.

It was created on AT&T Hackathon 2019 to help mentors with assessing the technical quality of participating teams.

It aggregates numerous information about repositories participating on the hackathon and provides an easy-to-get insight into the work ethics of the teams. It can point out suspiciously high, as well as suspiciously low commits amounts, figures out the languages teams use, and the most active committer of the whole hackathon can be easily identified (and awarded).

Possible improvements contain:
- caching the results for some time on the server, not having to harass GitHub and GitLab APIs so frequently
- add individual leaderboard for the most frequent committer (as an individual)
- identify commits that have been made outside of hackathon, so they can be easily reviewed and assessed (to avoid cheating, or to make it harder)
- error handling can be improved, to get better responses when repo does not exist anymore etc.

Credit for creating the Front-End goes to @albulinek (https://github.com/Albulinek)
