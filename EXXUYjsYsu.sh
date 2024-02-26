#!/bin/bash

# Cria o arquivo ApiKeySecretAuthApplication.java
cat << EOF > src/main/java/com/example/demo/ApiKeySecretAuthApplication.java
package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.security.servlet.SecurityAutoConfiguration;
import org.springframework.boot.autoconfigure.security.servlet.UserDetailsServiceAutoConfiguration;

@SpringBootApplication(exclude = {SecurityAutoConfiguration.class, UserDetailsServiceAutoConfiguration.class})
public class ApiKeySecretAuthApplication {

    public static void main(String[] args) {
        SpringApplication.run(ApiKeySecretAuthApplication.class, args);
    }
}
EOF
