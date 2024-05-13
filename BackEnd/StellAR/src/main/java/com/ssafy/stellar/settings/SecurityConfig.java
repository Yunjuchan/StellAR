package com.ssafy.stellar.settings;

import lombok.RequiredArgsConstructor;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
@EnableWebSecurity
@RequiredArgsConstructor
public class SecurityConfig {

    @Bean
    public BCryptPasswordEncoder bCryptPasswordEncoder() {
        return new BCryptPasswordEncoder();
    }
    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity httpSecurity) throws Exception {
        httpSecurity
                .httpBasic(http -> http.disable())  // HTTP 기본 인증 비활성화
                .csrf(csrf -> csrf.disable())  // CSRF 보호 비활성화
                .cors(cors -> cors.disable())  // CORS 설정 비활성화
                .authorizeHttpRequests(auth -> auth
                        .anyRequest().permitAll());  // 모든 요청에 대해 접근 허용

        return httpSecurity.build();
    }
}
