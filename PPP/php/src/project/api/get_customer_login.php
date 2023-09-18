<?php ob_start();?>
<?php
    #header
    @header('Content-Type: application/json');
    @header("Access-Control-Allow-Origin: *");
    @header('Access-Control-Allow-Headers: X-Requested-With, content-type, access-control-allow-origin, access-control-allow-methods, access-control-allow-headers');
?>
<?php
    #connection include  OR require
    require ("../config/config_db.php");
    //print_r($conn);
?>
<?php
    #input
    if($_SERVER["REQUEST_METHOD"] == "POST"){
       // print_r("POST");
        $content = @file_get_contents('php://input');
        $json_data = @json_decode($content, true);
        $inputEmail = $json_data["email"];
        $inputPassword = $json_data["password"];
        $session = trim($json_data["session"]);
    }else {
       // print_r("OTHER");
       ob_end_clean();
       @header("HTTP/1.0 420 Precondition Failed");
       die();
    }
?>
<?php
    #process
    $strSQL="SELECT * FROM customer WHERE email = '".$inputEmail."' ";
    $query = @mysqli_query($conn,$strSQL);
    $resultQuery = @mysqli_fetch_array($query);
    //print_r($resultQuery);
    if(trim($resultQuery['email'])!="" && trim($resultQuery['password']) == $inputPassword){
        //print_r("YES");
        $result=1;
        $message="เข้าสู่ระบบ";
        $strSQL ="UPDATE customer SET session = '".$session."' WHERE email ='".$resultQuery['email']."'";
        $query = @mysqli_query($conn,$strSQL);
    } else{
       // print_r("NO");
       $result=0;
       $message="เข้าสู่ระบบไม่เสร็จ";
    }
?>
<?php
    #output
    ob_end_clean();
    @mysqli_close($conn);
    echo $json_response = json_encode(array("result"=>$result,"message"=>$message));
    _log_customer_login($content,$json_response);
    exit;
?>
<?php
    #log function
    function _log_customer_login($content,$json_response){
        $ip = $_SERVER['REMOTE_ADDR'];
        $date = @date("Y-m=d H:i:s");
        $_log = "\n".$date."  ".$ip." request:".$content." response:".$json_response;
        $objFopen=@fopen("log/_log_customer_login.log","a+");
        @fwrite($objFopen,$_log);
        @fclose($objFopen);
    }
?>