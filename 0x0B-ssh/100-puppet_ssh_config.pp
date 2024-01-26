# Connects to a server using SSH without Password

exec { 'echo "PasswordAuthentification no\nIdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config':
	path	=> '/bin/'
}
