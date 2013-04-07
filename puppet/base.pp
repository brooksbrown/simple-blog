$venv_path = '/home/vagrant/venv'


Exec {
	path=> ["/usr/bin", "/bin", "/usr/sbin", "/sbin", "/usr/local/bin", "/usr/local/sbin"]
}

class { 'python':
    virtualenv => true,
}

python::virtualenv { $venv_path:
	ensure => present,
	requirements => '/vagrant/requirements.txt',
}

exec { 'cleanup':
	command => 'rm /vagrant/requirements.txt.sha1',	
	require => python::virtualenv[$venv_path],
}
