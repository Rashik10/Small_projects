#include <iostream>
#include <cmath>
using namespace std;

// InterestCalculator class definition
class InterestCalculator {
public:
    static double calculateSimpleInterest(double principal, double rate, double time);
    static double calculateCompoundInterest(double principal, double rate, double time, int frequency);
};

// Function to calculate simple interest
double InterestCalculator::calculateSimpleInterest(double principal, double rate, double time) {
    return (principal * rate * time) / 100;
}

// Function to calculate compound interest
double InterestCalculator::calculateCompoundInterest(double principal, double rate, double time, int frequency) {
    return principal * pow((1 + rate / (frequency * 100)), frequency * time) - principal;
}

int main() {
    double principal, rate, time;
    int frequency;
    char choice;

    cout << "Welcome to the Interest Calculator" << endl;
    
    cout << "Enter the principal amount: ";
    cin >> principal;
    
    cout << "Enter the rate of interest (in %): ";
    cin >> rate;
    
    cout << "Enter the time period (in years): ";
    cin >> time;
    
    cout << "Choose the type of interest calculation:" << endl;
    cout << "1. Simple Interest" << endl;
    cout << "2. Compound Interest" << endl;
    cin >> choice;
    
    if (choice == '1') {
        double simpleInterest = InterestCalculator::calculateSimpleInterest(principal, rate, time);
        cout << "The Simple Interest is: " << simpleInterest << endl;
        cout << "You will Get: " << simpleInterest + principal << endl;
    } else if (choice == '2') {
        cout << "Enter the number of times that interest is compounded per year: ";
        cin >> frequency;
        
        double compoundInterest = InterestCalculator::calculateCompoundInterest(principal, rate, time, frequency);
        cout << "The Compound Interest is: " << compoundInterest << endl;
        cout << "You will Get: " << compoundInterest + principal << endl;
    } else {
        cout << "Invalid choice!" << endl;
    }

    return 0;
}



// g++ interest_calculator.cpp -o interest_calculator
// interest_calculator