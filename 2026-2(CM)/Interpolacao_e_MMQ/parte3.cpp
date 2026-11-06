#include <iostream>
#include <Eigen/Dense>

// fixar o tamanho dos dados 
const int N = 20;


// aqui estão os dados referentes à parte 3
const double T[N] = {
    290.0, 300.0, 310.0, 320.0, 330.0, 340.0, 350.0, 360.0, 370.0, 380.0,
    390.0, 400.0, 410.0, 420.0, 430.0, 440.0, 450.0, 460.0, 470.0, 480.0
};

const double k[N] = {
    4.12e-15, 7.35e-15, 1.28e-14, 2.15e-14, 3.52e-14, 5.64e-14, 8.85e-14, 1.36e-13, 2.04e-13, 3.01e-13,
    4.38e-13, 6.25e-13, 8.78e-13, 1.21e-12, 1.65e-12, 2.22e-12, 2.94e-12, 3.86e-12, 5.01e-12, 6.44e-12
};


// Aqui crio a matriz que ajudará a construir o sistema normal
double A_original[N][2];


// Essa função é só para printar a matriz A
void imprimirA(const double A[N][2]) {
    for (int i = 0; i < N; ++i) {
        std::cout << A[i][0] << " " << A[i][1] << "\n";
    }
}

// Essa função constrói a matriz A
void A_construction(double A[N][2]) {
    for (int i = 0; i < N; ++i) {
        A_original[i][0] = 1.0;
        A_original[i][1] = 1.0 / T[i];
    }
}

int main() {
    A_construction(A_original);

    //Aqui começamos a construir os elementos para a biblioteca Eigen/Dense
    Eigen::MatrixXd A(N,2);
    Eigen::VectorXd y(N);

    for(int i = 0; i<N; ++i){
        A(i,0) = A_original[i][0];
        A(i,1) = A_original[i][1];
        y(i)   = std::log(k[i]);
    }

    // Construção do sistema normal, referente ao problema linearizado
    Eigen::MatrixXd AtA = A.transpose() * A;
    Eigen::VectorXd Aty = A.transpose() * y;

    // Solver do sistema normal
    Eigen::Vector2d c = AtA.ldlt().solve(Aty);


    //resultados já convertidos
    double Ea = c[1]*8.314;
    double A0 = std::exp(c[0]);

    
    std::cout << A0 << "\n";
    std::cout << Ea << "\n";

    return 0;
}