# python-grpc-simple.  
virtualenv -p python3 env.  
source env/bin/activate.  
pip install grpcio-tools==1.33.2.  
python3 -m grpc_tools.protoc --proto_path=. ./protos/greeting.proto --python_out=. --grpc_python_out=.   

# Server up. 
python grpc_client_test.py   
# Test Client.  
python grpc_client_test.py    
