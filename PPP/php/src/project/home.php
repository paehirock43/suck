<?php 
    ob_start();
    session_start();
    require "config/config_db.php";
    $strSQL = "SELECT id,name,session FROM customer WHERE session='".session_id()."'";
    $query = @mysqli_query($conn,$strSQL);
    $resultQuery = @mysqli_fetch_array($query);
    if(@$resultQuery['id']!="" ){
        //print_r("show form");
    } else{
        //print_r("go to login");
        header("location:http://localhost:8080/project/login.php");     
    }
        
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HOME</title>
    <link rel="stylesheet" type="text/css" href="./css/main_style.css"  >
</head>

<body>
    <header style="background-color: #574b90 ;">
     <h1> Header </h1>
    </header>
    <div class="row" style="background-color: #EEE3CB;">  
          <nav class="column menu" style="background-color: #778beb ;">
          <h2>Menu</h2> 
            <ul>
            <li><a href="#">Menu 1</a></li>
            <li><a href="#">Menu 2</a></li>
            </ul>
        </nav>
          <div class="column content" style="background-color:#786fa6 ;"> 
          <h2>Content</h2>
        </div>
    </div>
        <footer style="background-color: #546de5">
            <p>Footer</p>
        </footer>
</body>
</html>