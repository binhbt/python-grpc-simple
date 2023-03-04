# python-grpc-simple.  
virtualenv -p python3 env. 
source env/bin/activate. 
pip install grpcio-tools==1.33.2. 
python3 -m grpc_tools.protoc --proto_path=. ./greeting.proto --python_out=. --grpc_python_out=.  

# Server up. 
python /build/grpc/grpc_client_test.py   
# test Client.  
python /build/grpc/grpc_client_test.py    
