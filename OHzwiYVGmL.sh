#!/bin/bash

# Cria o arquivo ResourceController.java
cat << EOF > src/main/java/com/example/demo/ResourceController.java
package com.example.demo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ResourceController {
    @GetMapping("/home")
    public String homeEndpoint() {
        return "Baeldung !";
    }
}
EOF
