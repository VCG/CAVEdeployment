source env_config.sh
source $ENV_REPO_PATH/$1.sh

gcloud config set project $PROJECT_NAME
gcloud config set compute/region $ZONE
gcloud container clusters get-credentials $CLUSTER_NAME --zone $ZONE