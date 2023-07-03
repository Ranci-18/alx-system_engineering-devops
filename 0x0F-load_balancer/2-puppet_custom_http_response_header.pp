# installs nginx server with custom http header
exec { 'update':
    command => 'sudo apt-get -y update',
    path => '/usr/bin',
    before => Exec ['install Nginx'],    
}

exec { 'install Nginx':
    command => 'sudo apt-get -y install nginx',
    path => '/usr/bin',
    before => Exec['add_header'],
}

exec { 'add_header':
    environment => ["HOSTNAME=$hostname"],
    command => 'sudo sed -i "s/http {/http {\n\tadd_header X-Served-By \"$HOSTNAME\";/" /etc/nginx/nginx.conf',
    path => '/usr/bin',
    before => Exec['restart Nginx],
}

exec {'restart Nginx':
    command => 'sudo service nginx restart',
    path => '/usr/bin',
}
