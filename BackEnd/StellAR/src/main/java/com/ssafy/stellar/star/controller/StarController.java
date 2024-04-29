package com.ssafy.stellar.star.controller;


import com.ssafy.stellar.star.dto.response.StarDto;
import com.ssafy.stellar.star.service.StarService;
import io.swagger.v3.oas.annotations.tags.Tag;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@Tag(name = "Star", description = "별 관련 API")
@RestController
@Slf4j
@RequestMapping("/star")
public class StarController {

    private final StarService starService;

    public StarController(StarService starService) {
        this.starService = starService;
    }

    @GetMapping("/all")
    public ResponseEntity<?> returnAllStar() {
        try {
            List<StarDto> list = starService.returnAllStar();

            return new ResponseEntity<List<StarDto>>(list, HttpStatus.OK);
        } catch (Exception e) {
            e.printStackTrace();
            return new ResponseEntity<Void>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @GetMapping("/info")
    public ResponseEntity<?> starInfo(@RequestParam String starId) {
        try {
            StarDto dto = new StarDto();

            return new ResponseEntity<StarDto>(dto, HttpStatus.OK);
        } catch (Exception e) {
            e.printStackTrace();
            return new ResponseEntity<Void>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }


}
