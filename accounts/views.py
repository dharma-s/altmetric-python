# accounts/views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from .models import CustomUser

@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login(request):
    email = request.data["username"]
    password = request.data["password"]

    try:
        user = CustomUser.objects.get(username=email)
        if user.check_password(password):
            token = Token.objects.get_or_create(user=user)[0]
            return Response(
                {
                    "status_code": "1",
                    "auth_token": "%s" % token
                }
            )
        else:
            return Response({"status_code": "0", "message": "Invalid password..."})
    except CustomUser.DoesNotExist:
        return Response({"status_code": "0", "message": "User not found..."})
    except Exception as e:
        return Response({"status_code": "0", "message": "{}".format(e)})

@api_view(["POST"])
def profile(request):
    email = request.data["username"]
    password = request.data["password"]

    try:
        user = CustomUser.objects.get(username=email)
        if user.check_password(password):
            token = Token.objects.get_or_create(user=user)[0]
            return Response(
                {
                    "status_code": "1",
                    "auth_token": "%s" % token
                }
            )
        else:
            return Response({"status_code": "0", "message": "Invalid password..."})
    except CustomUser.DoesNotExist:
        return Response({"status_code": "0", "message": "User not found..."})
    except Exception as e:
        return Response({"status_code": "0", "message": "{}".format(e)})
