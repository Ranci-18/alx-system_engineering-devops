# Request limit fix

exec {'replace':
    provider => shell,
    command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-N 4096\"/" /etc/default/nginx',
    before   => Exec['restart'],
}

exec {'restart':
    provider => shell,
    command  => 'sudo service nginx restart',
}
