<?php
    session_start();
    /*print_r(session_id());
    exit;*/
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
    <link rel ="stylesheet" type="text/css" href= "./css/main_style.css">
</head>
<body>   

    <div  class="row" align="center" >
        <div class="column content ">
            <div class="container" align="left">
                <div class="row justify-content-center">
                    <div class="col-4" style="background-color: pink; padding:10px; border-radius:25px" >
                        <div align = "center"><img src="assets/images/logo.png" width="200px" height="200px"/></div>
                        <h2>Form Login</h2>
                        <form id="fr_login" name="fr_login" >
                            <div class="form-group space_box">
                                <label for="username" class="form-label">Username</label>
                                <input type="text" class="form-control" id="username" placeholder="Enter username">
                            </div>
                            <div class="form-group space_box">
                                <label for="password">Password</label>
                                <input type="password" class="form-control" id="password">
                            </div>
                            <div class="space box" align="center">
                                <button type="button" class="btn btn-primary" style="padding: 10px 20px 10px 20px" onclick="login()">Login</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <footer>
        <p> Footer </p>
    </footer>

</body>
</html>
<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
<script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
<script type=text/javascript>
    var session = "<?php echo session_id(); ?>";
    function login(){
        let username;
        let password;
        username = document.getElementById("username").value;
        password=document.getElementById("password").value;
        let request_data = {
            "email":username,
            "password":password,
            "session":session
        }
        console.log(request_data);
        let uri = "http://localhost:8080/api/get_customer_login.php";
        //url = Uniform Resource Locator
        //uri = Uniform Resource Identifie
        $.ajax({
            type:"POST",
            url:uri,
            async:false,
            data:JSON.stringify(request_data),
            success:function(response){
                console.log("connect success..."); 
                console.log(response);
                console.log(response.result);
                console.log(response.message);
                if(response.result===1){
                    //console.log("go to home.php");
                    window.location.replace("http://127.0.0.1:8080/home.php");
                }else{
                    //console.log("go to login.php");
                    document.getElementById("username").value ="";
                    document.getElementById("password").value ="";
                    document.getElementById("username").focus();
                    alert("เข้าสู่ระบบไม่สำเร็จ"); 
                }
            },error:function(error){
                console.log(error);
            }
        });

    }
</script>