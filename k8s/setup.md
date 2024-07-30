1. **Build da Imagem Docker:**

   ```bash
   docker build -t tech-challenge-phase-1-api:latest .
   ```
2. **Em caso de uso da aws**

   2.1. **Taguear a Imagem:**
   ```bash
   docker tag tech-challenge-phase-1-api:latest 195041288846.dkr.ecr.us-east-1.amazonaws.com/project-01:latest
   ```
   2.2. **Login no ECR:**
      ```bash
      aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <<aws_id>>.dkr.ecr.us-east-1.amazonaws.com
      ```
   2.3. **Push da Imagem:**
      ```bash
      docker push <<aws_id>>.dkr.ecr.us-east-1.amazonaws.com/project-01:latest
      ```
   2.4. **Carregar contexto do EKS**
      ```bash
      aws eks --region us-east-1 update-kubeconfig --name project-01
      ```

3. **Em caso de uso do minikube local**

   3.1. **Carregando a imagem**
      ```bash
      minikube image load tech-challenge-phase-1-api:latest
      ```
   3.2. **Start do service**
      ```bash
      minikube service tech-challenge-phase-1-api-service
      minikube tunnel #para habilitar serviços de loadbalancer
      ```

4. **Aplicar e verificar recursos**

   ```bash
   kubectl get configmap alembic-config -o yaml
   kubectl apply -f k8s/

   kubectl get all

   kubectl logs <pod-name>
   kubectl describe pod <pod-name>
   ```

5. **Testar escalagem de pods**
   Cheque o hpa:
   ```bash
   kubectl get hpa
   ```
   Gere uma carga de CPU nos pods da sua aplicação:
   ```bash
   kubectl run -i --tty load-generator --image=busybox /bin/sh
   while true; do wget -q -O- http://tech-challenge-phase-1-api-service; done
   ```
   Monitore o comportamento do HPA e o escalonamento dos pods e depois limpe os recursos
   ```bash
   kubectl get hpa -w
   kubectl delete pod load-generator
   ```



6. **Acessar o banco de dados**
Para realizar uma operação de GET (consulta) nos bancos de dados em um ambiente Kubernetes, você precisará acessar os bancos de dados de dentro dos pods ou usar uma ferramenta de administração de banco de dados que possa se conectar ao seu banco de dados rodando no Kubernetes. Aqui está um guia geral para diferentes bancos de dados:


### Acessar o Pod:

   Primeiro, obtenha o nome do pod onde o PostgreSQL está rodando:

   ```bash
   kubectl get pods
   ```

   Acesse o pod com:

   ```bash
   kubectl exec -it <pod-name> -- /bin/bash
   ```

2. **Conectar ao Banco de Dados:**

   Dentro do pod, use o comando `psql` para conectar ao banco de dados:

   ```bash
   psql -h <postgres-service> -U <username> -d <database>
   ```

   Por exemplo:

   ```bash
   psql -h postgres-service -U postgres -d mydatabase
   ```

3. **Executar a Consulta:**

   Dentro do `psql`, execute a consulta desejada, por exemplo:

   ```sql
   SELECT * FROM mytable;
   ```