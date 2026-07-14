Application - Initial Version

This screenshot shows the first version of the Docker Todo Application developed using Flask and MySQL. It demonstrates the basic functionality for displaying and managing todo tasks before the user interface was enhanced.

⸻

Application - CRUD Operations

This version demonstrates the implementation of CRUD functionality. Users can add new tasks, view existing tasks, and delete completed or unwanted tasks, confirming successful integration between the Flask application and the MySQL database.

⸻

Application - Final User Interface

The final version of the application features a responsive Bootstrap interface with task management capabilities, including task creation, created date, due date, status tracking (Pending/Completed), and complete/delete actions. This represents the finished web application deployed using Docker.

⸻

Microsoft Azure Deployment

The application is deployed on Microsoft Azure using an Azure Web App running a Docker container. This demonstrates cloud deployment, making the application accessible over the internet while leveraging Azure’s managed hosting platform.

⸻

GitHub Actions CI/CD Pipeline

GitHub Actions automates the CI/CD workflow by checking out the source code, building the Docker image, pushing it to Docker Hub, and deploying the latest version to Microsoft Azure. The successful workflow execution confirms that the application is continuously integrated and deployed automatically.

⸻

Project Architecture

This architecture illustrates the complete DevOps workflow. The developer pushes code to GitHub, GitHub Actions performs automated build and deployment, Docker images are stored in Docker Hub, and the application is deployed on Microsoft Azure using Docker Compose. Nginx acts as a reverse proxy for the Flask application, while MySQL stores application data using a persistent Docker volume. The application is publicly accessible through its Azure endpoint.
