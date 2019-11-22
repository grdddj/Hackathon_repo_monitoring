// $.get("localhost/v1/get_whatever", function (data) {
//     // TODO: append parsed data to table
//     $(".results").html(data);
//     console.log("Load was performed.");
// });


// Languages used - languages-table

// [{"team_name": "Prestiz", "table_number": 9, "repo_link": "https://github.com/Fenristan/Hackathon-2019", "language_amount": 0, "language_names": []}, {"team_name": "Gray Team", "table_number": 5, "repo_link": "https://github.com/blaza168/hack_2019", "language_amount": 1, "language_names": ["Python"]}, {"team_name": "Team20", "table_number": 20, "repo_link": "https://github.com/Kubos-cz/atthack20", "language_amount": 0, "language_names": []}, {"team_name": "Hundiska", "table_number": 10, "repo_link": "https://github.com/szymsza/att-hackathon", "language_amount": 0, "language_names": []}]

// Branches created - branches-table

// [{"team_name": "Gray Team", "table_number": 5, "repo_link": "https://github.com/blaza168/hack_2019", "branch_amount": 5, "branch_names": ["blazek", "kral", "martin", "master", "nguyen"]}, {"team_name": "Hundiska", "table_number": 10, "repo_link": "https://github.com/szymsza/att-hackathon", "branch_amount": 2, "branch_names": ["master", "server"]}, {"team_name": "Prestiz", "table_number": 9, "repo_link": "https://github.com/Fenristan/Hackathon-2019", "branch_amount": 1, "branch_names": ["master"]}, {"team_name": "Team20", "table_number": 20, "repo_link": "https://github.com/Kubos-cz/atthack20", "branch_amount": 1, "branch_names": ["master"]}]

// Commits pushed - commits-table

// [{"team_name": "Uzlabina", "table_number": 13, "repo_link": "https://github.com/kubax2000/ATTHACK2019", "contributors_amount": 4, "commit_amounts": {"Avik0": 7, "Fligos": 7, "Andrew-SE": 3, "kubax2000": 2}, "overall_commit_amount": 19}, {"team_name": "Hundiska", "table_number": 10, "repo_link": "https://github.com/szymsza/happy-chick-house", "contributors_amount": 1, "commit_amounts": {"szymsza": 4}, "overall_commit_amount": 4}, {"team_name": "grepnebonic", "table_number": 6, "repo_link": "https://github.com/atthack-2019/rogue-ap-detection", "contributors_amount": 1, "commit_amounts": {"adamivora": 3}, "overall_commit_amount": 3}, {"team_name": "Gray Team", "table_number": 5, "repo_link": "https://github.com/blaza168/hack_2019", "contributors_amount": 2, "commit_amounts": {"tortila123": 1, "Bjergus": 1}, "overall_commit_amount": 2}, {"team_name": "Prestiz", "table_number": 9, "repo_link": "https://github.com/Fenristan/Hackathon-2019", "contributors_amount": 2, "commit_amounts": {"Fenristan": 1, "Lukyk0": 1}, "overall_commit_amount": 2}, {"team_name": "Team20", "table_number": 20, "repo_link": "https://github.com/Kubos-cz/atthack20", "contributors_amount": 1, "commit_amounts": {"Kubos-cz": 1}, "overall_commit_amount": 1}]

function parse_commits(json) {
    var allowed = ['team_name', 'table_number', 'repo_link', 'contributors_amount', 'commit_amounts', 'overall_commit_amount'];
    html = `<thead class="thead-dark">
        <tr>
        <th scope="col">Team name</th>
        <th scope="col">Table number</th>
        <th scope="col">Repo link</th>
        <th scope="col">Contributor amount</th>
        <th scope="col">Commit amount</th>
        <th scope="col">Overall commit amount</th>
      </tr>
    </thead>
    <tbody>`
    for (const [id, team] of Object.entries(json)) {
        //console.log(team)
        html += `<tr>`
        for (const [par, value] of Object.entries(team)) {
            //const [key, value] of Object.entries(test)
            if (allowed.includes(par)) {
                if (par == 'commit_amounts') { 
                    html += `<th scope="row">`;
                    for (const [sub_par, sub_value] of Object.entries(value)) {
                        html += `<div class="row">${sub_par}: ${sub_value}</div>`;
                    }
                    html += `</th>`;
                } else {
                    html += `<th scope="row">${value}</th>`;
                }
            } else {
                html += `<th scope="row">Lost in multiverse</th>`;
            }

        } // for teams
        html += `</tr>`;
    } // for json
    html += `</tbody>
    </table>`;

    return html;
}



function clock(interval) {
    "use strict";
    // interval : "Aug 24, 2018"

    function getTimeRemaining(endtime) {
        var t = Date.parse(endtime) - Date.parse(new Date());
        var seconds = Math.floor((t / 1000) % 60);
        var minutes = Math.floor((t / 1000 / 60) % 60);
        return {
            'total': t,
            'minutes': minutes,
            'seconds': seconds,
        };
    }

    function initializeClock(id, endtime) {
        var minutesSpan = $('.minutes');
        var secondsSpan = $('.seconds');

        function updateClock() {
            var t = getTimeRemaining(endtime);

            minutesSpan.html(('0' + t.minutes).slice(-2));
            secondsSpan.html(('0' + t.seconds).slice(-2));

            if (t.total <= 0) {
                console.log('Calling API...');
                // TODO: Call API
                clearInterval(timeinterval);
                var newDeadline = new Date();
                newDeadline.setMinutes(newDeadline.getMinutes() + interval);
                initializeClock('clockdiv', newDeadline);
            }
        }

        updateClock();
        var timeinterval = setInterval(updateClock, 1000);
    }

    var deadline = new Date();
    deadline.setMinutes(deadline.getMinutes() + interval);
    initializeClock('clockdiv', deadline);
}

// Main loop

$(document).ready(function () {
    console.log("Calling API...");
    json = [{ "team_name": "Uzlabina", "table_number": 13, "repo_link": "https://github.com/kubax2000/ATTHACK2019", "contributors_amount": 4, "commit_amounts": { "Avik0": 7, "Fligos": 7, "Andrew-SE": 3, "kubax2000": 2 }, "overall_commit_amount": 19 }, { "team_name": "Hundiska", "table_number": 10, "repo_link": "https://github.com/szymsza/happy-chick-house", "contributors_amount": 1, "commit_amounts": { "szymsza": 4 }, "overall_commit_amount": 4 }, { "team_name": "grepnebonic", "table_number": 6, "repo_link": "https://github.com/atthack-2019/rogue-ap-detection", "contributors_amount": 1, "commit_amounts": { "adamivora": 3 }, "overall_commit_amount": 3 }, { "team_name": "Gray Team", "table_number": 5, "repo_link": "https://github.com/blaza168/hack_2019", "contributors_amount": 2, "commit_amounts": { "tortila123": 1, "Bjergus": 1 }, "overall_commit_amount": 2 }, { "team_name": "Prestiz", "table_number": 9, "repo_link": "https://github.com/Fenristan/Hackathon-2019", "contributors_amount": 2, "commit_amounts": { "Fenristan": 1, "Lukyk0": 1 }, "overall_commit_amount": 2 }, { "team_name": "Team20", "table_number": 20, "repo_link": "https://github.com/Kubos-cz/atthack20", "contributors_amount": 1, "commit_amounts": { "Kubos-cz": 1 }, "overall_commit_amount": 1 }]
    $('#commits-table').html(parse_commits(json))
    // TODO: Call API
    clock(1); // in minutes
});