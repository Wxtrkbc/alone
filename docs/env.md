## 环境搭建

### 搭建gitlab

1. 安装gitlab

   ```
   docker pull sameersbn/gitlab:latest


   ```

   ​

2. 安装gcilab-ci

   ```
   docker run -d --name gitlab-runner --restart always \
   -v /var/run/docker.sock:/var/run/docker.sock \
   gitlab/gitlab-runner:latest

   ```

   ​



