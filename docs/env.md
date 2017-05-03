## 环境搭建

### 搭建gitlab

1. 安装gitlab

   ```
   docker pull sameersbn/gitlab:latest

   wget https://raw.githubusercontent.com/sameersbn/docker-gitlab/master/docker-compose.yml

   docker-compose up

   ```

   ​

2. 安装gcilab-ci

   ```
   docker run -d --name gitlab-runner --restart always \
   -v /var/run/docker.sock:/var/run/docker.sock \
   -v /Users/ahprosim/tmp:/etc/gitlab-runner \
   gitlab/gitlab-runner:latest
   ```

   ​



