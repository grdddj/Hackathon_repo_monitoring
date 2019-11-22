$.get("localhost/v1/get_whatever", function (data) {
    // TODO: append parsed data to table
    $(".results").html(data);
    console.log("Load was performed.");
});


// Languages used

// [{"team_name": "Prestiz", "table_number": 9, "repo_link": "https://github.com/Fenristan/Hackathon-2019", "language_amount": 0, "language_names": []}, {"team_name": "Gray Team", "table_number": 5, "repo_link": "https://github.com/blaza168/hack_2019", "language_amount": 1, "language_names": ["Python"]}, {"team_name": "Team20", "table_number": 20, "repo_link": "https://github.com/Kubos-cz/atthack20", "language_amount": 0, "language_names": []}, {"team_name": "Hundiska", "table_number": 10, "repo_link": "https://github.com/szymsza/att-hackathon", "language_amount": 0, "language_names": []}]