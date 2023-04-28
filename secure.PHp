<?php
$file = $_SERVER['DOCUMENT_ROOT'] . '/index.php';
$mode = 0644;

if (chmod($file, $mode)) {
    echo "Hak akses berkas $file berhasil diubah menjadi $mode";
} else {
    echo "Gagal mengubah hak akses berkas $file";
}
