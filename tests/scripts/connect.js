const KNoTCloudWebSocket = require('@cesarbr/knot-cloud-websocket');

// Receber argumentos para passar pro script 
var myArgs = process.argv.slice(2);
protocol_arg = myArgs[0]
hostname_arg = myArgs[1]
port_arg =  myArgs[2]

const client = new KNoTCloudWebSocket({
  protocol: protocol_arg,
  hostname: hostname_arg,
  port: port_arg,
  pathname: '/',
  id: '78159106-41ca-4022-95e8-2511695ce64c',
  token: 'd5265dbc4576a88f8654a8fc2c4d46a6d7b85574',
});

client.on('ready', () => {
  console.log('Connection established');
  process.exit()
});
client.on('error', (err) => {
  console.error(err);
  console.log('Connection refused');
  process.exit()
});
client.connect();
