$.get("localhost/v1/get_whatever", function (data) {
    // TODO: append parsed data to table
    $(".results").html(data);
    console.log("Load was performed.");
});