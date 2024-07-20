1. **Build da Imagem Docker:**

   ```bash
   docker build -t tech-challenge-phase-1-api:latest .
   ```

2. **Taguear a Imagem:**

   ```bash
   docker tag tech-challenge-phase-1-api:latest 195041288846.dkr.ecr.us-east-1.amazonaws.com/project-01:latest
   ```

3. **Login no ECR:**

   ```bash
   aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 195041288846.dkr.ecr.us-east-1.amazonaws.com
   ```

4. **Push da Imagem:**

   ```bash
   docker push 195041288846.dkr.ecr.us-east-1.amazonaws.com/project-01:latest
   ```

Certifique-se de que os comandos estejam corretos e execute-os novamente. Aqui está um exemplo completo:

```bash
# Build the Docker image
docker build -t tech-challenge-phase-1-api:latest .

# Tag the Docker image
docker tag tech-challenge-phase-1-api:latest 195041288846.dkr.ecr.us-east-1.amazonaws.com/project-01:latest

# Login to ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 195041288846.dkr.ecr.us-east-1.amazonaws.com

# Push the Docker image to ECR
docker push 195041288846.dkr.ecr.us-east-1.amazonaws.com/project-01:latest
```

Verifique também se a imagem `tech-challenge-phase-1-api:latest` realmente existe localmente antes de tentar tagueá-la e enviá-la para o ECR:

```bash
docker images
```