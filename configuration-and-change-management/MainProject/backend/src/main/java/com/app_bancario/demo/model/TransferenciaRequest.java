package com.app_bancario.demo.model;

public class TransferenciaRequest {
    private String idDestino;
    private double valor;

    public String getIdDestino() {
        return idDestino;
    }

    public void setIdDestino(String idDestino) {
        this.idDestino = idDestino;
    }

    public double getValor() {
        return valor;
    }

    public void setValor(double valor) {
        this.valor = valor;
    }
}
