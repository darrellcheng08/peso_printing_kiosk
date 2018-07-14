<!DOCTYPE html>
<html>
<meta http-equiv="content-type" content="text/html;charset=UTF-8" />
<head>
  <title>Flash Drive Form</title>
  <meta charset="utf-8" />
  <link rel="stylesheet" type="text/css" href="css/bootstrap.css">
</head>

<body style="padding: 20px;">
  <div style="margin-top: 100px;" class="row">
    <h1 class="text-center" style="margin-top:-70px;margin-bottom: 20px;">Welcome to Printing Kiosk</h1>
    <div class="col-md-4"></div>
    <div class="col-md-4">
      <div class="panel panel-primary">
        <div class="panel-heading">Printing Kiosk</div>
        <div class="panel-body">
          <form id="formdata" action="function.php" method="post" enctype="multipart/form-data">
            <input type="hidden" name="txtpages" id="txtpages">
            <input type="hidden" name="txtcredits" id="txtcredits">
            <div class="form-group">
              <label>Choose file to print:</label>
              <input type="file" name="txtfilename" class="form-control" accept=".doc, .docx, .pdf" id="filename" required>
            </div>
            <div id="display" style="display:none;">
              <div class="form-group">
                <label>Number of page(s):</label> <label id="numpages"></label>
              </div>
              <div class="form-group">
                <label>Credit(s):</label> <label id="credits"></label>
              </div>
              <div class="form-group">
                <label>Number of copies:</label>
                <input type="text" name="txtnumcopy" class="form-control" id="txtnumcopy">
              </div>
              <div class="form-group">
                <label>Color:</label>
                <select class="form-control" name="txtcolor">
                  <option value="print-black">Black</option>
                  <option value="print-color">Colored</option>
                </select>
              </div>
              <a id="btnpreview" target="_blank" name="btnpreview" class="btn btn-success">Preview</a>
              <button type="submit" name="btnprint" class="btn btn-primary">Print</button>
            </div>
          </form>
        </div>
        <div class="panel-footer">
          <a href="index.php" class="btn btn-default">Cancel</a>
          <a id="makediscoverable" class="btn btn-info">Connect to Bluetooth</a>
        </div>
      </div>
    </div>
    <div class="col-md-4"></div>
  </div>
  <script src="js/jquery.min.js"></script>

  <script>
    $("#filename").on("change", function (e) {
      var file = $(this).val();
      var filename = $(this)[0].files[0].name;
      var name = filename.split('.');
      $('#btnpreview').prop('href', name[0]+'.pdf');
      if (file != "") {
        $('#display').show();
        form_data = new FormData();
        var file_data = $(this)[0].files[0];
        form_data.append("file", file_data);
        $.ajax({
          data: form_data,
          type: "POST",
          url: "getpages.php",
          cache: false,
          contentType: false,
          processData: false,
          success : function(res){
            $('#numpages').html(res);
            $('#txtpages').val(res);
          }
        })
      }else{
        $('#display').hide();
      }
      setInterval(function() { getCredit(); }, 2000);
    })

    function getCredit()
    {
      var credits = 0;
      $.ajax({
        type: "POST",
        url: "function.php",
        data: { getCredits:1 },
        success : function(res){
          $('#credits').html(res);
          $('#txtcredits').val(res);
        }
      })
    }

    $('#makediscoverable').click(function(){
      $.ajax({
        type: "POST",
        url: "function.php",
        data: { makediscoverable:1 },
        success : function(res){
          alert("Successfully Bluetooth Discoverable to User.")
        }
      })
    })
</script>
</body>
</html>