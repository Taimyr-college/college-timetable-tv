<?php // проверка расписания на завтра
$filename = "../../00_tomorrow/0.png";

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

