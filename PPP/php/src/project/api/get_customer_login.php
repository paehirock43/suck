<?php ob_start();?>
<?php
    #header
    header('Content-Type: application/json');
    header("Access-Control-Allow-Origin: *");
    header('Access-Control-Allow-Headers: X-Requested-With, content-type, access-control-allow-origin, access-control-allow-methods, access-control-allow-headers'); 

?>
<?php
    #connection and data include  OR require
    require ("../config/config_db.php");
    if (isset($json_data["email"]) && isset($json_data["password"])) {
        $inputEmail = $json_data["email"];
        $inputPassword = $json_data["password"];
    } else {
        // หากข้อมูลไม่ถูกต้อง ให้ส่งข้อผิดพลาดกลับ
        echo json_encode(array("result" => 0, "message" => "Invalid JSON data"));
        exit;
    }
    //print_r($conn);
?>
<?php
    #input
    $inputEmail = "";
    if($_SERVER["REQUEST_METHOD"]=="POST"){
        print_r("POST");
        $content = file_get_contents('php://input');
        $json_data = json_decode($content,true);
        $inputEmail=$json_data["email"];
        $inputPassword=$json_data["password"];
        //print_r($json_data["email"]);
    }
    else{
        print_r("OTHER");
    }
?>
<?php
    #process
    $strSQL="SELECT*FROM customer Where email='".$inputEmail."' ";
    $query=mysqli_query($conn,$strSQL);
    $resultQuery=mysqli_fetch_array($query);
    print_r($strSQL);
    if(trim(($resultQuery['email'])!="") && trim($resultQuery['password'])==$inputPassword){
       // print_r("YES");
       $result=1;
       $message="login";
    }
    else{
       // print_r("NO");
       $result=0;
       $message="can't login";
    }
?>
<?php
    #output
    ob_end_clean();
    mysqli_close($conn);
    echo $json_response = json_encode(array("result"=>$result,"message"=>$message));
    _log_customer_login($content,$json_response);
    exit;
?>
<?php
    #log function
    function _log_customer_login(){
        $ip=$_SERVER['REMOTE_ADDR'];
        $date=date("Y-m-d H:i:s");
        $_log = "\n".$date."".$ip."request:".$content."response:".$json_response;
        $objFopen= fopen("log/_log_customer_login.log","a+");
        fwrite($objFopen,$_log);
        fclose($objFopen);
    } 
?>