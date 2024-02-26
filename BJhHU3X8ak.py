import os

def update_properties_file(file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    exclude_line = "spring.autoconfigure.exclude=org.springframework.boot.autoconfigure.security.servlet.SecurityAutoConfiguration,org.springframework.boot.autoconfigure.security.servlet.UserDetailsServiceAutoConfiguration\n"
    
    with open(file_path, 'a') as file:
        file.write(exclude_line)

# Substitua 'src/main/resources/application.properties' pelo caminho do seu arquivo de propriedades
update_properties_file('src/main/resources/application.properties')
