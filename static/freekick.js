function createData(freekick) {
    $("#learning_data").empty()

    $("#learning_data").html(
        '<iframe src=' + `${freekick["video"]}` + ' frameborder="0" class="embed-responsive-item embed-responsive-16by9"></iframe>'
    )
    if (freekick["id"] == "5") {
        let movetoQuiz = $("#nextb")

        movetoQuiz.text("Proceed to Quiz")
        movetoQuiz.attr("href", "/quiz_home")
    }

}

$(document).ready(function() {
    createData(freekick)

})