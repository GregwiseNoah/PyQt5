% Define the IP address and port of the Python UDP server
serverIP = '127.0.0.1';  % Localhost (change to the actual IP address if needed)
serverPort = 5050;      % Port to send data to

% Create a UDP object
udpSender = udpport("datagram", "IPV4");

% Load the .mat file
loadedData = load('Fwd_I.mat'); 

% Assume your data is stored in a variable called 'myData' inside the .mat file
% Extract the numeric array from the loaded data
dataToSend = loadedData.Fwd_I.Data(3,:);  % Adjust 'myData' to match your variable name

% Check if the data is in the correct numeric format
if ~isnumeric(dataToSend)
    error('The loaded data is not numeric. Please check your .mat file.');
end

% Convert the numeric data to bytes before sending
% Let's assume the data is in double-precision floating-point format (8 bytes per double)
dataInBytes = typecast(dataToSend(:), 'uint8');  % Flatten data and convert to bytes

% Send the data in chunks if needed (UDP can have limitations on packet size)
maxPacketSize = 65535;  % Adjust the packet size as needed

% Split the data into packets and send over UDP
numPackets = ceil(numel(dataInBytes) / maxPacketSize);
for i = 1:numPackets
    startIdx = (i-1) * maxPacketSize + 1;
    endIdx = min(i * maxPacketSize, numel(dataInBytes));
    write(udpSender, dataInBytes(startIdx:endIdx), "uint8", serverIP, serverPort);
    pause(0.1);  % Optional: a small pause between packets, adjust as necessary
end

% Cleanup
clear udpSender;
disp('Data has been sent over UDP.');
