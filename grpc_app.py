
from mask import Mask
# project
from protos.hello_pb2 import HelloResponse


app = Mask(__name__)
app.config["REFLECTION"] = True
app.config["HEALTH"] = True


@app.route(method="SayHello", service="Hello")
def say_hello_handler(request, context):
    """ Handler SayHello request
    """
    return HelloResponse(message="Hello Reply: %s" % request.name)


if __name__ == "__main__":
    app.run(port=1020)