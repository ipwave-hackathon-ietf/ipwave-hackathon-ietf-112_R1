const express = require("express");
const app=express();
const wsModule=require('ws');


app.use("/",(req,res)=>{
	//res.sendFile('./index.html'));
	console.log("hi");
});

const HTTPServer=app.listen(9999,()=>{
	console.log("server is open at port:9999");
});

const webSocketServer=new wsModule.Server({
	server:HTTPServer,
});


webSocketServer.on('connection',(ws, request)=>{

	const ip=request.headers['x-forwarded-for']||request.connection.remoteAddress;
	console.log(`NEW CLIENT [${ip}] connected`);

	ws.on('message',(msg)=>{
		console.log(`received message : ${msg}`);
	})

});
