#Stage 1
FROM maven:3.6.3-openjdk as build
MAINTAINER Yurii Bakhur "yurabahur@gmail.com"
ENV MAVEN_OPTS "-Xmx1024m"
#Test webhook
#Copy files to container
RUN mkdir FootGo
COPY . /FootGo
RUN cp /FootGo/src/main/resources/application.properties.example /FootGo/src/main/resources/application.properties

#Run mvn 
WORKDIR /FootGo
RUN mvn package

#Stage 2
FROM openjdk:8-jre-alpine as prod
#Start app
RUN mkdir /home/webapp
WORKDIR /home/webapp

#Copy ROOT.war to WORKDIR
COPY --from=build /FootGo/target .
WORKDIR /home/webapp
ENTRYPOINT java -jar ROOT.war
