#!/bin/bash

# Adiciona a dependência javax.servlet-api ao arquivo pom.xml
sed -i '/<\/dependencies>/i\
        <dependency>\
            <groupId>javax.servlet<\/groupId>\
            <artifactId>javax.servlet-api<\/artifactId>\
            <version>4.0.1<\/version>\
            <scope>provided<\/scope>\
        <\/dependency>' pom.xml
