Exec {
	path=> ["/usr/bin", "/bin", "/usr/sbin", "/sbin", "/usr/local/bin", "/usr/local/sbin"]
}


class { 'python':
  version => 'system',
  dev => true,
  virtualenv => true,
}

python::virtualenv { '/home/vagrant/venv':
  ensure => present,
  version => 'system',
  requirements => '/vagrant/requirements.txt',
  systempkgs => true,
}

