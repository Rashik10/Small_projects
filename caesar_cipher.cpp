#include <iostream>
#include <string>

using namespace std;

// Function to encrypt the text using Caesar Cipher
string caesarCipherEncrypt(string text, int shift) {
    string result = "";

    // Traverse through the text
    for (int i = 0; i < text.length(); i++) {
        char ch = text[i];

        // Encrypt uppercase letters
        if (isupper(ch)) {
            ch = char(int(ch + shift - 65) % 26 + 65);
        }
        // Encrypt lowercase letters
        else if (islower(ch)) {
            ch = char(int(ch + shift - 97) % 26 + 97);
        }

        // Append the encrypted character to the result
        result += ch;
    }

    return result;
}

// Function to decrypt the text using Caesar Cipher
string caesarCipherDecrypt(string text, int shift) {
    return caesarCipherEncrypt(text, 26 - shift);
}

int main() {
    string text;
    int shift;

    // Get the text to be encrypted
    cout << "Enter the text to be encrypted: ";
    getline(cin, text);

    // Get the shift value
    cout << "Enter the shift value: ";
    cin >> shift;

    // Encrypt the text
    string encryptedText = caesarCipherEncrypt(text, shift);
    cout << "Encrypted Text: " << encryptedText << endl;

    // Decrypt the text
    string decryptedText = caesarCipherDecrypt(encryptedText, shift);
    cout << "Decrypted Text: " << decryptedText << endl;

    return 0;
}



// g++ caesar_cipher.cpp -o caesar_cipher
// caesar_cipher