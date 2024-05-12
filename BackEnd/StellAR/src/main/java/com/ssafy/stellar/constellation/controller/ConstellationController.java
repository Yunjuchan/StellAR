package com.ssafy.stellar.constellation.controller;

import com.ssafy.stellar.constellation.dto.response.ConstellationDto;
import com.ssafy.stellar.constellation.dto.response.ConstellationEventDto;
import com.ssafy.stellar.constellation.dto.response.ConstellationXODto;
import com.ssafy.stellar.constellation.service.ConstellationService;
import com.ssafy.stellar.userConstellation.dto.response.UserConstellationDto;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.media.ArraySchema;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.tags.Tag;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@Tag(name = "Constellation", description = "별자리 관련 API")
@RestController
@Slf4j
@RequestMapping("/constellation")
public class ConstellationController {

    @Autowired
    private final ConstellationService constellationService;

    public ConstellationController(ConstellationService constellationService) {
        this.constellationService = constellationService;
    }

    // hwangdo13, 3won28su
    @GetMapping("/all")
    public ResponseEntity<?> returnAllConstellation(@RequestParam String constellationType) {
        try {
            List<ConstellationDto> dto = constellationService.findAllConstellation(constellationType);
            return new ResponseEntity<>(dto, HttpStatus.OK);
        } catch (Exception e) {
            e.printStackTrace();
            return new ResponseEntity<Void>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    // hwangdo13, 3won28su
    @GetMapping("/link")
    public ResponseEntity<?> returnConstellation(@RequestParam String constellationType) {
        try {
            Map<String, Object> object = constellationService.findConstellationLink(constellationType);
            return new ResponseEntity<>(object, HttpStatus.OK);
        } catch (Exception e) {
            e.printStackTrace();
            return new ResponseEntity<Void>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @GetMapping("/find")
    public ResponseEntity<?> returnConstellationById(@RequestParam String constellationId) {
        try {
            ConstellationDto dto = constellationService.findConstellationById(constellationId);
            return new ResponseEntity<>(dto, HttpStatus.OK);
        } catch (Exception e) {
            e.printStackTrace();
            return new ResponseEntity<Void>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @GetMapping("/event")
    public ResponseEntity<?> returnConstellationEvent() {
        try {
            List<ConstellationEventDto> list = constellationService.returnConstellationEvent();
            return new ResponseEntity<>(list, HttpStatus.OK);
        } catch (Exception e) {
            e.printStackTrace();
            return new ResponseEntity<HttpStatus>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }


    @Operation(summary = "ox 퀴즈 조회", description = "별자리에 맞는 ox퀴즈를 반환해줍니다. ox가 아니라 xo로 조금 힙하게 해봤어요." +
            " \n 그냥 빈값넣으면 전체 퀴즈가 조회됩니다. ")
    @ApiResponse(responseCode = "200", description = "퀴즈 조회..... 성공!")
    @GetMapping("/xo")
    public ResponseEntity<?> returnContellationXO(@RequestParam String constellationId) {
        try {
            List<ConstellationXODto> dto = constellationService.returnConstellationXO(constellationId);
            return new ResponseEntity<>(dto, HttpStatus.OK);
        } catch (Exception e) {
            e.printStackTrace();
            return new ResponseEntity<Void>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

}
