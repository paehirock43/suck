<?php
    $serverName = "db"; #localhost:9906 #127.0.0.1:9906
    $userName = "root";
    $userPassword = "MYSQL_ROOT_PASSWORD";
    $dbName = "MYSQL_DATABASE";   
    #localhost:8080/project/config/config_db.php
?>
<?php
    $conn = @mysqli_connect($serverName,$userName,$userPassword,$dbName);
    if (!$conn) {
    die("การเชื่อมต่อล้มเหลว: " . mysqli_connect_error());
}
?>
<?php
    date_default_timezone_set("Asia/Bangkok");
    mysqli_set_charset($conn, "utf8");
    mysqli_query($conn,"SET NAMES UTF8");
?>
<?php
    $strSQL="SELECT * FROM customer";
    $query = mysqli_query($conn,$strSQL);
    if($query){
        while($resultObj = mysqli_fetch_array($query,MYSQLI_ASSOC)){
            print_r($resultObj);
        }
    } else {
        echo "ไม่สามารถส่งคำสั่ง SQL ได้: " . mysqli_error($conn);
    }

?> 
