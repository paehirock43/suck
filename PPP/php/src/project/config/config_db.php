<?php
    $serverName = "db"; #localhost:9906 #127.0.0.1:9906
    $userName = "root";
    $userPassword = "MYSQL_ROOT_PASSWORD";
    $dbName = "MYSQL_DATABASE";   
    #localhost:8080/project/config/config_db.php
?>
<?php
    $conn = @mysqli_connect($serverName,$userName,$userPassword,$dbName);
?>
<?php
    @date_default_timezone_set("Asia/Bangkok");
    @mysqli_set_charset($conn, "utf8");
    @mysqli_query($conn,"SET NAMES UTF8");
?>
<?php
    /**$strSQL="SELECT * FROM customer";
    $query = @mysqli_query($conn,$strSQL);  
    while($resultObj = @mysqli_fetch_array($query,MYSQLI_ASSOC)){
        print_r($resultObj);
    }
    */
?>

