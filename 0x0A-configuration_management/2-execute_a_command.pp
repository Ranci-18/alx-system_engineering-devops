# Puppet manifest uses exec and pkill to kill a process
# named killmenow
exec { 'killmenow':
    command => 'pkill killmenow',
    path    => '/usr/bin/',
}
