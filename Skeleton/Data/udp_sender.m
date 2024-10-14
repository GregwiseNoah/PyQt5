
serverIP = '127.0.1.1'; 
serverPort = 5050;     

udpSender = udpport();

loadedData = load('Fwd_I.mat'); 


dataToSend = loadedData.Fwd_I.Data(3,:);


write(udpSender, dataToSend, serverIP, serverPort);