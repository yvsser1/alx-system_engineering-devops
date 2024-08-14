# Fixes a typo in the WordPress settings file that causes Apache to return a 500 error

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin:/bin/',
  onlyif  => 'grep -q "phpp" /var/www/html/wp-settings.php',
}
