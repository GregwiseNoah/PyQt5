
serverIP = '127.0.1.1'; 
serverPort = 5050;     
loadedData = load('Fwd_I.mat'); 


udpSender = udpport();

dataToSend = loadedData.Fwd_I.Data(3,:);

write(udpSender, dataToSend, serverIP, serverPort);