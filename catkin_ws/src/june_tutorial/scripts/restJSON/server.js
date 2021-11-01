//import { WebSocketServer} from 'ws';
const jsonServer=require('json-server');
const server=jsonServer.create();
const path=require('path');
const router=jsonServer.router(path.join(__dirname,'db.json'));
const middlewares=jsonServer.defaults();

server.use(middlewares);

server.use(jsonServer.bodyParser);

server.use(router);

let port=5055;
server.listen(port,()=>{
	console.log(`JSON server is running on port ${port}`)
})

/////////////////////////////////////////////////////////////

const dgram=require('dgram');
const server_ws = dgram.createSocket('udp4');

server_ws.on('error', (err) => {
	console.log(`server error:\n${err.stack}`);
  	server_ws.close();
});

server_ws.on('message', (msg, rinfo) => {
	const json=JSON.parse(msg.toString());
	console.log(json.posex);
	//console.log(json["posex"]);
	//console.log(msg.toString());
  	//console.log(`server got: ${msg} from ${rinfo.address}:${rinfo.port}`);
});

server_ws.on('listening', () => {
  	const address = server_ws.address();
  	console.log(`server listening ${address.address}:${address.port}`);
});

server_ws.bind({
        address:'localhost',
        port:9998,
        exclusive: true
});
// Prints: server listening 0.0.0.0:41234
//
//
// ///////////////////////////////////////////////

