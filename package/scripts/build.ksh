#if [ -z "$DOCKER_HOST" ]; then
#   echo "ERROR: no DOCKER_HOST defined"
#   exit 1
#fi

echo "*****************************************"
echo "building on $DOCKER_HOST"
echo "*****************************************"

if [ -z "$DOCKER_HOST" ]; then
   DOCKER_TOOL=docker
else
   DOCKER_TOOL=docker-17.04.0
fi

# set the definitions
INSTANCE=dh-abstracts
NAMESPACE=uvadave

# build the image
$DOCKER_TOOL build -f dh_abstracts/Dockerfile -t $NAMESPACE/$INSTANCE .

# return status
exit $?
