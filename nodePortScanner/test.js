'use strict';

const scanPorts = require('./nodePortScanner');

scanPorts('192.168.1.1', 1, 65535, (ports) => {
    console.log('open ports: ', ports);
});