function makeQuizStatistics() {
    let num_of_wrongs = wrong_answers.length
        // console.log(wrong_answers)
        // console.log(num_of_wrongs)
    if (num_of_wrongs > 0) {
        let header = $("<div></div>")
        header.addClass("quiz_stats_header")
        header.html("Questions you got wrong")
        $(".quiz_stats").append(header)
    }


    let feedback = wrong_ans_feedback
    console.log(feedback)

    for (let key in feedback) {
        let str_key = key.toString()

        let item_button = $("<button>" + `Question ${key}` + "</button>")
        item_button.addClass("collapsible")
        item_button.attr("type", "button")

        //console.log(feedback[str_key]["explanation"])
        let item_explanation = $("<div class='content'></div>")
        item_explanation.attr("id", `${key}`)
        item_explanation.html("<p>" + `${feedback[str_key]["explanation"]}` + "</p>\
                            <p>Click <a class='quiz_stats_feedback' href=" + `${feedback[str_key]["explanation_link"]}` + " >here</a> to review</p>")

        let test_div = $("<div class='padding_quiz'></div>")

        $(".quiz_stats").append(item_button)
        $(".quiz_stats").append(item_explanation)
        $(".quiz_stats").append(test_div)


    }

    let coll = document.getElementsByClassName("collapsible");
    let i;

    for (i = 0; i < coll.length; i++) {
        coll[i].addEventListener("click", function() {
            this.classList.toggle("active");
            let content = this.nextElementSibling;
            if (content.style.display === "block") {
                content.style.display = "none";
            } else {
                content.style.display = "block";
            }
        });
    }


}

$(document).ready(function() {


    $(".result_score").empty()
    $(".result_message").empty()

    if (quiz_score < 4) {
        $(".result_message").append("<span class='bold_large'>Practice Again!</span>")
        $(".result_message").append("<br>")
        $(".result_message").append("Don't worry, even David Beckham made mistakes")

        $(".result_score").addClass("red")
        $(".result_score").text("Score: " + quiz_score + "/5")
    } else {
        $(".result_message").append("<span class='bold_large'>Congratulations!!</span>")
        $(".result_message").append("<br>")
        $(".result_message").append("You have passed the test and are the next David Beckham!")
        $(".result_score").addClass("green")
        $(".result_score").text("Score: " + quiz_score + "/5")
        $(".result_btns").empty()
    }

    $(".quiz_stats").empty()
    $(".quiz_stats_header").empty()
    makeQuizStatistics()

})