#Creating a file using puppet

file { 'school':
  ensure => 'present',
  path => '/tmp/school',
  content => 'I love puppet',
  owner => 'www-data',
  group => 'www-data',
  mode => '0744'
}
