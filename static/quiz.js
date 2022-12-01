function createData(data) {
    $("#quiz_data").empty()
    let media = null
    let type = data["data_type"]
    if (type === "video") {
        $("#quiz_data").addClass("embed-responsive embed-responsive-16by9")
        $("#quiz_data").html(
            '<iframe src=' + `${data["data"]}` + ' frameborder="0" class="embed-responsive-item" ></iframe>'
        )
        $("#quiz_data").css("border", "5px solid #174785")
    } else if (type === "picture") {
        media = $("<img class='img-fluid'>")
        media.attr("src", `${data["data"]}`)
        media.prop("alt", `${data["alt"]}`)
        $("#quiz_data").append(media)
    } else if (type === "text") {
        media = $("<img class='img-fluid3'>")
        media.attr("src", "/static/images/cloud.png")
        media.prop("alt", "img of cloud bubble")
        $("#quiz_data").append(media)

        textOver = $("<div id='text'></div>")
        textOver.text(`${data["data"]}`)
        $("#quiz_data").append(textOver)
    }

}

// Creating a new record
function submit(data) {
    $.ajax({
        type: "POST",
        url: "quiz_feedback",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(data),
        success: function(result) {
            if (parseInt(result["data"]["id"]) > 5) {
                window.location.href = "/quiz/end";
            } else {
                window.location.href = "/quiz/" + result["data"]["id"];
            }

        },
        error: function(request, status, error) {
            console.log("Error");
            console.log(request);
            console.log(status);
            console.log(error);
        }
    });
}

$(document).ready(function() {

    createData(data)

    $("#dialog").dialog({
        autoOpen: false,
        modal: true,
        show: "blind",
        hide: "blind",
        buttons: {
            "Yes": function() {
                $(this).dialog("close");
                window.location.href = "/freekick/1";
            },
            "No": function() {
                $(this).dialog("close");
            }
        }
    });

    $('#stuck_button').click(function() {
        console.log("Stuck pressed")
        $('#dialog').dialog('open');
    });


    let ans = { "question_number": "0" }

    $("#answer1").click(function() {
        console.log("1 Pressed")
        $("#answer2").prop("checked", false);
        $("#answer3").prop("checked", false);
        $("#answer4").prop("checked", false);

        ans = {
            "question_number": data["id"],
            "answer_number": "1"
        }

    })

    $("#answer2").click(function() {
        console.log("2 Pressed")
        $("#answer1").prop("checked", false);
        $("#answer3").prop("checked", false);
        $("#answer4").prop("checked", false);

        ans = {
            "question_number": data["id"],
            "answer_number": "2"
        }

    })

    $("#answer3").click(function() {
        console.log("4 Pressed")
        $("#answer1").prop("checked", false);
        $("#answer2").prop("checked", false);
        $("#answer4").prop("checked", false);

        ans = {
            "question_number": data["id"],
            "answer_number": "3"
        }

    })

    $("#answer4").click(function() {
        console.log("4 Pressed")
        $("#answer1").prop("checked", false);
        $("#answer2").prop("checked", false);
        $("#answer3").prop("checked", false);
        ans = {
            "question_number": data["id"],
            "answer_number": "4"
        }

    })

    $("#submit_button").click(function() {
        console.log("Submit pressed")
        console.log(ans)
        if (ans["question_number"] != "0") {
            submit(ans)
        }

    })
});