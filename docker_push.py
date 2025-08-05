import docker
import sys

def push_docker_image(image_name='my-app', tag='latest'):
    try:
        client = docker.from_env()
        print(f"⬆️ Pushing Docker image: {image_name}:{tag}")
        response = client.images.push(image_name, tag=tag, stream=True, decode=True)
        for line in response:
            if 'status' in line:
                print(line['status'])
            elif 'error' in line:
                print(f"❌ Error: {line['error']}")
                sys.exit(1)
        print(f"✅ Image pushed successfully: {image_name}:{tag}")

    except docker.errors.APIError as e:
        print(f"❌ Docker API error: {e}")
        sys.exit(1)

    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    push_docker_image(image_name='my-app', tag='v1.0.0')
