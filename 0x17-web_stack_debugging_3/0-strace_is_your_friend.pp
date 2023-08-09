# fix 500 internal server error when sending a GET method

exec {'replace':
    provider => shell,
    command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
