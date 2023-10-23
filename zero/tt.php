<?php header("Refresh: 1800");?>

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
    require 'timeTomorrow.html';
} else {
    require 'timeToday.html';
}
?>

