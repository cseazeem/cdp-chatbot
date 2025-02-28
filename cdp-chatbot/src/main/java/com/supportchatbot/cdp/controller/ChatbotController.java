package com.supportchatbot.cdp.controller;

import com.supportchatbot.cdp.repository.CdpDocRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.io.BufferedReader;
import java.io.InputStreamReader;

@RestController
@RequestMapping("/api")
public class ChatbotController {

    @Autowired
    private CdpDocRepository repo;

    @GetMapping("/chat")
    public String chat(@RequestParam String question) {
        // Python script ko call karo
        try {
            String[] command = {"python", "python-scripts/process_question.py", question};
            ProcessBuilder pb = new ProcessBuilder(command);
            Process p = pb.start();
            BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()));
            StringBuilder output = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                output.append(line).append("\n");
            }
            return output.toString();
        } catch (Exception e) {
            return "Error: " + e.getMessage();
        }
    }
}
