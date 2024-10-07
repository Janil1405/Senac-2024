import java.util.Scanner;

public class Salario {
    public static void main(String[] args) {
        // Criação de um objeto Scanner para entrada de dados
        Scanner input = new Scanner(System.in);
        
        // Entrada de dados
        System.out.print("Salário Base: ");
        double salarioBase = input.nextDouble();
        
        System.out.print("Gratificação: ");
        double gratificacao = input.nextDouble();
        
        // Processamento
        double salarioBruto = salarioBase + gratificacao;
        
        // Saída
        System.out.println("O Valor do Salário bruto é R$ " + salarioBruto);
        
        // Fechar o scanner
        input.close();
    }
}
