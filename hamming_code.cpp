#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

// Function to calculate the number of parity bits needed
int calculateParityBits(int m) {
    int r = 0;
    while (pow(2, r) < (m + r + 1)) {
        r++;
    }
    return r;
}

// Function to generate Hamming Code
vector<int> generateHammingCode(vector<int>& data) {
    int m = data.size();
    int r = calculateParityBits(m);
    int n = m + r;

    vector<int> hammingCode(n, 0);

    // Placing data bits into the Hamming code positions
    int j = 0;
    for (int i = 0; i < n; i++) {
        if ((i + 1) & (i + 1 - 1)) {
            hammingCode[i] = data[j];
            j++;
        }
    }

    // Calculating parity bits
    for (int i = 0; i < r; i++) {
        int x = pow(2, i);
        for (int j = x - 1; j < n; j += 2 * x) {
            for (int k = j; k < j + x && k < n; k++) {
                hammingCode[x - 1] ^= hammingCode[k];
            }
        }
    }

    return hammingCode;
}

// Function to detect and correct errors in Hamming Code
int detectAndCorrectError(vector<int>& hammingCode) {
    int n = hammingCode.size();
    int r = log2(n + 1);
    int errorPosition = 0;

    // Detecting the error position
    for (int i = 0; i < r; i++) {
        int x = pow(2, i);
        int parity = 0;
        for (int j = x - 1; j < n; j += 2 * x) {
            for (int k = j; k < j + x && k < n; k++) {
                parity ^= hammingCode[k];
            }
        }
        errorPosition += parity * x;
    }

    if (errorPosition) {
        cout << "Error detected at position: " << errorPosition << endl;
        hammingCode[errorPosition - 1] ^= 1;  // Correct the error
        cout << "Error corrected." << endl;
    } else {
        cout << "No error detected." << endl;
    }

    return errorPosition;
}

int main() {
    // Example data bits
    vector<int> data = {1, 0, 1, 1};

    // Generate Hamming Code
    vector<int> hammingCode = generateHammingCode(data);

    cout << "Generated Hamming Code: ";
    for (int bit : hammingCode) {
        cout << bit << " ";
    }
    cout << endl;

    // Simulate an error (for example, flipping the 5th bit)
    hammingCode[4] ^= 1;

    cout << "Hamming Code with an error introduced: ";
    for (int bit : hammingCode) {
        cout << bit << " ";
    }
    cout << endl;

    // Detect and correct the error
    detectAndCorrectError(hammingCode);

    cout << "Corrected Hamming Code: ";
    for (int bit : hammingCode) {
        cout << bit << " ";
    }
    cout << endl;

    return 0;
}



// g++ hamming_code.cpp -o hamming_code
// ./hamming_code