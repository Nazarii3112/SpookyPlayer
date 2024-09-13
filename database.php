<?php
// Параметри підключення до MySQL
$host = 'sql204.infinityfree.com';
$dbname = 'if0_37045349_spookydb';
$user = 'if0_37045349';
$password = 'd31122009D';

// Підключення до MySQL
$mysqli = new mysqli($host, $user, $password, $dbname);

// Перевірка з'єднання
if ($mysqli->connect_error) {
    die(json_encode(["error" => "Помилка підключення до MySQL: " . $mysqli->connect_error]));
}

// Виконання запиту для отримання треків
$query = "SELECT title, artist, online_url FROM tracks";
$result = $mysqli->query($query);

$tracks = [];
if ($result) {
    while ($row = $result->fetch_assoc()) {
        $tracks[] = $row;
    }
}

echo json_encode($tracks);  // Виводимо дані у форматі JSON

// Закриття з'єднання
$mysqli->close();
?>
