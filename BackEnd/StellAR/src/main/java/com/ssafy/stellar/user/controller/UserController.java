package com.ssafy.stellar.user.controller;

import com.ssafy.stellar.user.entity.UserEntity;
import com.ssafy.stellar.user.service.UserService1;
import io.swagger.v3.oas.annotations.tags.Tag;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@Tag(name = "", description = "")
@RestController
@Slf4j
@RequestMapping("/user")
public class UserController {

    private final UserService1 userService;

    public UserController(UserService1 userService) { this.userService = userService;}

    @PostMapping("/signUp")
    public HttpEntity<?> signUp(@ModelAttribute UserEntity user) {
        try {
            userService.signUp(user);
            return new ResponseEntity<Void>(HttpStatus.CREATED);
        } catch (Exception e) {
            e.printStackTrace();
            return new ResponseEntity<String>("응 아니야", HttpStatus.BAD_REQUEST);
        }

    }

    @PostMapping("/login")
    public HttpEntity<?> login(@RequestParam String userId, @RequestParam String password) {

        UserEntity user = userService.logIn(userId, password);

        if (user != null) {
            return new ResponseEntity<UserEntity>(user, HttpStatus.OK);
        } else {
            return new ResponseEntity<String>("응 아니야", HttpStatus.BAD_REQUEST);
        }
    }

    @PostMapping("/deleteUser")
    public HttpEntity<?> deleteUser(@RequestParam String userId, @RequestParam String password) {
        if (userService.checkPassword(userId, password)) {
            userService.deleteUser(userId);
            return new ResponseEntity<Void>(HttpStatus.NO_CONTENT);
        } else {
            return new ResponseEntity<String>("응 아니야", HttpStatus.BAD_REQUEST);
        }
    }
}
