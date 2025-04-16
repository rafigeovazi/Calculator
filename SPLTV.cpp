#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

void gauss_jordan() {
    int n = 3;
    vector<vector<double>> A(n, vector<double>(n + 1));

    cout << "Masukkan koefisien dan konstanta dari sistem persamaan linear:\n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << "Masukkan koefisien a" << i + 1 << j + 1 << ": ";
            cin >> A[i][j];
        }
        cout << "Masukkan konstanta b" << i + 1 << ": ";
        cin >> A[i][n];
    }

    for (int i = 0; i < n; i++) {
        if (A[i][i] == 0.0) {
            cout << "Matematis tidak valid (tidak bisa dibagi dengan 0)\n";
            return;
        }

        for (int j = 0; j < n; j++) {
            if (i != j) {
                double ratio = A[j][i] / A[i][i];
                for (int k = 0; k < n + 1; k++) {
                    A[j][k] -= ratio * A[i][k];
                }
            }
        }
    }

    vector<double> solution(n);
    for (int i = 0; i < n; i++) {
        solution[i] = A[i][n] / A[i][i];
    }

    cout << "\nSolusi dari sistem persamaan adalah:\n";
    for (int i = 0; i < n; i++) {
        cout << "Variable " << static_cast<char>('x' + i) << " = " << fixed << setprecision(8) << solution[i] << endl;
    }
}

int main() {
    gauss_jordan();
    return 0;
}
