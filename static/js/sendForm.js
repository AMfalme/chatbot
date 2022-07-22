$(function() {
    console.log('halo');
    // $('.registration-form').html('halo send me home');
    function getFormData($form){
    var unindexed_array = $form.serializeArray();
    var indexed_array = {};

    $.map(unindexed_array, function(n, i){
      indexed_array[n['name']] = n['value'];
    });

    return indexed_array;
  }



  $('#registration-form').submit(function( event ) {
    console.log('halo');
    event.preventDefault();
    var form = $(this);
    var data = getFormData(form);
    
    data.DOB =  new Date(data.DOB)
    
    console.log(data.DOB)
    $.ajax({
      type: "POST",
      contentType: "application/json",
      url: "http://localhost:5000/register",
      data: JSON.stringify(data),
      success: function (response, status) {
       
        console.log(response);
        console.log(status);
        location.href = "http://localhost:5000/chat"
      },
      error: function(response, error) {
        // var err = eval("(" + xhr.responseText + ")");
        // alert(err.Message);
        $("#mailError").removeAttr("hidden");
        // $(".form-group").hide();
        $('.contactus').css('background','#fcf8e3');
        console.log(response);
        // console.log(status);
      }

    });
  });

});