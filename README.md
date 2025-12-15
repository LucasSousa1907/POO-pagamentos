# Sistema de Pagamentos (POO)

## Descrição
Este projeto é um exemplo simples de Programação Orientada a Objetos (POO) em Python, baseado em um diagrama de classes UML. O sistema simula diferentes formas de pagamento.

## Estrutura
- Pagamento (classe base)
- PagamentoCartao
- PagamentoPix
- PagamentoBoleto

## Conceitos de POO Utilizados
- Abstração: a classe Pagamento define um método que deve ser implementado.
- Herança: as classes de pagamento herdam da classe Pagamento.
- Polimorfismo: o método processar_pagamento possui comportamentos diferentes em cada classe.
- Encapsulamento: cada classe possui seus próprios atributos.

## Exemplo de Uso
O sistema permite processar pagamentos de diferentes tipos utilizando o mesmo método.
