<?php
    session_start();
    //print_r(session_id());
    //exit;
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" type="text/css" href="./css/main_style.css" >
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
</head>
<body style="background-color:black;">
  <div class="row" style="background-color:#ffff;">
    <div class="column">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-4" style="background-color:#ffff; border-radius: 1.25rem;">
                    <p align="center"> <img src="./assets/image/LOGO.jpg" width="200" height= "190"></p>
                      <h2 style="color:darkslategray">Login</h2>
                    <form>
                        <div class="form-group">
                            <label for="username">Username</label>
                            <input type="text" class="form-control" id="username" placeholder="Enter username">
                        </div>
                        <div class="form-group">
                            <label for="password">Password</label>
                            <input type="text" class="form-control" id="password" placeholder="Enter password">
                            <h2></h2>
                        </div>
                        <div class="form-group" align="center">
                            <button type="submit" class="btn btn-primary">login</button>
                            <h2></h2>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
  </div>
  <footer>
    <p>footer</p>
  </footer>
</body>
</html>
<script type= text/javascript>
</script>
<script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
<script type= text/javascript>
   var session = "<?php echo session_id(); ?>";
   console.log(session);
  /* let y =20;
   z=30;
    console.log("Hello world JS");*/

    //login();
    function login(){
        console.log("Hello function");
        let username ;
        let password ;
        username = document.getElementById("username").value;
        //console.log(username);
        password = document.getElementById("password").value;
        //console.log(password); 
        let request_data ={
            "email":username , 
            "password":password,
            "session":session
        }
        console.log(request_data);
        let uri = "http://localhost:8080/project/api/get_customer_login.php";
        //document.getElementById("username").value = "ku@gmail.com";
        $.ajax({
            type:"POST",
            url:uri,
            async:false,
            data:JSON.stringify(request_data),
            success:function(response){
                console.log("Connect SUCCESS...........");
                console.log(response);
                console.log(response.result);
                console.log(response.message);
                if(response.result===1){
                    console.log("go to home.php");
                    window.location.replace("http://localhost:8080/project/home.php");
                }else {
                    console.log("redirect to log.php")
                    document.getElementById("username").value ="";
                    document.getElementById("password").value ="";
                    document.getElementById("username").focus() ;
                    alert("เข้าสู่ระบบไม่สำเร็จ");
                }
            },error:function(error){
                console.log(error);
            }
        });
    }
</script>