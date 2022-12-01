function display_freekicks(data) {
    $("#posts").empty()
    if (data.length == 0) {
        let new_post = $("<div class='post1'>")
        new_post.append("No freekick found")
        $('#freekick_buttons').append(new_post)
    } else {
        $.each(data, function(index, value) {
            let new_post = $("<div class='col-md-2 col-4 mx-3 my-3'>")
            let link = "/freekick/" + value["id"]
            let img = $("<img class='img-fluid'>")
            img.attr("src", 'https://www.pinclipart.com/picdir/big/519-5193552_football-clip-art-transparent-background-soccer-ball-png.png')
            img.prop("alt", "soccerball")
            let name = $("<a class='link-center' href=" + link + ">")
            name.append(img)
            let span = $("<span class='freekick-link'>")
            span.text(value["name"])
            name.append(span)
            new_post.append(name)
            name.hover(function() {
                    img.addClass("bounce")
                },
                function() {
                    img.removeClass("bounce")
                }
            )
            $("#freekick_buttons").append(new_post)
        });
    }

}

$(document).ready(function() {


    display_freekicks(data)

})