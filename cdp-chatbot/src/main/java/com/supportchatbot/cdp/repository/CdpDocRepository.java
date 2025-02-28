package com.supportchatbot.cdp.repository;

import com.supportchatbot.cdp.model.CdpDoc;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface CdpDocRepository extends JpaRepository<CdpDoc, Long> {
    List<CdpDoc> findByPlatform(String platform);
}