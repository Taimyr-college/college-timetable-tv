
//<?php header("Refresh: 1");
//?>

<?php // проверка расписания на завтра
$filename = "web_images/R/tomorrow/1.png";

if (file_exists($filename)) {
    $tomorrow = True;
} else {
    $tomorrow = False;
}
?>

<?php // какое расписание показать
if ($tomorrow) {
    require 'timeTomorrowpc.html';
} else {
    require 'timeTodaypc.html';
}
?>

