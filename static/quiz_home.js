

function validateSearch() {
    if ( $.trim( $('#search_box').val() ) == '' )
    {
        reset()
        return false
    }
    return true
}

function reset()
{
    $("#search_box").val("")
    $("#search_box").focus()
}

$(document).ready(function(){

    $("#search_box").focus()

    // Detect Enter key
    $("#search_box").keyup(function(event){
        if (event.keyCode === 13)
        {
                $("#submit_search").click()
        }
    })

    $("#submit_search").click(function(){
        return validateSearch()
    })

})