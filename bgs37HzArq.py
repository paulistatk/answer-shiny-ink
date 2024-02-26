import os

def add_import(file_path, import_line):
    with open(file_path, 'r+') as file:
        lines = file.readlines()
        if import_line not in lines:
            lines.insert(2, import_line + '\n')
        file.seek(0)
        file.writelines(lines)

def replace_line(file_path, old_line, new_line):
    with open(file_path, 'r+') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if old_line in line:
                lines[i] = line.replace(old_line, new_line)
        file.seek(0)
        file.writelines(lines)

# Caminhos para os arquivos
authentication_filter_path = 'src/main/java/com/example/demo/AuthenticationFilter.java'
security_config_path = 'src/main/java/com/example/demo/SecurityConfig.java'

# Adiciona as importações necessárias
add_import(authentication_filter_path, 'import org.springframework.http.MediaType;')
add_import(security_config_path, 'import org.springframework.security.web.util.matcher.AntPathRequestMatcher;')

# Corrige o código nos arquivos
replace_line(authentication_filter_path, 'httpResponse.setContentType(MediaType.APPLICATION_JSON_VALUE);', 'httpResponse.setContentType(MediaType.APPLICATION_JSON_VALUE.toString());')
replace_line(security_config_path, 'authorizationManagerRequestMatcherRegistry -> authorizationManagerRequestMatcherRegistry.requestMatchers("/**").authenticated()', 'authorizationManagerRequestMatcherRegistry -> authorizationManagerRequestMatcherRegistry.requestMatchers(new AntPathRequestMatcher("/**")).authenticated()')
