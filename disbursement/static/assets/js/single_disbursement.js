$(document).ready(function(){
    var result;
    // Submit post on submit
    $('#single-disbursement').on('submit', function(event){
        event.preventDefault();
        load_confirmation_box();
    });

    function load_confirmation_box(){
      swal({
            title: "Disburse",
            text: "Are you sure you disburse "+$('#amount').val()+" to "+$('#recipient option:selected').text()+" ?",
            icon: "warning",
            buttons: {
                    cancel: {
                        text: "No, cancel plx!",
                        value: null,
                        visible: true,
                        className: "",
                        closeModal: false,
                    },
                    confirm: {
                        text: "Yes Proceed!!!",
                        value: true,
                        visible: true,
                        className: "",
                        closeModal: false
                    }
            }
        }).then(isConfirm => {
            if (isConfirm) {

              var csrftoken = getCookie('csrftoken');  

                    $.ajax({
                      beforeSend: function(xhr, settings) {
                          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                              xhr.setRequestHeader("X-CSRFToken", csrftoken);
                          }
                      },
                      url : "/disbursements/single_ajax", // the endpoint
                      type : "POST", // http method
                      data : { recipient: $('#recipient').val(), amount: $('#amount').val(), reason: $('#reason').val()}, // data sent with the post request

                      // handle a successful response
                      success : function(json) {
                          $('#recipient').val(''); // remove the value from the input
                          $('#amount').val(''); // remove the value from the input
                          $('#reason').val(''); // remove the value from the input
                          console.log(json)
                          result = json;
                          swal("Added!", "Supplier successfully added!!", "success").then(function() {
                                // Redirect the user
                                var return_url = $('#returnUrl').val()
                                window.location.href = return_url;
                                console.log('The Ok Button was clicked.');
                              });
                      },

                      // handle a non-successful response
                      error : function(xhr,errmsg,err) {

                          swal("Error!", xhr.status, "error")
                          
                      }
                  });

            } else {
                swal("Cancelled", "It's safe.", "error");
            }
        });
    }

    // using jQuery
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
});