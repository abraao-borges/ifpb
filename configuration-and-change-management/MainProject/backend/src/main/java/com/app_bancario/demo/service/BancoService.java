package com.app_bancario.demo.service;

import org.springframework.stereotype.Service;

@Service
public class BancoService {
    private double saldo = 1500.00;

    public double getSaldo() {
        return saldo;
    }

    public String transferir(String idDestino, double valor) {
        if (valor <= 0) {
            return "Valor inválido.";
        }

        if (valor > saldo) {
            return "Saldo insuficiente.";
        }

        saldo -= valor;
        return String.format("Transferência de R$ %.2f para ID %s realizada com sucesso.", valor, idDestino);
    }
}
