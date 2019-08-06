$(document).ready(function(){
    var result;
    // Submit post on submit
    $('#add-supplier').on('submit', function(event){
        event.preventDefault();
        load_confirmation_box();
    });


    function load_confirmation_box(){
      swal({
            title: "Add Supplier",
            text: "Are you sure you want to add "+$('#name').val()+" "+$('#account_number').val()+" as a supplier?",
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
                      url : "/suppliers/add_ajax", // the endpoint
                      type : "POST", // http method
                      data : { description: $('#description').val(), bank_code: $('#bank_code').val(), account_number: $('#account_number').val(), name: $('#name').val() }, // data sent with the post request

                      // handle a successful response
                      success : function(json) {
                          $('#name').val(''); // remove the value from the input
                          $('#account_number').val(''); // remove the value from the input
                          $('#bank_code').val(''); // remove the value from the input
                          $('#description').val(''); // remove the value from the input
                          console.log(json)
                          result = json;
                          swal("Added!", "Supplier successfully added!!", "success").then(function() {
                                // Redirect the user
                                var return_url = $('#returnUrl').val()
                                window.location.href = return_url;
                                console.log('The Ok Button was clicked.');
                              });
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