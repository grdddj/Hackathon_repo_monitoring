function call_api() {
    get_languages();
    get_commits();
    get_branches();
}

// Languages used - languages-table

// [{"team_name": "Prestiz", "table_number": 9, "repo_link": "https://github.com/Fenristan/Hackathon-2019", "language_amount": 0, "language_names": []}, {"team_name": "Gray Team", "table_number": 5, "repo_link": "https://github.com/blaza168/hack_2019", "language_amount": 1, "language_names": ["Python"]}, {"team_name": "Team20", "table_number": 20, "repo_link": "https://github.com/Kubos-cz/atthack20", "language_amount": 0, "language_names": []}, {"team_name": "Hundiska", "table_number": 10, "repo_link": "https://github.com/szymsza/att-hackathon", "language_amount": 0, "language_names": []}]
function get_languages() {
    $.getJSON("http://www.jirkuvserver.cz:5005/languages", function (data) {
        parse_languages(JSON.parse(data));
    });
}

function parse_languages(json) {
    html = `<thead class="thead-dark">
        <tr>
        <th scope="col">Team name</th>
        <th scope="col">Table number</th>
        <th scope="col">Repo link</th>
        <th scope="col">Language amount</th>
        <th scope="col">Language names</th>
      </tr>
    </thead>
    <tbody>`
    for (const [id, team] of Object.entries(json)) {
        language_names = '';
        for (const [sub_par, sub_value] of Object.entries(team.language_names)) {
            language_names += `<div class="row">${sub_par}: ${sub_value}</div>`;
        }
        html += `<tr>
        <th scope="row">${team.team_name}</th>
        <th>${team.table_number}</th>
        <th><a href="${team.repo_link}">${team.repo_link}</a></th>
        <th>${team.language_amount}</th>
        <th>${language_names}</th>
        </tr>
        `
    }
    html += `</tbody>
    </table>`;

    $('#languages-table').html(html);
}

// Branches created - branches-table

// [{"team_name": "Gray Team", "table_number": 5, "repo_link": "https://github.com/blaza168/hack_2019", "branch_amount": 5, "branch_names": ["blazek", "kral", "martin", "master", "nguyen"]}, {"team_name": "Hundiska", "table_number": 10, "repo_link": "https://github.com/szymsza/att-hackathon", "branch_amount": 2, "branch_names": ["master", "server"]}, {"team_name": "Prestiz", "table_number": 9, "repo_link": "https://github.com/Fenristan/Hackathon-2019", "branch_amount": 1, "branch_names": ["master"]}, {"team_name": "Team20", "table_number": 20, "repo_link": "https://github.com/Kubos-cz/atthack20", "branch_amount": 1, "branch_names": ["master"]}]

function get_branches() {
    $.getJSON("http://www.jirkuvserver.cz:5005/branches", function (data) {
        parse_branches(JSON.parse(data));
    });
}

function parse_branches(json) {
    html = `<thead class="thead-dark">
        <tr>
        <th scope="col">Team name</th>
        <th scope="col">Table number</th>
        <th scope="col">Repo link</th>
        <th scope="col">Branch amount</th>
        <th scope="col">Branch names</th>
      </tr>
    </thead>
    <tbody>`
    for (const [id, team] of Object.entries(json)) {
        branch_names = '';
        for (const [sub_par, sub_value] of Object.entries(team.branch_names)) {
            branch_names += `<div class="row">${sub_par}: ${sub_value}</div>`;
        }
        html += `<tr>
        <th scope="row">${team.team_name}</th>
        <th>${team.table_number}</th>
        <th><a href="${team.repo_link}">${team.repo_link}</a></th>
        <th>${team.branch_amount}</th>
        <th>${branch_names}</th>
        </tr>
        `
    }
    html += `</tbody>
    </table>`;

    $('#branches-table').html(html);
}

// Commits pushed - commits-table

// [{"team_name": "Uzlabina", "table_number": 13, "repo_link": "https://github.com/kubax2000/ATTHACK2019", "contributors_amount": 4, "commit_amounts": {"Avik0": 7, "Fligos": 7, "Andrew-SE": 3, "kubax2000": 2}, "overall_commit_amount": 19}, {"team_name": "Hundiska", "table_number": 10, "repo_link": "https://github.com/szymsza/happy-chick-house", "contributors_amount": 1, "commit_amounts": {"szymsza": 4}, "overall_commit_amount": 4}, {"team_name": "grepnebonic", "table_number": 6, "repo_link": "https://github.com/atthack-2019/rogue-ap-detection", "contributors_amount": 1, "commit_amounts": {"adamivora": 3}, "overall_commit_amount": 3}, {"team_name": "Gray Team", "table_number": 5, "repo_link": "https://github.com/blaza168/hack_2019", "contributors_amount": 2, "commit_amounts": {"tortila123": 1, "Bjergus": 1}, "overall_commit_amount": 2}, {"team_name": "Prestiz", "table_number": 9, "repo_link": "https://github.com/Fenristan/Hackathon-2019", "contributors_amount": 2, "commit_amounts": {"Fenristan": 1, "Lukyk0": 1}, "overall_commit_amount": 2}, {"team_name": "Team20", "table_number": 20, "repo_link": "https://github.com/Kubos-cz/atthack20", "contributors_amount": 1, "commit_amounts": {"Kubos-cz": 1}, "overall_commit_amount": 1}]

function get_commits() {
    $.getJSON("http://www.jirkuvserver.cz:5005/commits", function (data) {
        parse_commits(JSON.parse(data));
    });
}

function parse_commits(json) {
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
    <tbody>`;
    for (const [id, team] of Object.entries(json)) {
        commit_amounts = '';
        for (const [sub_par, sub_value] of Object.entries(team.commit_amounts)) {
            commit_amounts += `<div class="row">${sub_par}: ${sub_value}</div>`;
        }
        html += `<tr>
        <th scope="row">${team.team_name}</th>
        <th>${team.table_number}</th>
        <th><a href="${team.repo_link}">${team.repo_link}</a></th>
        <th>${team.contributors_amount}</th>
        <th>${commit_amounts}</th>
        <th>${team.overall_commit_amount}</th>
        </tr>
        `
    }
    html += `</tbody>
    </table>`;

    $('#commits-table').html(html);
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
                call_api();
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
    call_api();
    clock(1); // in minutes
});