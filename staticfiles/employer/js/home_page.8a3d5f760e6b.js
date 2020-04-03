 
  function add_employee(){
    document.getElementById("add_employee_submit").click();
  }


  function edit_employee(){

    //close the modal
    $("#edit_employee").modal('hide');

    //get the ID from the hidden field
    var employee_id = $('#employee_id').val(); //ISYED_CHANGE TO ID
    var url_str = "/edit_employee/" + employee_id;

    //set the form=edit_employee_form action attribute to the correct url ('edit_employee/last_name')
    $('#edit_employee_form').attr("action", url_str);
    //click the (edit_employee_submit)
    $('#edit_employee_submit').click();
  }

  

  function load_picture(element_id,image_id){
      url = document.getElementById(element_id).value;
      if (url === ""){

      }else{
        document.getElementById(image_id).setAttribute('src',url);
      }

    }


  