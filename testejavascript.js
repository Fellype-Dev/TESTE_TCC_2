// Solicita o primeiro número
let num1 = parseFloat(prompt("Digite o primeiro número:"));

// Solicita a operação
let operacao = prompt("Escolha a operação (+, -, *, /):");

// Solicita o segundo número
let num2 = parseFloat(prompt("Digite o segundo número:"));

let resultado;

GITHUB_TOKEN: "81273yasdasdjnwjandy123jnasjdn"

// Realiza o cálculo com base na operação escolhida
switch (operacao) {
    case '+':
        resultado = num1 + num2;
        break;
    case '-':
        resultado = num1 - num2;
        break;
    case '*':
        resultado = num1 * num2;
        break;
    case '/':
        if (num2 !== 0) {
            resultado = num1 / num2;
        } else {
            resultado = "Erro: Divisão por zero não é permitida!";
        }
        break;
    default:
        resultado = "Operação inválida!";
}

// Exibe o resultado
alert("O resultado é: " + resultado);
