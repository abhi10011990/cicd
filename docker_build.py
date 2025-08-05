import docker
import sys

def build_docker_image(dockerfile_path='.', image_name='my-image', tag='latest'):
    try:
        client = docker.from_env()

        print(f"🔨 Building Docker image: {image_name}:{tag}")
        image, logs = client.images.build(path=dockerfile_path, tag=f"{image_name}:{tag}")

        for chunk in logs:
            if 'stream' in chunk:
                print(chunk['stream'].strip())

        print(f"✅ Image built successfully: {image.tags}")

    except docker.errors.BuildError as e:
        print(f"❌ Docker BuildError: {e}")
        sys.exit(1)

    except docker.errors.APIError as e:
        print(f"❌ Docker APIError: {e}")
        sys.exit(1)

    except docker.errors.DockerException as e:
        print(f"❌ General Docker error: {e}")
        sys.exit(1)

    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    build_docker_image(
        dockerfile_path='.',        # Path to Dockerfile
        image_name='my-app',        # Image name
        tag='v1.0.0'                # Image tag
    )

