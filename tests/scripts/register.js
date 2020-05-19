const KNoTCloudWebSocket = require('@cesarbr/knot-cloud-websocket');

// Receber argumentos para passar pro script 
var myArgs = process.argv.slice(2);
type_arg = myArgs[0]
name_arg = myArgs[1]

const client = new KNoTCloudWebSocket({
  protocol: 'wss',
  hostname: 'ws.knot.cloud',
  port: 443,
  pathname: '/',
  id: '78159106-41ca-4022-95e8-2511695ce64c',
  token: 'd5265dbc4576a88f8654a8fc2c4d46a6d7b85574',
});

client.on('ready', () => {
  client.register({
    id: '6e5a681b2ae7be40',
    type: type_arg,
    name: name_arg,
  });
});
client.on('registered', (thing) => {
  console.log(thing);
  client.close();
});
client.on('error', (err) => {
  console.error(err);
  console.log('Connection refused');
  client.close();
});
client.connect();