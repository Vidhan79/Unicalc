#include <iostream>
#include <sstream>

using namespace std;

int main() {
    string input;
    double sum = 0;

    // Taking input in "pice-price" format
    cout << "Enter pice * price (format: 11-22, 30-10, 60-11): ";
    getline(cin, input);

    stringstream ss(input);
    string pair;

    // Processing input
    while (getline(ss, pair, ',')) {  
        double piece, price;
        char separator;
        stringstream pairStream(pair);

        // Extract numbers separated by '-'
        if (pairStream >> piece >> separator >> price && separator == '-') {
            double total = piece * price;
            cout << piece << " x " << price << " = " << total << endl;
            sum += total;
        }
    }

    cout << "\nFinal Total Cost: " << sum << endl;
    return 0;
}
