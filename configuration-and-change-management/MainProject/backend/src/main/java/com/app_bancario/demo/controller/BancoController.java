package com.app_bancario.demo.controller;


import org.springframework.web.bind.annotation.*;

import com.app_bancario.demo.model.TransferenciaRequest;
import com.app_bancario.demo.service.BancoService;

@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "*") // Permite acesso do frontend (HTML)
public class BancoController {

    private final BancoService bancoService;

    public BancoController(BancoService bancoService) {
        this.bancoService = bancoService;
    }

    @GetMapping("/saldo")
    public double getSaldo() {
        return bancoService.getSaldo();
    }

    @PostMapping("/transferir")
    public String transferir(@RequestBody TransferenciaRequest request) {
        return bancoService.transferir(request.getIdDestino(), request.getValor());
    }
}
