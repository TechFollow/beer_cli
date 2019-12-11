#! /usr/bin/php
<?php


if (PHP_SAPI !== 'cli') {
    exit;
}

require __DIR__ . '/vendor/autoload.php';

use BeerCli\Cli;

$cli = new Cli();
$cli->exec($argv);