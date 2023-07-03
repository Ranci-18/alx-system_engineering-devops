# installs nginx server with custom http header
exec { 'update':
    command => 'sudo apt-get -y update',
}
-> package {'nginx':
    ensure => 'present',
}
-> file_line { 'http_header':
    path  => '/etc/nginx/nginx.conf',
    line  => "http {\n\tadd_header X-Served-By \"$HOSTNAME\";/",
    match => 'http {',
}
-> exec {'start':
    command => 'sudo service nginx start'
    path    => '/usr/sbin'
}
