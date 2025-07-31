package com.example.spamdetector.controller;

import com.example.spamdetector.model.EmailRequest;
import com.example.spamdetector.service.SpamDetectionService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
@CrossOrigin
public class SpamDetectorController {

    @Autowired
    private SpamDetectionService spamDetectionService;

    @PostMapping("/check-email")
    public String checkEmail(@RequestBody EmailRequest emailRequest) {
        return spamDetectionService.checkSpam(emailRequest.getContent());
    }
}
