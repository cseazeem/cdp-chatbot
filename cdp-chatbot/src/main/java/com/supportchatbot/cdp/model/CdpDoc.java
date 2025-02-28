package com.supportchatbot.cdp.model;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;

@Entity
public class CdpDoc {
    @Id
    private Long id;
    private String platform;
    private String section;
    private String content;

    // Getters aur Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getPlatform() { return platform; }
    public void setPlatform(String platform) { this.platform = platform; }
    public String getSection() { return section; }
    public void setSection(String section) { this.section = section; }
    public String getContent() { return content; }
    public void setContent(String content) { this.content = content; }
}
